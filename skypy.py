from skypy_constants import *

# API Calls
import aiohttp
import asyncio
from datetime import datetime
import time
# --------

_session = None

async def session():
    global _session
    if _session is None:
        _session = aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=15), raise_for_status=True)
    return _session

# Inventory parsing
from base64 import b64decode as one
from gzip import decompress as two
from io import BytesIO as three
from struct import unpack
import re
# -----------------

class SkyblockError(Exception):
    """A general exception from the skyblock library"""


class NeverPlayedSkyblockError(SkyblockError):
    """This user has never played skyblock before!"""
        
class HypixelAPIError(SkyblockError):
    """There was an issue connecting to the Hypixel API"""
    def __init__(self, reason): 
        self.reason = reason
    
class HypixelInternalError(SkyblockError):
    """Hypixel broke"""
    def __init__(self, reason): 
        self.reason = reason
     
class BadNameError(SkyblockError):
    """This uuid, username, or guild name is invalid"""
    def __init__(self, reason): 
        self.reason = reason
        
class APIKeyError(SkyblockError):
    """You used an invalid API key"""
    def __init__(self, reason): 
        self.reason = reason

def decode_inventory_data(raw):
    """Takes a raw string representing inventory data.
    Returns a json object with the inventory's contents"""

    raw = three(two(one(raw)))  # Unzip raw string from the api

    def read(type, length):
        if type in 'chil':
            return int.from_bytes(raw.read(length), byteorder='big')
        if type == 's':
            return raw.read(length).decode('utf-8')
        return unpack('>' + type, raw.read(length))[0]

    def parse_list():
        subtype = read('c', 1)
        payload = []
        for _ in range(read('i', 4)):
            parse_next_tag(payload, subtype)
        return payload

    def parse_compound():
        payload = {}
        while parse_next_tag(payload) != 0:  # Parse tags until we find an endcap (type == 0)
            pass  # Nothing needs to happen here
        return payload

    payloads = {
        1: lambda: read('c', 1),  # Byte
        2: lambda: read('h', 2),  # Short
        3: lambda: read('i', 4),  # Int
        4: lambda: read('l', 8),  # Long
        5: lambda: read('f', 4),  # Float
        6: lambda: read('d', 8),  # Double
        7: lambda: raw.read(read('i', 4)),  # Byte Array
        8: lambda: read('s', read('h', 2)),  # String
        9: parse_list,  # List
        10: parse_compound,  # Compound
        11: lambda: [read('i', 4) for _ in range(read('i', 4))],  # Int Array
        12: lambda: [read('l', 8) for _ in range(read('i', 4))]  # Long Array
    }

    def parse_next_tag(dictionary, tag_id=None):
        if tag_id is None:  # Are we inside a list?
            tag_id = read('c', 1)
            if tag_id == 0:  # Is this the end of a compound?
                return 0
            name = read('s', read('h', 2))

        payload = payloads[tag_id]()
        if isinstance(dictionary, dict):
            dictionary[name] = payload
        else:
            dictionary.append(payload)

    raw.read(3)  # Remove file header (we ingore footer)
    root = {}
    parse_next_tag(root)
    return [Item(x, i) for i, x in enumerate(root['i']) if x]


