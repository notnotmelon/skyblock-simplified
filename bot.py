import os
import discord
import skypy
import skypy_constants
import asyncio
import math
import traceback
import motor.motor_asyncio
import itertools
import re
import random
from statistics import mean, median, mode, pstdev, StatisticsError
from datetime import datetime, timezone, timedelta
from bs4 import BeautifulSoup
import cloudscraper
from aiohttp import ClientError
import traceback

TIME_FORMAT = '%m/%d %I:%M %p UTC'

if os.environ.get('API_KEY') is None:
    import dotenv

    dotenv.load_dotenv()
keys = os.getenv('API_KEY').split()

def time_until(goal):
    now = datetime.now(timezone.utc)
    then = datetime.fromtimestamp(goal, timezone.utc)
    delta = then - now
    
    d, h, m, s = delta.days, delta // timedelta(hours=1), delta // timedelta(minutes=1), delta.seconds
        
    if d:
        return f'{d} days, {h} hours'
    
    if h:
        return f'{h} hours'
        
    return f'0:{m:02}:{s:02}'

DAMAGING_POTIONS = {
    'critical': {
        'stats': {
            'crit chance': [0, 10, 15, 20, 25],
            'crit damage': [0, 10, 20, 30, 40]
        },
        'levels': [0, 3, 4]
    },
    'strength': {
        'stats': {'strength': [0, 5.25, 13.125, 21, 31.5, 42, 52.5, 63, 78.75]},  # Assume cola
        'levels': [0, 5, 7, 8]
    },
    'spirit': {
        'stats': {'crit damage': [0, 10, 20, 30, 40]},
        'levels': [0, 3, 4]
    },
    'archery': {
        'stats': {'enchantment modifier': [0, 17.5, 30, 55, 80]},
        'levels': [0, 3, 4]
    }
}

ORBS = {
    'weird tuba': {
        'internal': 'WEIRD_TUBA',
        'stats': {'strength': 30}
    },
    'mana flux': {
        'internal': 'MANA_FLUX_POWER_ORB',
        'stats': {'strength': 10}
    },
    'overflux': {
        'internal': 'OVERFLUX_POWER_ORB',
        'stats': {'strength': 25}
    }
}

LEADERBOARDS = {
    'Skill Average': (
        '📈', lambda player: player.skill_average, None, lambda guild: guild.stat_average('skill_average'), None),
    'Minion Slots': ('⛓', lambda player: player.unique_minions, lambda player: player.minion_slots,
                     lambda guild: guild.stat_average('unique_minions'),
                     lambda guild: guild.stat_average('minion_slots')),
    'Farming': ('🌾', lambda player: player.skill_experience['farming'], lambda player: player.skills['farming'],
                lambda guild: guild.stat_average('skill_experience')['farming'],
                lambda guild: guild.stat_average('skills')['farming']),
    'Mining': ('⛏', lambda player: player.skill_experience['mining'], lambda player: player.skills['mining'],
               lambda guild: guild.stat_average('skill_experience')['mining'],
               lambda guild: guild.stat_average('skills')['mining']),
    'Combat': ('⚔', lambda player: player.skill_experience['combat'], lambda player: player.skills['combat'],
               lambda guild: guild.stat_average('skill_experience')['combat'],
               lambda guild: guild.stat_average('skills')['combat']),
    'Foraging': ('🪓', lambda player: player.skill_experience['foraging'], lambda player: player.skills['foraging'],
                 lambda guild: guild.stat_average('skill_experience')['foraging'],
                 lambda guild: guild.stat_average('skills')['foraging']),
    'Enchanting': (
        '📖', lambda player: player.skill_experience['enchanting'], lambda player: player.skills['enchanting'],
        lambda guild: guild.stat_average('skill_experience')['enchanting'],
        lambda guild: guild.stat_average('skills')['enchanting']),
    'Alchemy': ('⚗', lambda player: player.skill_experience['alchemy'], lambda player: player.skills['alchemy'],
                lambda guild: guild.stat_average('skill_experience')['alchemy'],
                lambda guild: guild.stat_average('skills')['alchemy']),
    'Fishing': ('🎣', lambda player: player.skill_experience['fishing'], lambda player: player.skills['fishing'],
                lambda guild: guild.stat_average('skill_experience')['carpentry'],
                lambda guild: guild.stat_average('skills')['carpentry']),
    'Carpentry': ('🪑', lambda player: player.skill_experience['carpentry'], lambda player: player.skills['carpentry'],
                  lambda guild: guild.stat_average('skill_experience')['farming'],
                  lambda guild: guild.stat_average('skills')['farming']),
    'Runecrafting': (
        '⚜️', lambda player: player.skill_experience['runecrafting'], lambda player: player.skills['runecrafting'],
        lambda guild: guild.stat_average('skill_experience')['runecrafting'],
        lambda guild: guild.stat_average('skills')['runecrafting']),
    'Zombie': ('🧟', lambda player: player.slayer_exp['zombie'], lambda player: player.slayer_levels['zombie'],
               lambda guild: guild.stat_average('slayer_exp')['zombie'],
               lambda guild: guild.stat_average('slayer_levels')['zombie']),
    'Spider': ('🕸️', lambda player: player.slayer_exp['spider'], lambda player: player.slayer_levels['spider'],
               lambda guild: guild.stat_average('slayer_exp')['spider'],
               lambda guild: guild.stat_average('slayer_levels')['spider']),
    'Wolf': ('🐺', lambda player: player.slayer_exp['wolf'], lambda player: player.slayer_levels['wolf'],
             lambda guild: guild.stat_average('slayer_exp')['wolf'],
             lambda guild: guild.stat_average('slayer_levels')['wolf'])
}

LEVELS = {
    name: LEADERBOARDS[name] for name in
    ['Farming', 'Mining', 'Combat', 'Foraging', 'Enchanting', 'Alchemy', 'Fishing', 'Carpentry', 'Runecrafting',
     'Zombie', 'Spider', 'Wolf']
}

RANKS = [
    ['CAROLINA REAPER', 'GHOST PEPPER', 'HABAÑERO', 'JALAPEÑO', 'SWEET BANANA', 'BELL PEPPER'],
    ['WIZARD', 'KING', 'QUEEN', 'LORD', 'JESTER', 'PEASANT'],
    ['PRESIDENT', 'GENERAL', 'MAJOR', 'SERGEANT', 'CORPORAL', 'PRIVATE'],
    ['S', 'A', 'B', 'C', 'D', 'F'],
    ['MVP++', 'MVP+', 'MVP', 'VIP+', 'VIP', 'NON'],
    ['DRAGON', 'DINOSAUR', 'GILA', 'TURTLE', 'SNAKE', 'GECKO'],
    ['LEGENDARY', 'EPIC', 'RARE', 'UNCOMMON', 'COMMON', '" " " "SPECIAL" " " "'],
    ['GOD', 'PRO', 'ADVANCED', 'VIABLE', 'AVERAGE', 'NOOB'],
    ['PC', 'NINTENDO', 'PLAY STATION', 'XBOX', 'VR', 'MOBILE']
]

# List of players that bug abused skills or severely macroed for stats
EXPLOITERS = {
    '6c80f48d85544035bb31e6cb9f40b948': ('farming', 'enchanting'),
    '04e0ad3f4b7f4815bb39c3888249115c': ('farming',),
    '6ac668e787e74561b86bae8c496d0f97': ('farming',),
    '02bd483c511b4e1fbd0f0c071e2d0411': ('farming',),
    'e91e2680d7da4bc4adbb30c04366f6fa': ('farming',),
    'd14403fd77664905929ee1a6e365e623': ('enchanting',),
    '8f0d1d399aee48f59d5af5f0f69e4eee': ('enchanting',),
    '720d2a83efe446969bc29fbc8c98b31e': ('enchanting',),
    'f33f51a796914076abdaf66e3d047a71': ('enchanting',),
    '73464a378313409d8232076f44074bcf': ('enchanting',),
    '7b488582998f405a84c19ad7a4e9b2e7': ('enchanting',),
    '6170dede383a42a99db6166ca46a8469': ('combat',),    
    '6c5b615c2c47428aad137249d37c6fcc': ('farming',),   
    '44d03c6e2cba41799ad5c9d2f837d03d': ('farming',),   
    '446dea472dd0494b89260421b9981d15': ('combat',)    
}

