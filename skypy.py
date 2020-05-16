from exceptions import *
from constants import *

_advancedmode = False
def enable_advanced_mode():
	global _advancedmode
	_advancedmode = True

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
		_session = aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=3), raise_for_status=True)
	return _session

# Inventory parsing
from base64 import b64decode as one
from gzip import decompress as two
from io import BytesIO as three
from struct import unpack
import re
# -----------------

def decode_inventory_data(raw):
	"""Takes a raw string representing inventory data.
	Returns a json object with the inventory's contents"""

	raw = three(two(one(raw)))	# Unzip raw string from the api

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
		while parse_next_tag(payload) != 0:	 # Parse tags until we find an endcap (type == 0)
			pass  # Nothing needs to happen here
		return payload

	payloads = {
		1: lambda: read('c', 1),  # Byte
		2: lambda: read('h', 2),  # Short
		3: lambda: read('i', 4),  # Int
		4: lambda: read('l', 8),  # Long
		5: lambda: read('f', 4),  # Float
		6: lambda: read('d', 8),  # Double
		7: lambda: raw.read(read('i', 4)),	# Byte Array
		8: lambda: read('s', read('h', 2)),	 # String
		9: parse_list,	# List
		10: parse_compound,	 # Compound
		11: lambda: [read('i', 4) for _ in range(read('i', 4))],  # Int Array
		12: lambda: [read('l', 8) for _ in range(read('i', 4))]	 # Long Array
	}

	def parse_next_tag(dictionary, tag_id=None):
		if tag_id is None:	# Are we inside a list?
			tag_id = read('c', 1)
			if tag_id == 0:	 # Is this the end of a compound?
				return 0
			name = read('s', read('h', 2))

		payload = payloads[tag_id]()
		if isinstance(dictionary, dict):
			dictionary[name] = payload
		else:
			dictionary.append(payload)

	raw.read(3)	 # Remove file header (we ingore footer)
	root = {}
	parse_next_tag(root)
	return [Item(x, i) for i, x in enumerate(root['i']) if x]

def level_from_xp_table(xp, table):
	"""Takes a list of xp requirements and a xp value.
	Returns whatever level the thing should be at"""

	for level, requirement in enumerate(table):
		if requirement > xp:
			break
	else:
		level += 1
	return level

class Item:
	def __init__(self, nbt, slot_number):
		self.__nbt__ = nbt

		self.stack_size = self.__nbt__.get('Count', 1)
		self.slot_number = slot_number

		tag = nbt.get('tag', {})
		extras = tag.get('ExtraAttributes', {})

		self.description = tag.get('display', {}).get('Lore', [])
		self.description_clean = [re.sub('§.', '', line) for line in self.description]
		self.description = '\n'.join(self.description)
		self.internal_name = extras.get('id', None)
		self.hot_potatos = extras.get('hot_potato_count', 0)
		self.collection_date = extras.get('timestamp', '') # 'timestamp': '2/16/20 9:24 PM',
		self.runes = extras.get('runes', {}) # 'runes': {'ZOMBIE_SLAYER': 3},
		self.enchantments = extras.get('enchantments', {})
		self.reforge = extras.get('modifier', None)

		if self.description_clean:
			rarity_type = self.description_clean[-1].split()
			self.rarity = rarity_type[0].lower()
			self.type = rarity_type[1].lower() if len(rarity_type) > 1 else None

			if self.internal_name != 'ENCHANTED_BOOK':
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
		for line in self.description_clean:
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
			if results['defense'] - self.hot_potatos * 2 < end_defence[self.internal_name] * 2:
				for k in results.keys():
					results[k] *= 2
			else:
				reforge_multiplier = 2

		if use_reforge is False:
			if self.reforge:
				for stat, amount in reforges[self.reforge][self.rarity_level()].items():
					if stat in results:
						results[stat] -= amount * reforge_multiplier
		return results