class Item:
    def __init__(self, nbt, slot_number):
        self.__nbt__ = nbt

        self.stack_size = self.__nbt__.get('Count', 1)
        self.slot_number = slot_number
        self.internal_name = self['tag'].get('ExtraAttributes', {}).get('id', None)
        self.description = self['tag'].get('display', {}).get('Lore', None)
        self.hot_potatos = self['tag'].get('ExtraAttributes', {}).get('hot_potato_count', 0)
        self.collection_date = self['tag'].get('ExtraAttributes', {}).get('timestamp', '') # 'timestamp': '2/16/20 9:24 PM',
        self.runes = self['tag'].get('ExtraAttributes', {}).get('runes', {}) # 'runes': {'ZOMBIE_SLAYER': 3},

        try:
            self.enchantments = self['tag']['ExtraAttributes']['enchantments']
        except KeyError:
            self.enchantments = {}

        if self.description:
            for i, txt in enumerate(self.description):
                self.description[i] = re.sub('§.', '', txt)

            rarity_type = self.description[-1].split()
            self.rarity = rarity_type[0].lower()
            self.type = rarity_type[1].lower() if len(rarity_type) > 1 else None
            for type, list in {'sword': sword_enchants, 'bow': bow_enchants, 'fishing rod': rod_enchants}.items():
                for e in list:
                    if e in self.enchantments:
                        self.type = type
                        break
        else:
            self.rarity = None
            self.type = None

        self.name = re.sub('§.', '', self['tag']['display']['Name'])

    def __getitem__(self, name):
        return self.__nbt__[name]

    def __eq__(self, other):
        return self.internal_name == (other if isinstance(other, str) else other.internal_name)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def rarity_level(self):
        return ['common', 'uncommon', 'rare', 'epic', 'legendary', 'special'].index(self.rarity)

    def reforge(self):
        try:
            return self['tag']['ExtraAttributes']['modifier']
        except KeyError:
            return None

    # Why do we have to sift the lorestring for this?
    # Can't it just be in the nbt data?
    def stats(self, use_reforge=True):
        results = {}
        name = self.internal_name
                
        reforge_multiplier = 1
        
        # §7Attack Speed: §c+2% §8(Itchy +2%)
        # §7Intelligence: §a+9 §c(Godly +3)
        reg = re.compile(
            '(Damage|'
            'Strength|'
            'Crit Chance|'
            'Crit Damage|'
            'Attack Speed|'
            'Health|'
            'Defense|'
            'Speed|'
            'Intelligence)'
            ': \+(\d+).*'
        )
        for line in self.description:
            match = reg.match(line)
            if match:
                results[match[1].lower()] = int(match[2])
                
        def add(stat, amount):
            results[stat] = results.get(stat, 0) + amount

        end_defence = {'END_HELMET': 35, 'END_CHESTPLATE': 60, 'END_LEGGINGS': 50, 'END_BOOTS': 25}
                
        if name == 'RECLUSE_FANG':
            add('strength', 370)
        elif name == 'THE_SHREDDER':
            add('damage', 115)
            add('strength', 15)
        elif name == 'NIGHT_CRYSTAL' or name == 'DAY_CRYSTAL':
            add('strength', 2.5)
            add('defense', 2.5)
        elif name == 'CAKE_BAG':
            # add('health', len(decode_inventory_data(self[][][])))
            pass
        elif name == 'GRAVITY_TALISMAN':
            add('strength', 10)
            add('defense', 10)
        elif name in end_defence.keys():
            if results['defense'] - self.hot_potatos * 2 <= end_defence[self.internal_name] * 2:
                for k in results.keys():
                    results[k] *= 2
            else:
                reforge_multiplier = 2

        if use_reforge is False:
            reforge = self.reforge()
            if reforge:
                for stat, amount in reforges[self.reforge()][self.rarity_level()].items():
                    if stat in results:
                        results[stat] -= amount * reforge_multiplier
        return results