# list of all enchantment powers per level. can be a function or a number
ENCHANTMENT_VALUES = {
    # sword always
    'sharpness': 5,
    'giant_killer': lambda level: 25 if level > 0 else 0,
    # sword sometimes
    'smite': 8,
    'bane_of_arthropods': 8,
    'first_strike': 25,
    'ender_slayer': 12,
    'cubism': 10,
    'execute': 10,
    'impaling': 12.5,
    # bow always
    'power': 8,
    # bow sometimes
    'dragon_hunter': 8,
    'snipe': 5,  # Would be lower except I only use this for drags and magma bosses
    # rod always
    'spiked_hook': 5
}

MAX_BOOK_LEVELS = {
    'sharpness': 6,
    'giant_killer': 6,
    'smite': 6,
    'bane_of_arthropods': 6,
    'first_strike': 4,
    'ender_slayer': 6,
    'cubism': 5,
    'execute': 5,
    'impaling': 3,
    'power': 6,
    'dragon_hunter': 5,
    'snipe': 3,
    'spiked_hook': 6
}

CHEAP_MAX_BOOK_LEVELS = {
    'sharpness': 5,
    'giant_killer': 5,
    'smite': 5,
    'bane_of_arthropods': 5,
    'first_strike': 4,
    'ender_slayer': 5,
    'cubism': 5,
    'execute': 5,
    'impaling': 3,
    'power': 5,
    'dragon_hunter': 3,
    'snipe': 3,
    'spiked_hook': 5
}

# list of relevant enchants for common mobs
ACTIVITIES = {
    'slayer bosses': [
        'giant_killer',
        'sharpness',
        'power',
        'spiked_hook',
        'smite',
        'bane_of_arthropods',
        'execute'
    ],
    'dragons': [
        'giant_killer',
        'sharpness',
        'power',
        'spiked_hook',
        'ender_slayer',
        'execute',
        'dragon_hunter',
        'snipe'
    ],
    'zealots': [
        'giant_killer',
        'sharpness',
        'power',
        'spiked_hook',
        'ender_slayer',
        'first_strike'
    ],
    'sea creatures': [
        'giant_killer',
        'sharpness',
        'power',
        'spiked_hook',
        'first_strike',
        'impaling'
    ],
    'players': [
        'giant_killer',
        'sharpness',
        'power',
        'spiked_hook',
        'execute',
        'snipe'
    ],
    'magma boss': [
        'giant_killer',
        'sharpness',
        'power',
        'spiked_hook',
        'cubism',
        'execute',
        'snipe'
    ],
    'horseman': [
        'giant_killer',
        'sharpness',
        'power',
        'spiked_hook',
        'execute',
        'snipe'
    ],
    'other': [
        'giant_killer',
        'sharpness',
        'power',
        'spiked_hook',
        'smite',
        'bane_of_arthropods',
        'first_strike'
    ]
}

RELEVANT_REFORGES = {
    'forceful': (None, None, (7, 0, 0), None, None),
    'itchy': ((1, 0, 3), (2, 0, 5), (2, 0, 8), (3, 0, 12), (5, 0, 15)),
    'strong': (None, None, (4, 0, 4), (7, 0, 7), (10, 0, 10)),
    'godly': ((1, 1, 1), (2, 2, 2), (4, 2, 3), (7, 3, 6), (10, 5, 8))
}
reforges_list = list(RELEVANT_REFORGES.values())

CLOSE_MESSAGE = '\n> _use **exit** to close the session_'

PET_EMOJIS = {
    'SKELETON_HORSE': '💀',
    'SNOWMAN': '⛄',
    'BAT': '🦇',
    'SHEEP': '🐑',
    'CHICKEN': '🐔',
    'WITHER_SKELETON': '🏴‍☠️',
    'SILVERFISH': '🗿',
    'RABBIT': '🐇',
    'HORSE': '🐴',
    'PIGMAN': '🐽',
    'WOLF': '🐺',
    'OCELOT': '🐱',
    'LION': '🦁',
    'ENDER_DRAGON': '🐲',
    'GUARDIAN': '🛡️',
    'ENDERMAN': '😈',
    'BLUE_WHALE': '🐳',
    'GIRAFFE': '🦒',
    'PHOENIX': '🐦',
    'BEE': '🐝',
    'MAGMA_CUBE': '🌋',
    'FLYING_FISH': '🐟',
    'SQUID': '🦑',
    'PARROT': '🦜',
    'TIGER': '🐯',
    'TURTLE': '🐢',
    'SPIDER': '🕷',
    'BLAZE': '🔥',
    'JERRY': '🤡'
}

class Embed(discord.Embed):
    nbst = '\u200b'

    def __init__(self, channel, *, title, **kwargs):
        self.channel = channel

        if 'description' in kwargs:
            kwargs['description'] = kwargs['description'] or self.nbst

        super().__init__(title=title or self.nbst, color=self.color(channel), **kwargs)

    @staticmethod
    def color(channel):
        default = 0xbf2158

        if hasattr(channel, 'guild'):
            color = channel.guild.me.color
            return discord.Color(default) if color == 0x000000 else color
        else:
            return discord.Color(default)

    def add_field(self, *, name, value, inline=True):
        return super().add_field(name=f'**{name}**' if name else self.nbst, value=value or self.nbst, inline=inline)

    async def send(self):
        return await self.channel.send(embed=self)

WHITE = ('', '')   
GRAY = ('brainfuck', '')
GREY = GRAY
PUKE = ('css', '')
GREEN = ('yaml', '')
BLUE = ('md', '#')
YELLOW = ('fix', '')
ORANGE = ('glsl', '#')
RED = ('diff', '-')
RARITY_COLORS = {'common': GREY, 'uncommon': GREEN, 'rare': BLUE, 'epic': RED, 'legendary': YELLOW}

def colorize(s, color):
    language, point = color
    s = str(s)
    
    if s:
        return f'```{language}\n{point}' + s.replace('\n', f'\n{point}') + '\n```'
    else:
        return ''

class Route:
    def __init__(self, talismans, rarity):
        self.strength, self.crit_chance, self.crit_damage = [
            sum(reforges_list[y][rarity][x] * talismans[y]
                for y in range(len(reforges_list)) if reforges_list[y][rarity])
            for x in range(3)
        ]
        self.counts = talismans
        self.rarity = rarity
        self.rarity_str = ["common", "uncommon", "rare", "epic", "legendary"][self.rarity]

    def __str__(self):
        return ' ߸ '.join(f'{c} '
                          f'{"godly/zealous" if self.rarity < 2 and name == "godly" else name} '
                          f'{Route.rarity_grammar(self.rarity_str, c)}'
                          for name, c in zip(RELEVANT_REFORGES.keys(), self.counts) if c != 0)

    @staticmethod
    def routes(count, size, rarity):
        def helper(count, idx, current):
            if count == 0:
                yield Route(current, rarity)
            elif idx == size - 1:
                new = current.copy()
                new[idx] += count
                yield Route(new, rarity)
            else:
                if reforges_list[idx][rarity]:
                    new = current.copy()
                    new[idx] += 1
                    for x in helper(count - 1, idx, new):
                        yield x
                for x in helper(count, idx + 1, current):
                    yield x

        return helper(count, 0, [0] * size)

    @staticmethod
    def rarity_grammar(rarity, count=0):
        if count == 1:
            return rarity
        return f'{rarity[:-1]}ies' if rarity[-1] == 'y' else f'{rarity}s'


def chunks(lst, n):
        lst = list(lst)
        """Yield successive n-sized chunks from lst."""
        for i in range(0, len(lst), n):
            yield lst[i:i + n]

'''
'skill events': {
                'emoji': '😎',
                'desc': 'Useful for guilds. Records the amount of skill experience gained by each player in a week. Raise your averages!',
                'commands': {
                    'start event': {
                        'security': 1,
                        'function': self.start_event,
                        'desc': 'Starts a skyblock event',
                        'session': True
                    },
                    'view leaderboard': {
                        'function': self.view_lb,
                        'desc': 'Displays the leaderboard for the current event'
                    },
                    'end event': {
                        'security': 1,
                        'function': self.end_event,
                        'desc': 'Ends the current event and displays the winners'
                    }
                }
            },
'''