def damage(weapon_dmg, strength, crit_dmg, ench_modifier):
	return (5 + weapon_dmg + strength // 5) * (1 + strength / 100) * (1 + crit_dmg / 100) * (1 + ench_modifier / 100)

#class Stats:
#	def __init__(self, dict):
#		self.

async def fetch_uuid_uname(uname_or_uuid, _depth=0):
	s = await session()

	class TryNormal(Exception):
		#A simple exception that lets us exit mcheads
		pass

	try:
		async with s.get(f'https://mc-heads.net/minecraft/profile/{uname_or_uuid}') as r:
			if r.status == 204:
				raise BadNameError(uname_or_uuid, 'Malformed uuid or username')
			json = await r.json(content_type=None)
			if json is None:
				raise TryNormal
			return json['name'], json['id']

	except (asyncio.TimeoutError, TryNormal):
		# if mcheads fails, we try the normal minecraft API
		try:
			async with s.get(f'https://api.mojang.com/users/profiles/minecraft/{uname_or_uuid}') as r:

				json = await r.json(content_type=None)
				if json is None:

					async with s.get(f'https://api.mojang.com/user/profiles/{uname_or_uuid}/names') as r:
						json = await r.json(content_type=None)
						if json is None:
							raise BadNameError(uname_or_uuid, 'Malformed uuid or username') from None

						return json[-1]['name'], uname_or_uuid

				return json['name'], json['id']
		except asyncio.TimeoutError:
			raise ExternalAPIError('Could not connect to https://mc-heads.net') from None
	except aiohttp.client_exceptions.ClientResponseError as e:
		if e.status == 429:
			await asyncio.sleep(15)
			if _depth <= 5:
				return fetch_uuid_uname(uname_or_uuid, _depth + 1)
			else:
				raise ExternalAPIError('You are being ratelimited by https://api.mojang.com') from None
		else:
			raise BadNameError(uname_or_uuid, 'Malformed uuid or username') from None

class Pet:
	@staticmethod
	def from_API(data):
		cls = Pet()

		cls.xp = data.get('exp', 0)
		cls.active = data.get('active', False)
		cls.rarity = data.get('tier', 'COMMON').lower()
		cls.internal_name = data.get('type', 'BEE')
		cls.level = level_from_xp_table(cls.xp, pet_xp[cls.rarity])
		cls.name = pet_stats[cls.internal_name]['name']
		cls.title = f'[Lvl {cls.level}] {cls.name}'
		cls.xp_remaining = pet_xp[cls.rarity][-1] - cls.xp

		return cls

	def __str__(self):
		return self.name

	def __repr__(self):
		return self.name

	def stats(self):
		"""Returns a dictionary of this pet's stats"""
		return {stat: function(self.level) for stat, function in pet_stats[self.internal_name]['stats'].items()}

class ApiInterface:
	def __next_key__(self):
		self.__key_id__ += 1
		if self.__key_id__ == len(self._api_keys):
			self.__key_id__ = 0
		return self._api_keys[self.__key_id__]

	def _check_loads(self, load, raise_on_double):
		if self.__loads__[load] is True:
			if raise_on_double:
				raise LoadError(load, 'You tried to load a module, but it was already loaded!')
			else:
				return True
		self.__loads__[load] = True
		return False

	async def __call_api__(self, api, **kwargs):
		kwargs['key'] = self.__next_key__()
		url = f'https://api.hypixel.net{api}'

		try:
			async with (await session()).get(url, params=kwargs) as data:
				data = await data.json(content_type=None)

				if data['success']:
					return data

				elif data['cause'] == 'Invalid API key!':
					raise APIKeyError(kwargs["key"], f'Invalid API key!')

				else:
					raise ExternalAPIError(data['cause'])

		except asyncio.TimeoutError:
			return await self.__call_api__(api, **kwargs)

		except aiohttp.client_exceptions.ClientResponseError as e:
			if e.code == 429 or e.code == 403:
				await asyncio.sleep(1.5)
				return await self.__call_api__(api, **kwargs)

			elif e.code == 500:
				raise HypixelError(f'Hypixel\'s servers could not complete your request')

			else:
				raise e from None

	async def __new__(cls, keys, *args, **kwargs):
		instance = super().__new__(cls)

		instance.__loads__ = {
			'pets': False,
			'inventories': False,
			'collections': False,
			'skills slayers': False,
			'deaths': False,
			'banking': False,
			'misc': False
		}

		if isinstance(keys, str):
			instance._api_keys = [keys]
		else:
			instance._api_keys = keys

		instance.__key_id__ = 0

		await instance.__init__(*args, **kwargs)
		return instance

class Guild(ApiInterface):
	"""A class representing a Skyblock guild.
	Instantiate with either Guild(api_key, gname=guildname) or Guild(api_key, gid=guildid)
	api_key can either be a single key or a list of keys
	a list is highly recommended for bigger guilds"""

	async def __init__(self, *, gname=None, gid=None, profile_selection=None, profile_selection_threshold=10000):
		if gid:
			self.gid = gid
			self.data = (await self.__call_api__('/guild', id=gid))['guild']
		elif gname:
			self.gid = (await self.__call_api__('/findGuild', byName=gname))['guild']
			if self.gid is None:
				raise BadGuildError(gname, 'Bad guildname')
			self.data = (await self.__call_api__('/guild', id=self.gid))['guild']
		else:
			raise DataError('You need to provide either a guildname or guild id!')

		if self.data is None:
			raise BadGuildError(gname, 'Bad guildname')

		v = self.data
		self.gname = v['name']
		self.created = v['created']
		self.gxp = v.get('exp', 0)
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
		for player in self.data['members']:
			try:
				player = await Player(self._api_keys, uuid=player['uuid'])
				self.players.append(player)
			except NeverPlayedSkyblockError:
				pass

		if profile_selection:
			await asyncio.gather(*[
				player.set_profile_automatically(
					attribute=profile_selection,
					threshold=profile_selection_threshold
				) for player in self
			])
		else:
			await asyncio.gather(*[
				player.set_profile_automatically(
					threshold=profile_selection_threshold
				) for player in self
			])

		if _advancedmode is False:
			for player in self:
				player.load_all()

			self.load_all()

	def load_skills_slayers(self, raise_on_double=True):
		if self._check_loads('skills slayers', raise_on_double):
			return self

		for player in self:
			player.load_skills_slayers(False)

		l = len(self)

		if l == 0:
			self.skill_average = {skill: 0 for skill in skills}
			self.skills = {skill: 0 for skill in skills}
			self.slayers = {slayer: 0 for slayer in slayer}
			self.slayer_xp = {slayer: 0 for slayer in slayer}
		else:
			self.skill_average = sum(player.skill_average for player in self) / l
			self.skills = {
				skill: sum(player.skills[skill] for player in self) / l
				for skill in skills
			}
			self.skill_xp = {
				skill: sum(player.skill_xp[skill] for player in self) / l
				for skill in skills
			}
			self.slayers = {
				slayer: sum(player.slayers[slayer] for player in self) / l
				for slayer in slayers
			}
			self.slayer_xp = {
				slayer: sum(player.slayer_xp[slayer] for player in self) / l
				for slayer in slayers
			}

		return self

	def load_collections(self, raise_on_double=True):
		if self._check_loads('collections', raise_on_double):
			return self

		for player in self:
			player.load_collections(False)

		l = len(self)

		if l == 0:
			self.unique_minions = 0
			self.minion_slots = 0
		else:
			self.unique_minions = sum(player.unique_minions for player in self) / l
			self.minion_slots = sum(player.minion_slots for player in self) / l

		return self

	def load_banking(self, raise_on_double=True):
		if self._check_loads('banking', raise_on_double):
			return self

		for player in self:
			player.load_banking(False)

		l = len(self)

		if l == 0:
			self.bank_balance = 0
			self.purse = 0
		else:
			self.bank_balance = sum(player.bank_balance for player in self) / l
			self.purse = sum(player.purse for player in self) / l

		return self

	def load_deaths(self, raise_on_double=True):
		if self._check_loads('deaths', raise_on_double):
			return self

		for player in self:
			player.load_deaths(False)

		self.kills = sum(player.kills for player in self)
		self.deaths = sum(player.deaths for player in self)

		return self

	def load_all(self, raise_on_double=True):
		return self.load_skills_slayers(raise_on_double).load_collections(raise_on_double).load_banking(raise_on_double).load_deaths(raise_on_double)

	def __iter__(self):
		return iter(self.players)

	def __str__(self):
		return str(self.players)

	def __len__(self):
		return len(self.players)

	def __getitem__(self, index):
		return self.players[index]

class Player(ApiInterface):
	"""A class representing a Skyblock player.
	Instantiate the class with Player(api_key, username) or Player(api_key, uuid)
	Use profiles() and set_profile() to retrieve and define all the profile data.
	Use weapons() and set_weapon() to retrieve and set the player's weapon."""

	async def __init__(self, *, uname=None, uuid=None, guild=False, _profiles=None, _achivements=None):
		if uname and uuid:
			self.uname, self.uuid = await fetch_uuid_uname(uuid)
		elif uname:
			self.uname, self.uuid = await fetch_uuid_uname(uname)
		elif uuid:
			self.uname, self.uuid = await fetch_uuid_uname(uuid)
		else:
			raise DataError('You need to provide either a minecraft username or uuid!')

		if _profiles and _achivements:
			self.profiles = _profiles
			self.achievements = _achivements
		else:
			try:
				self.profiles = {}
				player = await self.__call_api__('/player', uuid=self.uuid)
				profile_ids = player['player']['stats']['SkyBlock']['profiles']

				self.achievements = player['player']['achievements']

				for k, v in profile_ids.items():
					self.profiles[v['cute_name']] = k

			except (KeyError, TypeError):
				raise NeverPlayedSkyblockError(self.uname) from None
			if not self.profiles:
				raise NeverPlayedSkyblockError(self.uname)

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

		self._profile_set = False

	@classmethod
	def from_raw(cls, uname, uuid, data, achievements):
		cls.uname, cls.uuid

		return cls

	def __str__(self):
		return self.uname

	def __repr__(self):
		return self.uname

	def avatar(self, size=None):
		if size:
			return f'https://mc-heads.net/avatar/{self.uuid}/{size}'
		else:
			return f'https://mc-heads.net/avatar/{self.uuid}'

	async def set_profile_automatically(self, attribute=lambda player: player.load_skills_slayers(False).total_slayer_xp, threshold=None):
		"""Sets a player profile automatically
		<attribute> is a function that takes a <Player> class and returns whatever value you want to set it based on
		example: player.set_profile_automatically(lambda player: player.skill_xp['combat'])"""
		best = None
		max = 0

		async def create_canidate(profile):
			player = await Player(
				self._api_keys,
				uname=self.uname,
				uuid=self.uuid,
				_profiles=self.profiles,
				_achivements=self.achievements
			)
			await player.set_profile(profile)
			return player

		profile_ids = list(self.profiles.values())

		if threshold:
			best = profile_ids[0]
			for profile in reversed(profile_ids):
				try:
					canidate = await create_canidate(profile)
				except HypixelError:
					continue

				if attribute(canidate) >= threshold:
					best = profile
					break
		else:
			for canidate in asyncio.as_completed([create_canidate(profile) for profile in profile_ids]):
				try:
					canidate = await canidate
					current = attribute(canidate)
					if best is None or current > max:
						max = current
						best = canidate.profile
				except HypixelError:
					pass

		await self.set_profile(best)

	def load_pets(self, raise_on_double=True):
		"""Loads all of a player's pets into RAM
		Returns the player for efficent function chaining"""

		if self._check_loads('pets', raise_on_double):
			return self

		v = self._api_data['members'][self.uuid]

		self.pets = []
		self.pet = None
		if 'pets' in v:
			for data in v['pets']:
				pet = Pet.from_API(data)
				self.pets.append(pet)
				if pet.active:
					self.pet = pet

		return self

	@staticmethod
	def _parse_inventory(v, *path):
		try:
			result = v
			for key in path:
				result = result[key]
			return decode_inventory_data(result)
		except KeyError:
			return []

	def load_inventories(self, raise_on_double=True):
		"""Loads all of a player's inventories into RAM (inventory, armor, enderchest, quiver, ect)
		Returns the player for efficent function chaining"""
		if self._check_loads('inventories', raise_on_double):
			return self
		v = self._api_data['members'][self.uuid]

		self.inventory = Player._parse_inventory(v, 'inv_contents', 'data')
		self.echest = Player._parse_inventory(v, 'ender_chest_contents', 'data')
		self.armor = Player._parse_inventory(v, 'inv_armor', 'data')
		self.weapons = [item for item in self.inventory + self.echest if item.type in ('sword', 'bow', 'fishing rod')]
		self.candy_bag = Player._parse_inventory(v, 'candy_inventory_contents', 'data')
		self.talisman_bag = Player._parse_inventory(v, 'talisman_bag', 'data')
		self.potion_bag = Player._parse_inventory(v, 'potion_bag', 'data')
		self.fish_bag = Player._parse_inventory(v, 'fishing_bag', 'data')
		self.quiver = Player._parse_inventory(v, 'quiver', 'data')

		if self.inventory or self.echest or self.talisman_bag:
			self.enabled_api['inventory'] = True

		self.talismans = [talisman for talisman in self.inventory + self.talisman_bag if talisman.type == 'accessory']

		for talisman in self.talismans:
			talisman.active = True

			# Check for duplicate talismans
			if self.talismans.count(talisman) > 1:
				talisman.active = False
				continue

			# Check for talisman families
			if talisman.internal_name in tiered_talismans:
				for other in tiered_talismans[talisman.internal_name]:
					if other in self.talismans:
						talisman.active = False
						break

		return self

	@staticmethod
	def _parse_collection(v, data):
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

	def load_collections(self, raise_on_double=True):
		"""Loads a player's minion slots and collections into RAM
		Returns the player for efficent function chaining"""

		if self._check_loads('collections', raise_on_double):
			return self
		v = self._api_data['members'][self.uuid]

		try:
			self.collections = {name.lower().replace('_', ' '): level for name, level in v['collection'].items()}
			self.enabled_api['collection'] = True

		except KeyError:
			self.collections = {}

		self.unlocked_collections = Player._parse_collection(v, 'unlocked_coll_tiers')
		self.minions = Player._parse_collection(v, 'crafted_generators')

		self.unique_minions = max(
			self.achievements.get('skyblock_minion_lover', 0),
			sum(self.minions.values())
		)

		self.minion_slots = level_from_xp_table(self.unique_minions, minion_slot_requirements)

		return self

	def load_skills_slayers(self, raise_on_double=True):
		"""Loads a player's skill and slayer data into RAM
		Returns the player for efficent function chaining"""

		if self._check_loads('skills slayers', raise_on_double):
			return self
		v = self._api_data['members'][self.uuid]

		if 'experience_skill_farming' in v:
			self.enabled_api['skills'] = True

			self.skill_xp = {}
			self.skills = {}

			for skill in skills:
				xp = int(v.get(f'experience_skill_{skill}', 0))
				self.skill_xp[skill] = xp
				self.skills[skill] = level_from_xp_table(
					xp,
					runecrafting_xp_requirements if skill == 'runecrafting' else skill_xp_requirements
				)
		else:
			self.enabled_api['skills'] = False

			self.skill_xp = {
				'carpentry': 0,
				'runecrafting': 0
			}
			self.skills = {
				'carpentry': 0,
				'runecrafting': 0
			}

			for skill, achievement in [
					('farming', 'skyblock_harvester'),
					('mining', 'skyblock_excavator'),
					('foraging', 'skyblock_gatherer'),
					('combat', 'skyblock_combat'),
					('enchanting', 'skyblock_augmentation'),
					('alchemy', 'skyblock_concoctor'),
					('fishing', 'skyblock_angler'),
					('taming', 'no achievement')
				]:

				level = self.achievements.get(achievement, 0)
				self.skills[skill] = level
				self.skill_xp[skill] = 0 if level == 0 else skill_xp_requirements[level - 1]

		self.skill_average = sum(self.skills[skill] for skill in skills if skill not in cosmetic_skills) / (len(skills) - len(cosmetic_skills))

		self.slayer_xp = {}
		self.slayers = {}
		for slayer in slayers:
			xp = v.get('slayer_bosses', {}).get(slayer, {}).get('xp', 0)
			self.slayer_xp[slayer] = xp
			self.slayers[slayer] = level_from_xp_table(xp, slayer_level_requirements[slayer])

		self.total_slayer_xp = sum(self.slayer_xp.values())

		return self

	def load_deaths(self, raise_on_double=True):
		"""Loads a player's kills and deaths into RAM
		Returns the player for efficent function chaining"""

		if self._check_loads('deaths', raise_on_double):
			return self
		v = self._api_data['members'][self.uuid]

		self.kills = int(v.get('stats', {'kills': 0}).get('kills', 0))
		self.specifc_kills = {name.replace('kills_', '').replace('_', ' '): int(amount)
							  for name, amount in v['stats'].items() if re.match('kills_', name)}
		self.deaths = int(v.get('stats', {'deaths': 0}).get('deaths', 0))
		self.specifc_deaths = {name.replace('deaths_', '').replace('_', ' '): int(amount)
							   for name, amount in v['stats'].items() if re.match('deaths_', name)}

		return self

	def load_banking(self, raise_on_double=True):
		"""Loads a player's bank balance and purse into RAM
		Returns the player for efficent function chaining"""

		if self._check_loads('banking', raise_on_double):
			return self

		if 'banking' in self._api_data:
			self.enabled_api['banking'] = True
			self.bank_balance = float(self._api_data['banking'].get('balance', 0))
		else:
			self.bank_balance = 0

		self.purse = float(self._api_data['members'][self.uuid].get('coin_purse', 0))

		return self

	def load_misc(self, raise_on_double=True):
		"""Loads a player's misc stats into RAM
		Returns the player for efficent function chaining"""

		if self._check_loads('misc', raise_on_double):
			return self
		v = self._api_data['members'][self.uuid]

		self.join_date = datetime.fromtimestamp(v.get('first_join', 0) / 1000.0)
		self.fairy_souls_collected = v.get('fairy_souls_collected', 0)

		return self

	def load_all(self, raise_on_double=True):
		"""Loads the entire player API output into RAM
		Called automatically if you have not used skypy.enable_advanced_mode()
		Returns the player for efficent function chaining"""

		return self.load_pets(raise_on_double).load_inventories(raise_on_double).load_collections(raise_on_double).load_skills_slayers(raise_on_double).load_deaths(raise_on_double).load_banking(raise_on_double).load_misc(raise_on_double)

	async def set_profile(self, profile):
		"""Sets a player's profile based on the provided profile ID"""
		global _advancedmode

		if self._profile_set == True:
			raise DataError('This player already has their profile set!')
		self._profile_set = True

		self.profile = profile
		for cute_name, id in self.profiles.items():
			if id == profile:
				self.profile_name = cute_name
				break
		else:
			raise DataError('Bad profile ID!')

		self._api_data = (await self.__call_api__('/skyblock/profile', profile=self.profile))['profile']
		self.enabled_api = {'skills': False, 'collection': False, 'inventory': False, 'banking': False}

		if _advancedmode is False:
			self.load_all()

	async def is_online(self):
		player_data = (await self.__call_api__('/player', name=self.uname))['player']
		return player_data['lastLogout'] < player_data['lastLogin']

	def base_stats(self):
		return base_stats

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
		for rewards, level in zip(list(slayer_rewards.values()), list(self.slayers.values())):
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
		r = await self.__call_api__('/skyblock/auction', uuid=self.uuid, profile=self.profile)

		return [
			{
				'item': decode_inventory_data(auction['item_bytes']['data'])[0],
				'start': auction['start'],
				'end': auction['end'],
				'starting_bid': auction['starting_bid'],
				'highest_bid': auction['highest_bid_amount'],
				'bids': auction['bids'],
				'buyer': auction['bids'][-1]['bidder'] if auction['bids'] else None
			}
			for auction in r['auctions']
			if auction['claimed'] is False
		]