def damage(weapon_dmg, strength, crit_dmg, ench_modifier):
    return (5 + weapon_dmg + strength // 5) * (1 + strength / 100) * (1 + crit_dmg / 100) * (1 + ench_modifier / 100)

async def fetch_uuid_uname(uname_or_uuid):
    try:
        r = await (await session()).get(f'https://mc-heads.net/minecraft/profile/{uname_or_uuid}')
        json = await r.json(content_type=None)
        return (json['name'], json['id'])
    except aiohttp.ClientResponseError as e:
        if e.status == 204:
            raise BadNameError('Invalid uname!') from None
        else:
            raise e from None
    finally:
        r.close()

class ApiInterface:
    def __next_key__(self):
        self.__key_id__ += 1
        if self.__key_id__ == len(self.__api_keys__):
            self.__key_id__ = 0
        return self.__api_keys__[self.__key_id__]

    async def __call_api__(self, api, **kwargs):
        kwargs['key'] = self.__next_key__()
        url = f'https://api.hypixel.net{api}'
        
        try:
            async with (await session()).get(url, params=kwargs) as data:
                data = await data.json(content_type=None)
                
                if data['success']:
                    return data
                    
                elif data['cause'] == 'Key throttle!':
                    await asyncio.sleep(0.5)
                    return await self.__call_api__(api, **kwargs)
                    
                elif data['cause'] == 'Invalid API key!':
                    raise APIKeyError(f'Invalid key {kwargs["key"]}!')
                    
                elif data['cause'] == 'Internal error':
                    raise HypixelInternalError(f'Hypixel\'s servers could not complete your request')
                    
                else:
                    raise HypixelAPIError(data['cause'])
        except asyncio.TimeoutError:
            return await self.__call_api__(api, **kwargs)
    
    async def __new__(cls, keys, *args, **kwargs):
        instance = super().__new__(cls)
        
        if isinstance(keys, str):
            instance.__api_keys__ = [keys]
        else:
            instance.__api_keys__ = keys

        instance.__key_id__ = 0
        
        await instance.__init__(*args, **kwargs)
        return instance

class Guild(ApiInterface):
    """A class representing a Skyblock guild.
    Instantiate with either Guild(api_key, gname=guildname) or Guild(api_key, gid=guildid)
    api_key can either be a single key or a list of keys
    a list is highly recommended for bigger guilds"""

    async def __init__(self, *, gname=None, gid=None, profile_selection=None):
        if gid:
            self.gid = gid
            self.data = (await self.__call_api__('/guild', id=gid))['guild']
        elif gname:
            self.gid = (await self.__call_api__('/findGuild', byName=gname))['guild']
            if self.gid is None:
                raise BadNameError('Bad guildname')
            self.data = (await self.__call_api__('/guild', id=self.gid))['guild']
        else:
            raise SkyblockError('You need to provide either a guildname or guild id!')

        if self.data is None:
            raise BadNameError('Bad guildname')

        v = self.data
        self.gname = v['name']
        self.created = v['created']
        self.gxp = v['exp']
        self.tag = v.get('tag')
        self.description = v.get('description')
                
        xp = self.gxp
        for level, requirement in enumerate(guild_level_requirements):
            if xp >= requirement:
                xp -= requirement
            else:
                break
        level += xp // guild_level_requirements[-1]
        self.level = level

        self.players = []
        for player in asyncio.as_completed([Player(self.__api_keys__, uuid=member['uuid']) for member in self.data['members']]):
            try:
                player = await player
                self.players.append(player)
            except NeverPlayedSkyblockError:
                pass
        
        if profile_selection:
            await asyncio.gather(*[player.set_profile_automatically(profile_selection) for player in self.players])
        else:
            await asyncio.gather(*[self.set_profile_quickly(player) for player in self.players])

    def __iter__(self):
        return iter(self.players)

    def __str__(self):
        return str(self.players)

    def __len__(self):
        return len(self.players)

    def __getitem__(self, index):
        return self.players[index]

    def __getattr__(self, attr):
        if len(self) == 0:
            return 0
        
        type = getattr(self[0], attr)
        
        if isinstance(type, int) or isinstance(type, float):
            sum = 0
            for player in self:
                sum += getattr(player, attr)
            return sum
        
        if isinstance(type, dict):
            result = {}
            for player in self:
                d = getattr(player, attr)
                for k, v in d.items():
                    if k in result:
                        result[k] += v
                    else:
                        result[k] = v
            return result
            
        '''
        if type == list or type == tuple:
            result = []
            for player in self:
                l = getattr(player, attr)
                for i in l:
                    result.a
        ''' 
        
    def stat_average(self, attr):
        normal = self.__getattr__(attr)
        if len(self) == 0:
            return 0
        
        type = getattr(self[0], attr)
        
        if isinstance(type, int) or isinstance(type, float):
            sum = 0
            count = 0
            for player in self:
                amount = getattr(player, attr)
                if amount != 0:
                    sum += amount
                    count += 1
            return sum / count
        
        if isinstance(type, dict):
            result = {}
            for player in self:
                d = getattr(player, attr)
                for k, v in d.items():
                    if v != 0:
                        if k in result:
                            result[k][0] += v
                            result[k][1] += 1
                        else:
                            result[k] = [v, 1]
            return {k: v[0] / v[1] for k, v in result.items()}
        
    async def set_profile_quickly(self, player):
        for profile in reversed(player.profiles.values()):
            try:
                await player.set_profile(profile)
            except HypixelInternalError:
                continue
            if player.total_slayer_exp >= 10000:
                break

class Player(ApiInterface):
    """A class representing a Skyblock player.
    Instantiate the class with Player(api_key, username) or Player(api_key, uuid)
    Use profiles() and set_profile() to retrieve and define all the profile data.
    Use weapons() and set_weapon() to retrieve and set the player's weapon."""

    async def __init__(self, *, uname=None, uuid=None, guild=False):
        if not uuid and not uname:
            raise SkyblockError('You need to provide either a minecraft username or uuid!')
        elif not uuid:
            self.uname, self.uuid = await fetch_uuid_uname(uname)
        else:
            self.uname, self.uuid = await fetch_uuid_uname(uuid)

        try:
            self.profiles = {}
            player = await self.__call_api__('/player', uuid=self.uuid)
            profile_ids = player['player']['stats']['SkyBlock']['profiles']

            self.achievements = player['player']['achievements']

            for k, v in profile_ids.items():
                self.profiles[v['cute_name']] = k
                
        except (KeyError, TypeError):
            raise NeverPlayedSkyblockError from None
        if not self.profiles:
            raise NeverPlayedSkyblockError
            
        if guild:
            id = (await self.__call_api__('/findGuild', byUuid=self.uuid))['guild']
            if id:
                self.guild_id = id
                self.guild_info = (await self.__call_api__('/guild', id=self.guild_id))['guild']
                self.guild = self.guild_info['name']
            else:
                self.guild_id = None
                self.guild_info = None
                self.guild = None

    def __str__(self):
        return self.uname

    def __repr__(self):
        return self.uname

    def avatar(self, size=None):
        if size:
            return f'https://mc-heads.net/minecraft/profile/{self.uuid}/{size}'
        else:
            return f'https://mc-heads.net/minecraft/profile/{self.uuid}'

    async def set_profile_automatically(self, attribute=lambda player: player.total_slayer_exp):
        """Sets a player profile automatically
        <attribute> is a function that takes a <Player> class and returns whatever value you want to set it based on
        example: player.set_profile_automatically(lambda player: player.skill_experience['combat'])"""
        best = None
        max = 0
        
        async def return_profile(profile):
            try:
                await self.set_profile(profile)
                return profile
            except HypixelInternalError:
                return None
        
        for profile in asyncio.as_completed([return_profile(profile) for profile in self.profiles.values()]):
            profile = await profile
            if profile is not None:
                cur = attribute(self)
                if best is None or cur > max:
                    max = cur
                    best = profile
                
        await self.set_profile(best)

    async def set_profile(self, profile):
        """Sets a player's profile based on the provided profile id. Also retrieves all api data for that profile."""
        self.profile = profile
        for cute_name, id in self.profiles.items():
            if id == profile:
                self.profile_name = cute_name
                break
        else:
            raise SkyblockError('hey fucker that\'s a bullshit profile id and you know it')

        self.__api_data__ = (await self.__call_api__('/skyblock/profile', profile=self.profile))['profile']
        v = self.__api_data__['members'][self.uuid]

        self.enabled_api = {'skills': False, 'collection': False, 'inventory': False, 'banking': False}

        if 'banking' in self.__api_data__:
            self.enabled_api['banking'] = True
            self.bank_balance = float(self.__api_data__['banking'].get('balance', 0))
        else:
            self.bank_balance = 0
        
        def parse_collections(data):
            try:
                tuples = []
                for s in v[data]:
                    temp = re.split('_(?!.*_)', s, maxsplit=1)
                    temp[1] = int(temp[1])
                    tuples.append(temp)
                dictionary = {}
                for s in set(name for name, level in tuples):
                    max = 0
                    for name, level in tuples:
                        if name == s and level > max:
                            max = level
                    dictionary[s.lower().replace('_', ' ')] = max
                return dictionary
            except KeyError:
                return {}

        try:
            self.collections = {name.lower().replace('_', ' '): level for name, level in v['collection'].items()}
            self.enabled_api['collection'] = True
        except KeyError:
            self.collections = {}
        self.unlocked_collections = parse_collections('unlocked_coll_tiers')
        self.minions = parse_collections('crafted_generators')
        self.unique_minions = max(
            self.achievements.get('skyblock_minion_lover', 0),
            sum(self.minions.values())
        )

        for slots, req in enumerate(minion_slot_requirements):
            if self.unique_minions < req:
                break
                
        self.minion_slots = slots

        def optional_inv(*path):
            try:
                result = v
                for key in path:
                    result = result[key]
                return decode_inventory_data(result)
            except KeyError:
                return []

        self.inventory = optional_inv('inv_contents', 'data')
        self.echest = optional_inv('ender_chest_contents', 'data')
        self.armor = optional_inv('inv_armor', 'data')
        self.weapons = [item for item in self.inventory + self.echest if
                        item.type in ('sword', 'bow', 'fishing rod')]
        self.candy_bag = optional_inv('candy_inventory_contents', 'data')
        self.talisman_bag = optional_inv('talisman_bag', 'data')
        self.potion_bag = optional_inv('potion_bag', 'data')
        self.fish_bag = optional_inv('fishing_bag', 'data')
        self.quiver = optional_inv('quiver', 'data')

        if self.inventory or self.echest or self.talisman_bag:
            self.enabled_api['inventory'] = True

        self.talismans = [talisman for talisman in self.inventory + self.talisman_bag if talisman.type == 'accessory']
        for i, talisman in enumerate(self.talismans):
            talisman.active = True

            # Check for duplicate talismans
            if self.talismans[i:].count(talisman) > 1:
                talisman.active = False

            # Check for talisman families
            for other in self.talismans:
                for familiy in tiered_talismen:
                    if talisman in familiy and other in familiy and familiy.index(talisman) < familiy.index(other):
                        talisman.active = False

        self.join_date = datetime.fromtimestamp(v.get('first_join', 0) / 1000.0)
        self.fairy_souls_collected = v.get('fairy_souls_collected', 0)
        self.purse = float(v.get('coin_purse', 0))

        self.kills = int(v.get('stats', {'kills': 0}).get('kills', 0))
        self.specifc_kills = {name.replace('kills_', '').replace('_', ' '): int(amount)
                              for name, amount in v['stats'].items() if re.match('kills_', name)}
        self.deaths = int(v.get('stats', {'deaths': 0}).get('deaths', 0))
        self.specifc_deaths = {name.replace('deaths_', '').replace('_', ' '): int(amount)
                               for name, amount in v['stats'].items() if re.match('deaths_', name)}

        if 'experience_skill_farming' in v:
            def parse_skill(skill):
                try:
                    return int(v['experience_skill_' + skill])
                except KeyError:
                    return 0

            self.skill_experience = {
                name: parse_skill(name)
                for name in ['farming', 'mining', 'foraging', 'combat', 'enchanting', 'alchemy', 'fishing', 'carpentry',
                             'runecrafting']
            }
        
            self.enabled_api['skills'] = True
        
            def parse_exp(exp, runecrafting=False):
                for lvl, requirement in enumerate(runecrafting_exp_requirements if runecrafting else skill_exp_requirements):
                    if exp >= requirement:
                        exp -= requirement
                    else:
                        break
                else:
                    lvl += 1
                return lvl

            self.skills = {
                name: parse_exp(parse_skill(name), name == 'runecrafting')
                for name in ['farming', 'mining', 'foraging', 'combat', 'enchanting', 'alchemy', 'fishing', 'carpentry', 'runecrafting']
            }
        else:
            self.skills = {
                name: self.achievements.get(achievement, 0)
                for name, achievement in [
                    ('farming', 'skyblock_harvester'),
                    ('mining', 'skyblock_excavator'),
                    ('foraging', 'skyblock_gatherer'),
                    ('combat', 'skyblock_combat'),
                    ('enchanting', 'skyblock_augmentation'),
                    ('alchemy', 'skyblock_concoctor'),
                    ('fishing', 'skyblock_angler')
                ]
            }
            
            self.skill_experience = {skill: sum(skill_exp_requirements[:level]) for skill, level in self.skills.items()}
            
            self.skills['carpentry'] = 0
            self.skills['runecrafting'] = 0
            self.skill_experience['carpentry'] = 0
            self.skill_experience['runecrafting'] = 0

        self.skill_average = sum(list(self.skills.values())[0:7]) / 7

        def parse_slayer_api(name):
            try:
                return int(list(v['slayer_bosses'][name]['claimed_levels'].keys())[-1].replace('level_', ''))
            except (IndexError, KeyError):
                return 0

        self.slayer_levels = {
            'zombie': parse_slayer_api('zombie'),
            'spider': parse_slayer_api('spider'),
            'wolf': parse_slayer_api('wolf')
        }
        
        try:
            self.slayer_exp = {name: v['slayer_bosses'][name]['xp'] for name in ('zombie', 'spider', 'wolf')}
        except KeyError:
            self.slayer_exp = {'zombie': 0, 'spider': 0, 'wolf': 0}
        self.total_slayer_exp = sum(self.slayer_exp.values())

    async def is_online(self):
        player_data = (await self.__call_api__('/player', name=self.uname))['player']
        return player_data['lastLogout'] < player_data['lastLogin']

    def base_stats(self):
        return {'damage': 0, 'strength': 0, 'crit chance': 20, 'crit damage': 50, 'attack speed': 100, 'health': 100,
                'defense': 0,
                'speed': 100, 'intelligence': 0}

    def fairy_soul_stats(self):
        hp = 0
        num_souls = self.fairy_souls_collected
        for i, amount in enumerate(fairy_soul_hp_bonus):
            if i * 5 + 5 > num_souls:
                break
            hp += amount
        return {
            'health': hp,
            'defense': num_souls // 5 + num_souls // 25,
            'strength': num_souls // 5 + num_souls // 25,
            'speed': num_souls // 50
        }

    def slayer_stats(self):
        stats = {}
        for rewards, level in zip(list(slayer_rewards.values()), list(self.slayer_levels.values())):
            for i, (reward, amount) in enumerate(rewards):
                if level > i and reward:
                    stats[reward] = stats.get(reward, 0) + amount
        return stats

    def skill_stats(self):
        return {
            'crit chance': self.skills['combat'],
            'strength': self.skills['foraging'] + min(0, self.skills['foraging'] - 15)
        }

    def talisman_stats(self, include_reforges=True):
        stats = {}
        names = [tali.internal_name for tali in self.talismans if tali.active]
        for i in self.talismans:
            if i.active:
                for stat, amount in i.stats(include_reforges).items():
                    stats[stat] = stats.get(stat, 0) + amount
        return stats

    def armor_stats(self, include_reforges=True):
        stats = {}      
        for armor in self.armor:
            for stat, amount in armor.stats().items():
                stats[stat] = stats.get(stat, 0) + amount
        return stats

    def stat_modifiers(self):
        modifers = {}

        def add_modifier(name, mod):
            if name in modifers:
                if name == 'crit damage':
                    modifers[name] = lambda stat, strength: mod(modifers[name](stat, strength))
                else:
                    modifers[name] = lambda stat: mod(modifers[name](stat))
            else:
                modifers[name] = mod

        helmet = next((piece for piece in self.armor if piece.type == 'helmet'), None)
        tarantula_helmet = helmet and helmet.internal_name == 'TARANTULA_HELMET'
        superior = 0
        mastiff = 0
        for i in self.armor:
            if 'SUPERIOR' in i.internal_name:
                superior += 1
            elif 'MASTIFF' in i.internal_name:
                mastiff += 1
            else:
                break
        if superior == 4:
            for name in ['damage', 'strength', 'crit chance', 'attack speed', 'health', 'defense', 'speed',
                         'intelligence']:
                add_modifier(name, lambda stat: stat * 1.05)
            add_modifier('crit damage', lambda stat, strength: stat * 1.05)
        elif mastiff == 4:
            add_modifier('crit damage', lambda stat, strength: stat / 2)
        elif tarantula_helmet:
            add_modifier('crit damage', lambda stat, strength: stat + strength / 10)
        return modifers

    # Method is unfinished, only works for damage stats. feel free to send me a corrected version!
    def stats(self, weapon):
        """Returns a dictionary containing all the player's stats including their weapon's stats."""
        stats = self.base_stats()

        def apply_stats(additional):
            for key, value in additional.items():
                stats[key] += value

        apply_stats(self.fairy_soul_stats())
        apply_stats(self.slayer_stats())
        apply_stats(self.cake_stats())
        apply_stats(self.skill_stats())
        apply_stats(self.talisman_stats(include_reforges=True))

        stats = self.armor_modifiers(stats)

        return stats

    def talisman_counts(self):
        counts = {'common': 0, 'uncommon': 0, 'rare': 0, 'epic': 0, 'legendary': 0}
        for tali in self.talismans:
            if tali.active:
                counts[tali.rarity] += 1
        return counts

    async def auctions(self):
        resp = await self.__call_api__('/skyblock/auction', uuid=self.uuid, profile=self.profile)

        player_auctions = []
        for i in range(len(resp['auctions'])):
            curr_auction = resp['auctions'][i]

        if not curr_auction['claimed']:
            player_auctions.append({
                'item_name': curr_auction['item_name'], 'starting_bid': curr_auction['starting_bid'],
                'highest_bid': curr_auction['highest_bid_amount'],
                'highest_bidder': curr_auction['claimed_bidders'] if len(
                    curr_auction['claimed_bidders']) > 0 else None,
                'end': curr_auction['end']
            })