class Bot(discord.Client):
    def __init__(self, *args, **kwargs):
        self.callables = {}
        self.commands = {
            'bot': {
                'emoji': '🤖',
                'desc': 'View bot stats, visit the support server, and other status commands',
                'commands': {
                    'stats': {
                        'function': self.stats,
                        'desc': 'Displays stats about the bot including number of servers and users'
                    },
                    'help': {
                        'function': self.help,
                        'desc': 'Opens the menu that you are looking at now'
                    },
                    'support': {
                        'function': self.support_server,
                        'desc': 'Have an question about the bot? Use this command'
                    }
                }
            },
            'internet': {
                'emoji': '🌐',
                'desc': 'Surf the world wide web! Check the forums, manage guild applications, view the skyblock wiki, and more',
                'commands': {
                    'news': {
                        'function': self.view_trending,
                        'desc': f'Displays the top three Skyblock threads from the past {trending_timeout} hours'
                    }
                }
            },
            'damage': {
                'emoji': '💪',
                'desc': 'A collection of tools designed to optimize your damage and talismans',
                'commands': {
                    'optimizer': {
                        'function': self.optimize_talismans,
                        'desc': 'Optimizes your talismans to their best reforges',
                        'session': True
                    },
                    'missing': {
                        'args': '[username] (profile)',
                        'function': self.view_missing_talismans,
                        'desc': 'Displays a list of your missing talismans. Also displays inactive/unnecessary talismans if you have them'
                    },
                    'damage': {
                        'function': self.calculate_damage,
                        'desc': 'Calcuates damage based on hypothetical stat values. This is not the talisman optimizer',
                        'session': True
                    }
                }
            },
            'spy': {
                'emoji': '🕵️‍♂️',
                'desc': 'View stats and leaderboards for both guilds and players. Most functions work without API settings enabled',
                'commands': {
                    'player': {
                        'args': '[username] (profile)',
                        'function': self.player,
                        'desc': 'Displays a player\'s guild, skills, and slayer levels'
                    },
                    'guild': {
                        'args': '[name]',
                        'function': self.guild,
                        'desc': 'Displays skill averages for a guild, aswell as leaderboards for all their players'
                    },
                    'royalty': {
                        'function': self.royalty,
                        'desc': 'Shows the top 30 guilds and players for every skill and slayer'
                    },
                    'pets': {
                        'args': '[username] (profile)',
                        'function': self.pets,
                        'desc': 'Shows all of a player\'s pets and their pet levels'
                    }
                }
            },
            'auctions': {
                'emoji': '💸',
                'desc': 'View average prices for items aswell as past auctions for any player. Powered by https://hypixel-skyblock.com',
                'commands': {
                    'price': {
                        'args': '[itemname] (stacksize)',
                        'function': self.price,
                        'desc': 'Displays the average price for any item'
                    },
                    'buys': {
                        'args': '[username]',
                        'function': self.buys,
                        'desc': 'Displays all past purchases for any player'
                    },
                    'sells': {
                        'args': '[username]',
                        'function': self.sells,
                        'desc': 'Displays all past purchases for any player'
                    },
                    'current': {
                        'args': '[username]',
                        'function': self.current_auctions,
                        'desc': 'Displays all current auctions'
                    }
                }
            }
        }
        self.hot_channels = {}
        self.ready = False
        self.args_message = '`[] signifies a required argument, while () signifies an optional argument`'

        super().__init__(*args, **kwargs)

    async def log(self, *args):
        print(*args, sep='')

    async def on_error(self, *args, **kwargs):
        error = traceback.format_exc().replace('```', '"""')
        await self.get_user(270352691924959243).send(f'```python\n{error}```')
        print(error)

    async def on_ready(self):
        await self.log(f'Logged on as {self.user}!')

        for data in self.commands.values():
            self.callables.update(data['commands'])

        await self.change_presence(activity=discord.Game('| 🍤 sbs help'))

        self.ready = True

    async def on_message(self, message):
        if self.ready is False:
            return

        user = message.author

        if user.bot:
            return

        channel = message.channel
        dm = channel == user.dm_channel

        if channel in self.hot_channels and self.hot_channels[channel] == user:
            return

        command = message.content.replace('!', '', 1)

        if command == self.user.mention:
            await self.help(message)
            return

        command = re.split('\s+', command)
        command[0] = command[0].lower()
        if command[0] == self.user.mention or command[0].lower() == 'sbs':
            command = command[1:]
        elif not dm:
            return

        if not command:
            return

        name = command[0].lower()
        args = command[1:]

        if name not in self.callables:
            return

        '''
        whitelisted_servers = [int(server) for server in os.getenv('SERVERS').split()]
        if not dm and not channel.guild.id in whitelisted_servers and len(channel.guild.members) > 50:
            await Embed(
                channel,
                title='Donate 20$ to my PayPal to use Skyblock Simplified on this server',
                description='https://www.paypal.com/pools/c/8mstSPhQNO'
            ).set_footer(
                text='Free for servers under 50 members'
            ).send()
            await self.log('Paywal enforced in server {guild.name}')
            return
        '''
        
        data = self.callables[name]
        security = data['security'] if 'security' in data else 0
        session = 'session' in data and data['session']
        function = data['function']

        if session and channel in self.hot_channels:
            await channel.send(
                f'{user.mention} someone else is currently using me in this channel! Try sending me a dm with your command instead')
            return

        if security == 1 and not channel.permissions_for(user).administrator:
            await channel.send(
                f'{user.mention} you do not have permission to use this command here! Try using it on your own discord server')
            return

        await self.log(f'{user.name} used {name} {args} in {"a DM" if dm else channel.guild.name}')
        if session:
            self.hot_channels[channel] = user

            try:
                await function(message, *args)
            except discord.errors.Forbidden:
                await channel.send(f'{user.mention} your DM\'s are disabled')

            self.hot_channels.pop(channel)
        else:
            await function(message, *args)

    async def no_args(self, command, user, channel):
        data = self.callables[command]
        usage = f'sbs {command} {data["args"]}' if 'args' in data else command

        await Embed(
            channel,
            title='This command requires arguments!',
            description=f'Correct usage is `{usage}`\n{self.args_message}'
        ).send()

    async def current_auctions(self, message, *args):
        user = message.author
        channel = message.channel
        
        if not args:
            await self.no_args('current', user, channel)
            return

        name = args[0]
        try:
            _, uuid = await skypy.fetch_uuid_uname(name)
        except skypy.BadNameError:
            await channel.send(f'{user.mention} invalid username!')
            return
        except skypy.ExternalAPIError as e:
            await channel.send(f'{user.mention} {e.reason}')
            return
        
        query = 'query Auctions($seller: String) { auctions(seller: $seller) { auction { id highestBidAmount startingBid itemName itemBytes bids { amount bidder timestamp } itemData { name lore id quantity tag } end }}}'
        r = await craftlink(user, channel, query, operation='Auctions', seller=uuid)
        if r is None:
            return
        r = r['auctions']['auction']
                
        embed = Embed(
            channel,
            title=f'Current Auctions From {name}',
            description=f'Powered by https://hypixel-skyblock.com'
        )

        if r:
            for auction in r:
                item = auction['itemData']
                
                if auction['bids']:
                    try:
                        buyer, _ = await skypy.fetch_uuid_uname(auction['bids'][0]['bidder'])
                    except skypy.ExternalAPIError as e:
                        buyer = f'{user.mention} {e.reason}'
                        
                    embed.add_field(
                        name=f'{item["quantity"]}x {item["name"].upper()}',
                        value=f'```diff\n! {int(auction["highestBidAmount"]):,} coins\n'
                              f'-bidder: {buyer}\n'
                              f'ends in {time_until(int(auction["end"]) // 1000)}```'
                    )
                else:
                    embed.add_field(
                        name=f'{item["quantity"]}x {item["name"].upper()}',
                        value=f'```diff\n! {int(auction["startingBid"]):,} coins\n'
                              f'❌ -this auction has no bids!'
                              f'ends in {time_until(int(auction["end"]) // 1000)}```'
                    )
        else:
            embed.add_field(name=None, value='```❌ no auctions found```')
            
        await embed.send()

    async def royalty(self, message, *args):
        global db
        lb = db.leaderboards
    
        user = message.author
        channel = message.channel

        menu = {emoji: name for name, (emoji, _, _, _, _) in LEADERBOARDS.items()}

        current = 'Skill Average'
        while True:
            emoji, function, optional_function, _, _ = LEADERBOARDS[current]
        
            embed = Embed(
                channel,
                title=f'{current} Leaderboard',
                description=None
            )

            players = []
            
            cursor = lb.find().sort(current, -1).limit(50)
            
            i = 0
            if optional_function:
                for d in await cursor.to_list(length=None):
                    players.append(f'#{str(i + 1).ljust(2)} {d["name"]} [{d[current + "_"]:.3f}] [{d[current]:,.3f}]')
                    i += 1
            else:
                for d in await cursor.to_list(length=None):
                    players.append(f'#{str(i + 1).ljust(2)} {d["name"]} [{d[current]:,.3f}]')
                    i += 1

            portion = len(players) / 30
            sections = [0, 1, 4, 9, 15, 22, 30]
            peppers = random.choice(RANKS)
            meal = {}
            for i, pepper in enumerate(peppers):
                meal[pepper] = players[round(sections[i] * portion): round(sections[i + 1] * portion)]

            for pepper, players in meal.items():
                embed.add_field(
                    name=pepper,
                    value=('```css\n' + '\n'.join(players) + '```') if players else r'```¯\_(ツ)_/¯```',
                    inline=False
                )
        
            msg = await embed.send()
            current = await self.reaction_menu(msg, user, menu)
            if current is None:
                break
            await msg.delete()

    async def price(self, message, *args):
        user = message.author
        channel = message.channel

        if not args:
            await self.no_args('price', user, channel)
            return

        if len(args) > 1 and args[-1].isdigit():
            stacksize = int(args[-1])
            itemname = ' '.join(args[:-1]).title()
        else:
            stacksize = None
            itemname = ' '.join(args).title()

        query = 'query ItemsList($page: Int, $items: Int, $name: String) { itemList(page: $page, items: $items, name: $name) { page item { name }}}'
        r = await craftlink(user, channel, query, operation='ItemsList', name=itemname, items=1, page=1)
        if r is None:
            return
        r = r['itemList']['item']

        if not r:
            await channel.send(f'{user.mention} invalid itemname')
            return

        itemname = r[0]['name']

        query = 'query Item($name: String) { item(name: $name) { sales { end price } recent { id seller itemData { quantity lore } bids { bidder timestamp amount } highestBidAmount end } }}'
        r = await craftlink(user, channel, query, operation='Item', name=itemname)
        if r is None:
            return
        r = r['item']
        sales = r['sales']

        if stacksize is None:
            if r['recent']:
                stacksize = 64 if max([int(auction['itemData']['quantity']) for auction in r['recent']]) > 32 else 1
            else:
                stacksize = 1

        auctions = [float(item['price']) * stacksize for item in sales]

        size = len(auctions)
        avg = mean(auctions)
        std = pstdev(auctions, mu=avg)
        small = min(auctions)
        big = max(auctions)

        cutoff = std * 1.5
        lower, upper = avg - cutoff, avg + cutoff
        auctions = [a for a in auctions if lower < a < upper]

        try:
            avg = mean(auctions)
            mid = median(auctions)
            common = mode(auctions)
            std = pstdev(auctions, mu=avg)
            cutoff = std * 1.5
            steals = [a for a in auctions if a < avg - cutoff]
        except StatisticsError:
            await channel.send(f'{user.mention} there haven\'t been any `{itemname}` sold recently')
            return

        await Embed(
            channel,
            title=f'{itemname} (x{stacksize})',
            description='Powered by https://hypixel-skyblock.com'
        ).add_field(
            name=None,
            value=f'```Average: {avg:,.0f}\nMedian: {mid:,.0f}\nMode: {common:,.0f}\nStandard Deviation: {std:,.0f}\nMin: {math.ceil(small):,}\nMax: {math.ceil(big):,}```'
                  f'```There were {len(steals)} steals and {size} total sales```'
        ).set_footer(
            text='Statistics are from the last 1500 items sold\nPrices are ignored unless they are within 1.5 standard deviations'
        ).send()

    async def sells(self, message, *args):
        page_size = 12

        user = message.author
        channel = message.channel

        if not args:
            await self.no_args('sells', user, channel)
            return

        name = args[0]
        try:
            _, uuid = await skypy.fetch_uuid_uname(name)
        except skypy.BadNameError:
            await channel.send(f'{user.mention} invalid username!')
            return
        except skypy.ExternalAPIError as e:
            await channel.send(f'{user.mention} {e.reason}')
            return

        async def pages(page_num):
            query = 'query UserHistory($id: String, $type: String, $limit: Int, $skip: Int) { userHistory(id: $id, type: $type, limit: $limit, skip: $skip) { auctions { id seller itemData { texture id name tag quantity lore __typename } bids { bidder timestamp amount __typename } highestBidAmount end __typename } __typename } }'
            r = await craftlink(user, channel, query, operation='UserHistory', id=uuid, limit=page_size, skip=page_num * page_size, type='auctions')
            if r is None:
                return
            r = r['userHistory']['auctions']

            if len(r) < page_size:
                last_page = True
            else:
                last_page = False

            embed = Embed(
                channel,
                title=f'Past Auctions From {name}',
                description=f'Page {page_num + 1} | Powered by https://hypixel-skyblock.com'
            )

            if r:
                for auction in r:
                    try:
                        buyer, _ = await skypy.fetch_uuid_uname(auction['bids'][0]['bidder'])
                    except skypy.ExternalAPIError:
                        buyer = '[error fetching name]'

                    item = auction['itemData']
                    embed.add_field(
                        name=f'{item["quantity"]}x {item["name"].upper()}',
                        value=f'```diff\n! {int(auction["highestBidAmount"]):,} coins\n'
                              f'-sold to {buyer}\n'
                              f'{datetime.fromtimestamp(int(auction["end"]) // 1000).strftime(TIME_FORMAT)}```'
                    )
            else:
                embed.add_field(name=None, value=r'```¯\_(ツ)_/¯```')

            return embed, last_page

        await self.book(user, channel, pages)

    async def buys(self, message, *args):
        page_size = 12

        user = message.author
        channel = message.channel

        if not args:
            await self.no_args('buys', user, channel)
            return

        name = args[0]
        try:
            _, uuid = await skypy.fetch_uuid_uname(name)
        except skypy.BadNameError:
            await channel.send(f'{user.mention} invalid username!')
            return

        async def pages(page_num):
            query = 'query UserHistory($id: String, $type: String, $limit: Int, $skip: Int) {userHistory(id: $id, type: $type, limit: $limit, skip: $skip) {auctions {id seller itemData {texture id name tag quantity lore __typename} bids {bidder timestamp amount __typename} highestBidAmount end __typename} __typename}}'
            r = await craftlink(user, channel, query, operation='UserHistory', id=uuid, limit=page_size, skip=page_num * page_size, type='purchases')
            if r is None:
                return
            r = r['userHistory']['auctions']

            if len(r) < page_size:
                last_page = True
            else:
                last_page = False

            embed = Embed(
                channel,
                title=f'Past Purchases From {name}',
                description=f'Page {page_num + 1} | Powered by https://hypixel-skyblock.com'
            )

            if r:
                for auction in r:
                    item = auction['itemData']
                    
                    try:
                        seller, _ = await skypy.fetch_uuid_uname(auction['seller'])
                    except skypy.ExternalAPIError:
                        seller = '[error fetching name]'
                    
                    embed.add_field(
                        name=f'{item["quantity"]}x {item["name"].upper()}',
                        value=f'```diff\n! {int(auction["highestBidAmount"]):,} coins\n'
                              f'-by {seller}\n'
                              f'{datetime.fromtimestamp(int(auction["end"]) // 1000).strftime(TIME_FORMAT)}```'
                    )
            else:
                embed.add_field(name=None, value=r'```¯\_(ツ)_/¯```')

            return embed, last_page

        await self.book(user, channel, pages)

    async def player(self, message, *args):
        user = message.author
        channel = message.channel

        if not args:
            await self.no_args('player', user, channel)
            return

        try:
            player = await skypy.Player(keys, uname=args[0], guild=True)
        except (skypy.BadNameError, skypy.NeverPlayedSkyblockError, Exception):
            await channel.send(f'{user.mention} invalid username!')
            return
        except skypy.ExternalAPIError as e:
            await channel.send(f'{user.mention} {e.reason}')
            return

        if len(args) == 1:
            await player.set_profile_automatically()
        else:
            try:
                await player.set_profile(player.profiles[args[1].capitalize()])
            except KeyError:
                await channel.send(f'{user.mention} invalid profile!')
                return
                
        await update_top_players(player)

        api_header = ' '.join(f'{k.capitalize()} {"✅" if v else "❌"}' for k, v in player.enabled_api.items())

        embed = Embed(
            channel,
            title=f'{player.uname} | {player.profile_name}',
            description=f'```{api_header}```\n'
                        f'```Skill Average > {player.skill_average:.2f}{"*" if player.uuid in EXPLOITERS else ""}\n'
                        f'Deaths > {player.deaths}\n'
                        f'Guild > {player.guild}\n'
                        f'Money > {player.bank_balance + player.purse:,.0f}\n'
                        f'Slots > {player.minion_slots} ({player.unique_minions} crafts)```'
        ).set_thumbnail(
            url=player.avatar()
        )

        for name, (emoji, function, optional_function, _, _) in LEVELS.items():
            embed.add_field(
                name=f'{emoji}\t{name}',
                value=f'```Level > {optional_function(player)}\nxp: {function(player):,}```'
            )

        if player.uuid in EXPLOITERS:
            embed.add_field(name="Cheater", value=f'***Player has bug abused or excessively macroed skill(s)**', inline=True)
            
        await embed.send()
        
    async def pets(self, message, *args):
        user = message.author
        channel = message.channel

        if not args:
            await self.no_args('pets', user, channel)
            return

        try:
            player = await skypy.Player(keys, uname=args[0], guild=True)
        except (skypy.BadNameError, skypy.NeverPlayedSkyblockError, Exception):
            await channel.send(f'{user.mention} invalid username!')
            return
        except skypy.ExternalAPIError as e:
            await channel.send(f'{user.mention} {e.reason}')
            return

        if len(args) == 1:
            await player.set_profile_automatically()
        else:
            try:
                await player.set_profile(player.profiles[args[1].capitalize()])
            except KeyError:
                await channel.send(f'{user.mention} invalid profile!')
                return
                
        await update_top_players(player)

        pets = '\n'.join(p.name for p in player.pets)

        embed = Embed(
            channel,
            title=f'{player.uname} | {player.profile_name}'
        ).set_thumbnail(
            url=player.avatar()
        )
            
        for pet in sorted(player.pets, key=lambda pet: (pet.active, pet.xp), reverse=True):
            value = colorize(f'Level > {pet.level}\nxp: {pet.xp:,.0f}', YELLOW if pet.active else WHITE)
        
            pin = '\t📌' if pet.active else ''
            embed.add_field(
                name=f'{PET_EMOJIS[pet.internal_name]}\t{pet.name}{pin}',
                value=value + colorize(pet.rarity.upper(), RARITY_COLORS[pet.rarity])
            )
            
        await embed.send()

    async def guild(self, message, *args):
        user = message.author
        channel = message.channel

        if not args:
            await self.no_args('guild', user, channel)
            return

        args = ' '.join(args).lower()

        try:
            guild = await skypy.Guild(keys, gname=args)
        except skypy.BadNameError:
            await channel.send(f'{user.mention} invalid guild!')
            return

        await asyncio.gather(*[update_top_players(player) for player in guild])

        embed = Embed(
            channel,
            title=f'{guild.gname} | {guild.tag}' if guild.tag else guild.gname,
            description=f'```Skill Average > {guild.stat_average("skill_average"):.3f}\n'
                        f'Players > {len(guild)}\n'
                        f'Level > {guild.level}\n'
                        f'Deaths > {guild.deaths:,}\n'
                        f'Average Money > {(guild.bank_balance + guild.purse) / len(guild):,.0f}\n'
                        f'Slots > {guild.stat_average("minion_slots"):.3f} ({guild.stat_average("unique_minions"):.0f} crafts)```'
        )

        for name, (emoji, _, _, function, optional_function) in LEVELS.items():
            embed.add_field(
                name=f'{emoji}\t{name}',
                value=f'```Level > {optional_function(guild):.3f}\nxp: {function(guild):,.0f}```'
            )

        menu = {}
        prompt = {}
        for name, (emoji, function, optional_function, _, _) in LEADERBOARDS.items():
            lb = Embed(
                channel,
                title=f'{guild.gname} {name} Leaderboard'
            )

            if optional_function:
                players = [(player, function(player), optional_function(player)) for player in guild.players]
            else:
                players = [(player, function(player)) for player in guild.players]

            players.sort(key=lambda tuple: tuple[1], reverse=True)

            if optional_function:
                players = [f'#{str(index + 1).ljust(2)} {player.uname} [{optional_stat:.2f}] [{stat:,.2f}]'
                           for index, (player, stat, optional_stat) in enumerate(players)]
            else:
                players = [f'#{str(index + 1).ljust(2)} {player.uname} [{stat:,.2f}]'
                           for index, (player, stat) in enumerate(players)]

            portion = len(players) / 30
            sections = [0, 1, 4, 9, 15, 22, 30]
            peppers = random.choice(RANKS)
            meal = {}
            for i, pepper in enumerate(peppers):
                meal[pepper] = players[round(sections[i] * portion): round(sections[i + 1] * portion)]

            for pepper, players in meal.items():
                lb.add_field(
                    name=pepper,
                    value=('```css\n' + "\n".join(players)[:1000] + '```') if players else r'```¯\_(ツ)_/¯```',
                    inline=False
                )

            prompt[emoji] = name
            menu[emoji] = lb

        reaction_prompt = '**React to this message for guild leaderboards**```'
        for group in chunks(prompt.items(), 4):
            reaction_prompt += f'{" | ".join([" ".join(g) for g in group])}\n'
        reaction_prompt += '```'

        embed.add_field(
            name=None,
            value=reaction_prompt,
            inline=False
        )

        while True:
            msg = await embed.send()
            lb = await self.reaction_menu(msg, user, menu)
            if lb:
                await msg.delete()
                msg = await lb.send()
                if await self.back(msg, user):
                    await msg.delete()
                else:
                    break
            else:
                break

    @staticmethod
    async def unimplemented(message):
        await message.channel.send(f'{message.author.mention} this command is unimplemented')

    async def optimize_talismans(self, message, *args):
        user = message.author
        channel = message.channel
        
        valid = False
        while valid is False:
            await channel.send(f'{user.mention} what is your Minecraft username?')
            msg = await self.respond(user, channel)
            if msg is None:
                return

            msg = msg.content.lower()

            try:
                player = await skypy.Player(keys, uname=msg)
                if len(player.profiles) == 0:
                    await embed(
                        channel,
                        title=f'{user.name}, the Hypixel API has returned invalid information'
                    ).add_field(
                        name=None,
                        value='You can usually solve this issue by simply retrying in a few minutes, contact melon if otherwise'
                    ).set_footer(
                        text='This error is rare, about the same chance as getting an overflux! Congratulations!'
                    ).send()
                    return

                else:
                    valid = True

            except skypy.NeverPlayedSkyblockError:
                await channel.send(f'You have never played skyblock{CLOSE_MESSAGE}')

            except skypy.BadNameError:
                await channel.send(f'Invalid username!{CLOSE_MESSAGE}')
                
            except skypy.ExternalAPIError as e:
                await channel.send(f'{user.mention} {e.reason}')
                return

        if len(player.profiles) == 1:
            await player.set_profile(list(player.profiles.values())[0])

        else:
            embed = Embed(
                channel,
                title='Which profile do you want to use?',
                description='Sorted by date created'
            ).add_field(
                name=None,
                value='\n\n'.join(player.profiles.keys())
            )

            valid = False

            while valid is False:
                await embed.send()

                msg = await self.respond(user, channel)
                if msg is None:
                    return
                msg = msg.content.capitalize()

                if msg in player.profiles:
                    await player.set_profile(player.profiles[msg])
                    valid = True

                else:
                    await channel.send(f'Invalid profile! Did you make a typo?{CLOSE_MESSAGE}')

        if player.enabled_api['skills'] is False or player.enabled_api['inventory'] is False:
            await self.api_disabled(user.name, '', 'API', channel)
            return
        
        if len(player.weapons) == 0:
            await channel.send(f'{user.mention} you have `no weapons` in your inventory')
            return
            
        if len(player.weapons) == 1:
            weapon = player.weapons[0]
        else:
            valid = False

            while valid is False:
                await Embed(
                    channel,
                    title='Which weapon would you like to use?'
                ).set_footer(
                    text='You may use either the weapon name or the weapon number'
                ).add_field(
                    name=None,
                    value=''.join([f'```{i + 1} > ' + weapon.name + '```' for i, weapon in enumerate(player.weapons)])
                ).send()

                msg = await self.respond(user, channel)
                if msg is None:
                    return
                msg = msg.content.lower()

                names = [weapon.name.lower() for weapon in player.weapons]

                if msg in names:
                    weapon = player.weapons[names.index(msg)]
                    valid = True
                else:
                    try:
                        weapon = player.weapons[int(msg) - 1]
                        valid = True
                    except (IndexError, TypeError, ValueError):
                        await channel.send(f'Invalid weapon! Did you make a typo?{CLOSE_MESSAGE}')

        embed = Embed(
            channel,
            title='Is this the correct equipment?'
        ).add_field(
            name='Weapon',
            value=f'```{weapon.name}```',
            inline=False
        )

        for piece in ['helmet', 'chestplate', 'leggings', 'boots']:
            embed.add_field(
                name=piece.capitalize(),
                value='```' + str(next((a.name for a in player.armor if a.type == piece), None)) + '```',
                inline=False
            )

        for name, amount in player.talisman_counts().items():
            if amount:
                embed.add_field(name=Route.rarity_grammar(name).capitalize(), value=amount)

        if not await self.yesno(await embed.send(), user):
            await channel.send(f'{user.mention} session ended')
            return

        numbers = ['0️⃣', '1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣', '7️⃣', '8️⃣', '9️⃣', '🔟']

        stats = {'crit damage': 0, 'crit chance': 0, 'strength': 0, 'enchantment modifier': 0, 'damage': 0}

        for name, pot in DAMAGING_POTIONS.items():
            buff = pot['stats']
            levels = pot['levels']

            if weapon.type != 'bow' and name == 'archery':
                continue

            msg = await channel.send(f'{user.mention} what level of `{name} potion` do you use?')

            emojis = {numbers[level]: level for level in levels}

            level = await self.reaction_menu(msg, user, emojis)
            if level is None:
                return

            for name1, amount in buff.items():
                stats[name1] += amount[level]

        for name, orb in ORBS.items():
            internal_name = orb['internal']
            buff = orb['stats']

            if internal_name in player.inventory or internal_name in player.echest:
                msg = await channel.send(f'{user.mention} will you be using your `{name}`?')
                yn = await self.yesno(msg, user)

                if yn is True:
                    for name, amount in buff.items():
                        stats[name] += amount

        def apply_stats(additional, reverse=False):
            for key, value in additional.items():
                if key in stats:
                    if reverse:
                        stats[key] -= value
                    else:
                        stats[key] += value

        apply_stats(player.base_stats())
        apply_stats(player.fairy_soul_stats())
        apply_stats(player.armor_stats())
        apply_stats(player.slayer_stats())
        apply_stats(player.skill_stats())
        apply_stats(weapon.stats())
        weapon_damage = stats['damage']
        
        apply_stats(player.talisman_stats(include_reforges=True))
        cur_str = stats['strength']
        cur_cc = stats['crit chance']
        cur_cd = stats['crit damage']
        apply_stats(player.talisman_stats(include_reforges=True), reverse=True)
        apply_stats(player.talisman_stats(include_reforges=False))

        stat_modifiers = player.stat_modifiers()
        str_mod = stat_modifiers.get('strength', lambda x: x)
        cc_mod = stat_modifiers.get('crit chance', lambda x: x)
        cd_mod = stat_modifiers.get('crit damage', lambda x, y: x)

        cur_str = str_mod(cur_str)
        cur_cc = cc_mod(cur_cc)
        cur_cd = cd_mod(cur_cd, cur_str)

        base_str = stats['strength']
        base_cc = stats['crit chance']
        base_cd = stats['crit damage']

        counts = player.talisman_counts()

        best = 0
        best_route = []
        best_str = 0
        best_cc = 0
        best_cd = 0

        #print(*(f"({n} {v})" for n, v in locals().items()))

        if cc_mod(base_cc) <= 100:
            cc_mod = stat_modifiers.get('crit chance', None)
            if cc_mod:
                for c, u, r, e, l in itertools.product(
                        *[Route.routes(counts[key], 4, rarity_num) for rarity_num, key in enumerate(counts.keys())]):
                    crit_chance = cc_mod(
                        base_cc + c.crit_chance + u.crit_chance + r.crit_chance + e.crit_chance + l.crit_chance) // 1
                    if crit_chance >= 100:
                        strength = str_mod(base_str + c.strength + u.strength + r.strength + e.strength + l.strength)
                        crit_damage = cd_mod(
                            base_cd + c.crit_damage + u.crit_damage + r.crit_damage + e.crit_damage + l.crit_damage,
                            strength)

                        d = (5 + weapon_damage + strength // 5) * (1 + strength / 100) * (1 + crit_damage / 100)

                        if d > best:
                            best = d
                            best_route = [c, u, r, e, l]
                            best_str = strength
                            best_cc = crit_chance
                            best_cd = crit_damage
            else:
                for c, u, r, e, l in itertools.product(
                        *[Route.routes(counts[key], 4, rarity_num) for rarity_num, key in enumerate(counts.keys())]):
                    crit_chance = base_cc + c.crit_chance + u.crit_chance + r.crit_chance + e.crit_chance + l.crit_chance
                    if crit_chance >= 100:
                        strength = str_mod(base_str + c.strength + u.strength + r.strength + e.strength + l.strength)
                        crit_damage = cd_mod(
                            base_cd + c.crit_damage + u.crit_damage + r.crit_damage + e.crit_damage + l.crit_damage,
                            strength)

                        d = (5 + weapon_damage + strength // 5) * (1 + strength / 100) * (1 + crit_damage / 100)

                        if d > best:
                            best = d
                            best_route = [c, u, r, e, l]
                            best_str = strength
                            best_cc = crit_chance
                            best_cd = crit_damage
        else:
            for c, u, r, e, l in itertools.product(
                    *[Route.routes(counts[key], 4, rarity_num) for rarity_num, key in enumerate(counts.keys())]):
                strength = str_mod(base_str + c.strength + u.strength + r.strength + e.strength + l.strength)
                crit_damage = cd_mod(
                    base_cd + c.crit_damage + u.crit_damage + r.crit_damage + e.crit_damage + l.crit_damage, strength)

                d = (5 + weapon_damage + strength // 5) * (1 + strength / 100) * (1 + crit_damage / 100)

                if d > best:
                    best = d
                    best_route = [c, u, r, e, l]
                    best_str = strength
                    best_cc = cc_mod(
                        base_cc + c.crit_chance + u.crit_chance + r.crit_chance + e.crit_chance + l.crit_chance)
                    best_cd = crit_damage

        if not best_route:
            await Embed(
                    channel,
                title='There is no possible setup that will give you 100% crit chance',
                description='Collect more talismans or raise your combat level before trying again'
            ).send()
            return

        embed = Embed(
            channel,
            title='Success!'
        )
        for route, color in zip(best_route, [GRAY, GREEN, BLUE, RED, YELLOW]):
            route = route if route.counts else r'```¯\_(ツ)_/¯```'
            
            embed.add_field(
                name=f'**{route.rarity_str.title()}**',
                value=colorize(route, color),
                inline=False
            )
        
        def emod(activity):
            result = 0
            for enchantment in ACTIVITIES[activity]:
                if enchantment in weapon.enchantments:
                    value = ENCHANTMENT_VALUES[enchantment]
                    if callable(value):
                        result += value(weapon.enchantments[enchantment])
                    else:
                        result += value * weapon.enchantments[enchantment]
            return result
        
        base_mod = stats['enchantment modifier'] + player.skills['combat'] * 4
        zealot_mod = emod('zealots') + base_mod
        slayer_mod = emod('slayer bosses') + base_mod
        
        if weapon.internal_name == 'REAPER_SWORD':
            slayer_mult = 3
        elif weapon.internal_name == 'SCORPION_FOIL':
            slayer_mult = 2.5
        else:
            slayer_mult = 1
        
        zealot_damage = skypy.damage(weapon_damage, cur_str, cur_cd, zealot_mod)
        slayer_damage = skypy.damage(weapon_damage, cur_str, cur_cd, slayer_mod)
        slayer_damage *= slayer_mult
        
        zealot_damage_after = skypy.damage(weapon_damage, best_str, best_cd, zealot_mod)
        slayer_damage_after = skypy.damage(weapon_damage, best_str, best_cd, slayer_mod)
        slayer_damage_after *= slayer_mult
        
        embed.add_field(
            name='**Before**',
            value=f'```{cur_str:.0f} strength\n{cur_cd:.0f} crit damage\n{cur_cc:.0f} crit chance```'
                  f'```{zealot_damage:,.0f} to zealots\n{slayer_damage:,.0f} to slayers```'
        )
        
        embed.add_field(
            name='**After**',
            value=f'```{best_str:.0f} strength\n{best_cd:.0f} crit damage\n{best_cc:.0f} crit chance```'
                  f'```{zealot_damage_after:,.0f} to zealots\n{slayer_damage_after:,.0f} to slayers```'
        )
            
        if zealot_damage > zealot_damage_after or slayer_damage > slayer_damage_after:
            embed.set_footer(
                text=f'Even though you will be dealing less damage, you will gain {best_cc - cur_cc} crit chance'
            )
            
        await embed.send()
        
    async def calculate_damage(self, message, *args):
        channel = message.channel
        user = message.author

        stats = {'strength': 0, 'crit damage': 0, 'weapon damage': 0, 'combat level': 0}
        questions = {
            'strength': f'{user.mention} how much **strength** do you want to have?',
            'crit damage': f'{user.mention} how much **crit damage** do you want to have?',
            'weapon damage': f'{user.mention} how much **damage** does your weapon have on the tooltip?',
            'combat level': f'{user.mention} what is your **combat level**?'
        }
        
        for stat in stats.keys():
            await channel.send(questions[stat])
            resp = await self.respond(user, channel)
            if resp is None:
                return

            if resp.content[0] == '+':
                resp.content = resp.content[1:]

            if resp.content.isdigit() is False or len(resp.content) > 20:
                await channel.send(f'{user.mention} Invalid input!')
                return
            stats[stat] = int(resp.content)

        mobs = '\n'.join([k.capitalize() for k in ACTIVITIES.keys()])

        embed = Embed(
            channel,
            title='Which mob will you be targeting with this setup?'
        ).add_field(
            name=None,
            value=f'```{mobs}```',
        )

        while True:
            await embed.send()

            resp = await self.respond(user, channel)
            if resp is None:
                return
            resp = resp.content.lower()

            if resp in ACTIVITIES:
                break
            else:
                await channel.send(f'{user.mention} choose one of the listed enemies{CLOSE_MESSAGE}')

        msg = await channel.send(
            f'{user.mention} do you want to use **level 5** or **level 6** enchantments? **[react to this message]**')
        enchant_levels = await self.reaction_menu(msg, user, {'5️⃣': CHEAP_MAX_BOOK_LEVELS, '6️⃣': MAX_BOOK_LEVELS})
        if enchant_levels is None:
            return

        modifier = stats['combat level'] * 4
        for enchantment in ACTIVITIES[resp]:
            perk = ENCHANTMENT_VALUES[enchantment]
            if callable(perk):
                modifier += perk(enchant_levels[enchantment])
            else:
                modifier += perk * enchant_levels[enchantment]                

        damage = round(skypy.damage(
            stats['weapon damage'],
            stats['strength'],
            stats['crit damage'],
            modifier
        ))

        no_crit = round(skypy.damage(
            stats['weapon damage'],
            stats['strength'],
            0,
            modifier
        ))

        await Embed(
            channel,
            title=f'{user.name}, you should be doing **{damage} damage** with those stats'
        ).add_field(
            name=f'**{no_crit}** without a crit',
            value='```lua\n(5 + damage + floor(str ÷ 5)) ⋅\n(1 + str ÷ 100) ⋅\n(1 + cd ÷ 100) ⋅\n(1 + enchants ÷ 100)```'
        ).send()

    async def view_missing_talismans(self, message, *args):
        user = message.author
        channel = message.channel

        if not args:
            await self.no_args('missing', user, channel)
            return

        try:
            player = await skypy.Player(keys, uname=args[0], guild=True)
        except (skypy.BadNameError, skypy.NeverPlayedSkyblockError):
            await channel.send(f'{user.mention} invalid username!')
            return
        except skypy.ExternalAPIError as e:
            await channel.send(f'{user.mention} {e.reason}')
            return

        if len(args) == 1:
            await player.set_profile_automatically()
        else:
            try:
                await player.set_profile(player.profiles[args[1].capitalize()])
            except KeyError:
                await channel.send(f'{user.mention} invalid profile!')
                return

        if player.enabled_api['inventory'] is False:
            await self.api_disabled(player.uname, f' on {player.profile_name.title()}', 'inventory API', channel)
            return

        talismans = skypy_constants.talismen.copy()
        for talisman in player.talismans:
            if talisman.active and talisman.internal_name in talismans:
                talismans.pop(talisman.internal_name)

        embed = Embed(
            channel,
            title=f'{player.uname}, you are missing {len(talismans)} talisman{"" if len(talismans) == 1 else "s"}!',
            description='Only counting talismans in your bag or inventory'
        )

        if talismans:
            embed.add_field(
                name='[Roughly sorted by price]',
                value='```' + '\n'.join(talismans.values()) + '```',
                inline=False
            )

        inactive = [talisman for talisman in player.talismans if talisman.active is False]

        if inactive:
            embed.add_field(
                name=f'You also have {len(inactive)} unnecessary talismans',
                value='```' + '\n'.join(map(str, inactive)) + '```'
                                                              '```An unnecessary talisman is any talisman is\nduplicated or part of a talisman familiy```'
            )

        await embed.send()

    async def help(self, message, *args):
        user = message.author
        channel = message.channel

        if user.dm_channel != channel:
            await channel.send(f'Sent you a DM with the information {user.mention}!')

        dm = user.dm_channel or await user.create_dm()

        embed = Embed(
            dm,
            title='Skyblock Simplified',
            description='Welcome to Skyblock Simplified, a Skyblock bot designed to streamline gameplay\nAdd to your server with https://tinyurl.com/add-sbs\n'
                        f'**React to this message with any of the emojis to view commands**\n{self.args_message}\n'
        ).set_footer(
            text='Skyblock Simplified for Hypixel Skyblock | Created by notnotmelon#7218'
        )

        for category, data in self.commands.items():
            embed.add_field(
                name=f'{data["emoji"]}  {category}',
                value=f'```{data["desc"]}```'
            )

        boxes = {}
        for category, data in self.commands.items():
            category_data = self.commands[category]

            def command_desc(name, data):
                security = data['security'] if 'security' in data else 0
                args = f' {data["args"]}' if 'args' in data else ''

                moderators = "\n\t*Can only be used by moderators*" if security == 1 else ""
                return f'> {self.user.mention} {name}{args}\n{data["desc"]}{moderators}'

            boxes[data['emoji']] = Embed(
                dm,
                title=category.capitalize(),
                description=f'{self.args_message}\n```{category_data["desc"]}```'
            ).add_field(
                name=None,
                value='\n\n'.join([command_desc(name, data) for name, data in category_data['commands'].items()])
            ).set_footer(
                text='Skyblock Simplified for Hypixel Skyblock | Created by notnotmelon#7218'
            )

        while True:
            try:
                msg = await embed.send()
            except discord.errors.Forbidden:
                await channel.send(f'{user.mention} your DM\'s are turned off')
                return

            box = await self.reaction_menu(msg, user, boxes)
            if box is None:
                return
            if await self.back(await box.send(), user) is False:
                return

    async def stats(self, message, *args):
        channel = message.channel

        server_rankings = sorted(self.guilds, key=lambda guild: len(guild.members), reverse=True)[:10]
        server_rankings = f'{"Top Servers".ljust(28)} | Users\n' + '\n'.join(
            [f'{guild.name[:28].ljust(28)} | {len(guild.members)}' for guild in server_rankings])

        await Embed(
            channel,
            title='Discord Stats'
        ).add_field(
            name='Servers',
            value=f'{self.user.name} is running in {len(self.guilds)} servers with {sum(len(guild.text_channels) for guild in self.guilds)} channels\n```{server_rankings}```',
            inline=False
        ).add_field(
            name='Users',
            value=f'There are currently {sum(len(guild.members) for guild in self.guilds)} users with access to the bot',
            inline=False
        ).add_field(
            name='Heartbeat',
            value=f'This message was delivered in {self.latency * 1000:.0f} milliseconds',
            inline=False
        ).send()

    async def start_event(self, message, *args):
        await self.unimplemented(message)

    async def view_lb(self, message, *args):
        await self.unimplemented(message)

    async def end_event(self, message, *args):
        await self.unimplemented(message)

    async def respond(self, user, channel):
        msg = None

        try:
            msg = await self.wait_for('message',
                                      check=lambda message: message.author == user and message.channel == channel,
                                      timeout=60 * 3)
        except asyncio.TimeoutError:
            await channel.send(f'{user.mention} session timed out')
            return None
        if msg.content.lower() == 'exit':
            await channel.send(f'Session closed with {user.mention}')
            return None

        return msg

    async def reaction_menu(self, message, user, reactions, edit=False):
        if edit:
            await message.clear_reactions()

        for reaction in reactions.keys():
            await message.add_reaction(reaction)

        check = lambda reaction, u: u == user and reaction.message.id == message.id and str(reaction) in reactions

        try:
            reaction, _ = await self.wait_for('reaction_add', check=check, timeout=600)
            return reactions[str(reaction)]
        except asyncio.TimeoutError:
            for reaction in reactions.keys():
                await message.remove_reaction(reaction, self.user)
            for reaction in ['🇹', '🇮', '🇲', '🇪', '🇴', '🇺', '✝️']:
                await message.add_reaction(reaction)
            return None

    async def back(self, message, user):
        return True if await self.reaction_menu(message, user, {'⬅️': True}) else False

    async def yesno(self, message, user):
        return await self.reaction_menu(message, user, {'✅': True, '❌': False})

    async def book(self, user, channel, pages):
        page_num = 0
        backward = {'⬅️': -1}
        forward = {'➡️': 1}
        both = {'⬅️': -1, '➡️': 1}

        if user.dm_channel != channel and channel.guild.me.permissions_in(channel).manage_messages:
            r = await pages(page_num)
            if r is None:
                return
            embed, last_page = r
            
            msg = await embed.send()
            while True:
                if page_num == 0 and last_page is True:
                    return
                
                if page_num == 0:
                    result = await self.reaction_menu(msg, user, forward, edit=True)
                elif last_page is True:
                    result = await self.reaction_menu(msg, user, backward, edit=True)
                else:
                    result = await self.reaction_menu(msg, user, both, edit=True)
                if result is None:
                    break
                page_num += result
                
                r = await pages(page_num)
                if r is None:
                    return
                embed, last_page = r
                
                await msg.edit(embed=embed)
        else:
            while True:
                r = await pages(page_num)
                if r is None:
                    return
                embed, last_page = r
            
                msg = await embed.send()
                if page_num == 0 and last_page is True:
                    return
                    
                if page_num == 0:
                    result = await self.reaction_menu(msg, user, forward, edit=False)
                elif last_page is True:
                    result = await self.reaction_menu(msg, user, backward, edit=False)
                else:
                    result = await self.reaction_menu(msg, user, both, edit=False)
                if result is None:
                    break
                await msg.delete()
                page_num += result

    async def view_trending(self, message, *args):
        embed = Embed(
            message.channel,
            title='Trending Threads',
            description=f'It\'s the talk of the town! Here\'s six popular threads from the past {trending_timeout} hours'
        ).set_footer(
            text=f'Last updated {last_forums_update.strftime(TIME_FORMAT)}'
        )

        if trending_threads:
            for thread in trending_threads:
                embed.add_field(
                    name=f'**{thread["name"]}\n_{thread["views"]} views_ | _{thread["likes"]} likes_**',
                    value=f'[{thread["link"]}]'
                )
        else:
            embed.add_field(
                name=None,
                value='Hypixel currently has their anti DDOS protection enabled. I can\'t get in!'
            )

        await embed.send()

    async def api_disabled(self, text, text_end, kind, channel):
        await Embed(
            channel,
            title=f'{text}, your **{kind}** is disabled!{text_end}',
            description='Re-enable them with [skyblock menu > settings > api settings]'
        ).set_footer(
            text='Sometimes this message appears even if your API settings are enabled. If so, exit Hypixel and try again. It\'s also possible that Hypixel\'s API servers are down'
        ).send()

    async def support_server(self, message, *args):
        await Embed(
            message.channel,
            title='Here\'s a link to my support server',
            description='[https://discord.gg/8Wbh3p7]'
        ).set_footer(
            text='(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧'
        ).send()

async def craftlink(user, channel, query, *, operation, **kwargs):
    url = 'https://craftlink.xyz/graphql'

    json = {
        'operationName': operation,
        'variables': dict(kwargs),
        'query': query
    }
    
    try:
        async with (await skypy.session()).post(url, json=json) as r:
            return (await r.json(content_type=None))['data']
    except (asyncio.exceptions.TimeoutError, ClientError, ValueError):
        await channel.send(f'{user.mention} {url} did not respond after 30 seconds')
        return None

client = motor.motor_asyncio.AsyncIOMotorClient(os.getenv('DATABASE_URI'))
db = client.sbs

async def update_top_players(player):
    global db
    lb = db.leaderboards
    
    try:
        if player.uuid in EXPLOITERS:
            for offence in EXPLOITERS[player.uuid]:
                player.skills[offence] *= -1
            player.skill_average = sum(list(player.skills.values())[0:7]) / 7
        
        document = {
            'name': player.uname,
            'uuid': player.uuid
        }
        
        for name, (emoji, function, optional_function, _, _) in LEADERBOARDS.items():
            document[name] = function(player)
            if optional_function:
                document[f'{name}_'] = optional_function(player)
    except AttributeError:
        await client.log(f'Failed to add {player.uname} to leaderboards')
        return
    
    await lb.replace_one({'uuid': player.uuid}, document, upsert=True)
    await client.log(f'Leaderboard updated for {player.uname}')

# Forums parsing ---
trending_threads = []
last_forums_update = datetime.now()
num_trending = 6
trending_timeout = int(os.getenv('TRENDING_TIMEOUT'))

def trending_algorithm(thread):
    return (thread['views'] + thread['likes'] * 200) / math.sqrt(thread['date'] / 1000 + 1)

def update_trending():
    global trending_threads, last_forums_update
    loop = asyncio.new_event_loop()

    class Timeout(Exception):
        pass

    class Nothing(Exception):
        pass

    while True:
        pagenumber = 1
        now = None
        backup = trending_threads.copy()
        trending_threads.clear()
        s = cloudscraper.create_scraper()

        try:
            while True:
                loop.run_until_complete(client.log(f'Attempting to parse forums page {pagenumber}'))

                soup = BeautifulSoup(
                    s.get(f'https://hypixel.net/forums/skyblock.157/page-{pagenumber}?order=post_date').content,
                    'html.parser',
                    multi_valued_attributes=None
                )
                posts = soup.find_all(class_='discussionListItem visible  ')
                if not posts:
                    raise Nothing

                for post in posts:
                    thread = {}

                    header = post.find('h3').a
                    thread['link'] = f'https://hypixel.net/{header["href"]}'
                    thread['name'] = header.string

                    info = post.find(class_='listBlock stats pairsJustified')
                    thread['likes'] = int(info['title'].replace('Members who liked the first message: ', ''))
                    thread['views'] = int(info.find(class_='minor').dd.string.replace(',', ''))
                    thread['replies'] = int(info.find(class_='major').dd.string.replace(',', ''))
                    thread['date'] = int(post.find(class_='posterDate muted').find('abbr')['data-time'])

                    if now is None:
                        now = thread['date']

                    thread['date'] = now - thread['date']
                    if thread['date'] >= trending_timeout * 3600:
                        raise Timeout

                    if discord.utils.find(lambda t: thread['link'] == t['link'], trending_threads) is None:
                        trending_threads.append(thread)
                        trending_threads.sort(key=trending_algorithm, reverse=True)
                        del trending_threads[num_trending:]
                pagenumber += 1

        except Timeout:
            now = datetime.now(timezone.utc)
            last_forums_update = now
            loop.run_until_complete(client.log(
                f'Trending threads updated at {now.strftime(TIME_FORMAT)}. {pagenumber} pages parsed\n',
                '\n'.join([thread['link'] for thread in trending_threads])
            ))

        except (Nothing, RuntimeError):
            now = datetime.now(timezone.utc)
            loop.run_until_complete(client.log(f'Failed to parse forums at {now.strftime(TIME_FORMAT)}'))
            trending_threads = backup
            
        loop.run_until_complete(asyncio.sleep(3600 * 2))

discord.Embed = None  # Disable default discord Embed
client = Bot()
client.loop.run_in_executor(None, update_trending)
client.run(os.getenv('DISCORD_TOKEN'))