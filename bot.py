import concurrent.futures
from aiohttp import ClientError
import cloudscraper
from bs4 import BeautifulSoup
from datetime import datetime, timezone, timedelta
from statistics import mean, median, mode, pstdev, StatisticsError
import random
import re
import itertools
import motor.motor_asyncio
import traceback
import math
import asyncio
import discord
import os
import skypy
from constants import skills, cosmetic_skills
skypy.enable_advanced_mode()


TIME_FORMAT = '%m/%d %I:%M %p UTC'

if os.environ.get('API_KEY') is None:
	import dotenv
	dotenv.load_dotenv()

keys = os.getenv('API_KEY').split()
prefix = os.getenv('TOKEN', 'sbs')

class EndSession(Exception):
	def __init__(self, message=''):
		self.message = message

	def __str__(self):
		return self.message


def time_until(goal):
	now = datetime.now(timezone.utc)
	then = datetime.fromtimestamp(goal, timezone.utc)
	delta = then - now

	d, h, m, s = delta.days, delta // timedelta(
		hours=1), delta // timedelta(minutes=1), delta.seconds

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
		# Assume cola
		'stats': {'strength': [0, 5.25, 13.125, 21, 31.5, 42, 52.5, 63, 78.75]},
		'levels': [0, 5, 6, 7, 8]
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
	'skill average': ('📈', lambda player: player.skill_average, None),
	'minion slots': ('⛓', lambda player: player.unique_minions, lambda player: player.minion_slots),
	'farming': ('🌾', lambda player: player.skill_xp['farming'], lambda player: player.skills['farming']),
	'mining': ('⛏', lambda player: player.skill_xp['mining'], lambda player: player.skills['mining']),
	'combat': ('⚔', lambda player: player.skill_xp['combat'], lambda player: player.skills['combat']),
	'foraging': ('🪓', lambda player: player.skill_xp['foraging'], lambda player: player.skills['foraging']),
	'enchanting': ('📖', lambda player: player.skill_xp['enchanting'], lambda player: player.skills['enchanting']),
	'alchemy': ('⚗', lambda player: player.skill_xp['alchemy'], lambda player: player.skills['alchemy']),
	'fishing': ('🎣', lambda player: player.skill_xp['fishing'], lambda player: player.skills['fishing']),
	'taming': ('🐣', lambda player: player.skill_xp['taming'], lambda player: player.skills['taming']),
	'carpentry': ('🪑', lambda player: player.skill_xp['carpentry'], lambda player: player.skills['carpentry']),
	'runecrafting': ('⚜️', lambda player: player.skill_xp['runecrafting'], lambda player: player.skills['runecrafting']),
	'zombie': ('🧟', lambda player: player.slayer_xp['zombie'], lambda player: player.slayers['zombie']),
	'spider': ('🕸️', lambda player: player.slayer_xp['spider'], lambda player: player.slayers['spider']),
	'wolf': ('🐺', lambda player: player.slayer_xp['wolf'], lambda player: player.slayers['wolf']),
	'total slayer': ('☠️', lambda player: player.total_slayer_xp, None)
}

LEVELS = {name: LEADERBOARDS[name] for name in skypy.skills + skypy.slayers}

RANKS = [
	['CAROLINA REAPER', 'GHOST PEPPER', 'HABAÑERO',
		'JALAPEÑO', 'SWEET BANANA', 'BELL PEPPER'],
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
'''
EXPLOITERS = {
	'6c80f48d85544035bb31e6cb9f40b948': ('farming', 'enchanting'),
	'04e0ad3f4b7f4815bb39c3888249115c': ('farming'),
	'6ac668e787e74561b86bae8c496d0f97': ('farming'),
	'02bd483c511b4e1fbd0f0c071e2d0411': ('farming'),
	'e91e2680d7da4bc4adbb30c04366f6fa': ('farming'),
	'd14403fd77664905929ee1a6e365e623': ('enchanting'),
	'8f0d1d399aee48f59d5af5f0f69e4eee': ('enchanting'),
	'720d2a83efe446969bc29fbc8c98b31e': ('enchanting'),
	'f33f51a796914076abdaf66e3d047a71': ('enchanting'),
	'73464a378313409d8232076f44074bcf': ('enchanting'),
	'7b488582998f405a84c19ad7a4e9b2e7': ('enchanting'),
	'6170dede383a42a99db6166ca46a8469': ('combat'),
	'6c5b615c2c47428aad137249d37c6fcc': ('farming'),
	'44d03c6e2cba41799ad5c9d2f837d03d': ('farming'),
	'446dea472dd0494b89260421b9981d15': ('combat')
}
'''
EXPLOITERS = {}

PROFILE_EMOJIS = {
	'Apple': '🍎',
	'Banana': '🍌',
	'Blueberry': '🔵',
	'Coconut': '🥥',
	'Cucumber': '🥒',
	'Grapes': '🍇',
	'Kiwi': '🥝',
	'Lemon': '🍋',
	'Lime': '🍏',
	'Mango': '🥭',
	'Orange': '🍊',
	'Papaya': '🍈',
	'Peach': '🍑',
	'Pear': '🍐',
	'Pineapple': '🍍',
	'Pomegranate': '👛',
	'Raspberry': '🍒',
	'Strawberry': '🍓',
	'Tomato': '🍅',
	'Watermelon': '🍉',
	'Zucchini': '🥬'
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
	'snipe': 5,	 # Would be lower except I only use this for drags and magma bosses
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
	'dragon_hunter': 0,
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

'''
RELEVANT_REFORGES = {
	'forceful': ((2, 0), (4, 0), (7, 0), None, None),
	'itchy': ((1, 3), (2, 5), (2, 8), (3, 12), (5, 15)),
	'strong': (None, None, (4, 4), (7, 7), (10, 10))
}
'''

CLOSE_MESSAGE = '\n> _use **exit** to close the session_'

PET_EMOJIS = {
	'SKELETON_HORSE': '🦓',
	'SNOWMAN': '⛄',
	'BAT': '🦇',
	'SHEEP': '🐑',
	'CHICKEN': '🐔',
	'WITHER_SKELETON': '🏴‍☠️',
	'SILVERFISH': '🐁',
	'RABBIT': '🐇',
	'HORSE': '🐴',
	'PIGMAN': '🐽',
	'WOLF': '🐺',
	'OCELOT': '🐆',
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
	'SPIDER': '🕷️',
	'BLAZE': '🔥',
	'JERRY': '🤡',
	'PIG': '🐽',
	'BLACK_CAT': '🐱',
	'JELLYFISH': '🎐',
	'MONKEY': '🐒',
	'ELEPHANT': '🐘',
	'ZOMBIE': '🧟',
	'SKELETON': '💀',
	'ENDERMITE': '🦠',
	'ROCK': '🥌',
	'DOLPHIN': '🐬',
	'HOUND': '🐶',
	'GHOUL': '🧟‍♀️',
	'TARANTULA': '🕸️',
	'GOLEM': '🗿'
}


class Embed(discord.Embed):
	nbst = '\u200b'

	def __init__(self, channel, *, user=None, **kwargs):
		self.channel = channel
		self.user = user

		super().__init__(
			color=self.color(channel),
			**kwargs
		)

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

	def set_image(self, url):
		return super().set_image(url=url)

	async def send(self):
		return await self.channel.send(self.user.mention if self.user else None, embed=self)


def format_pet(pet):
	"""Returns a pretty string repersenting a pet"""
	return f'{pet.title} |{pet.rarity.upper()}|' if pet else ''


WHITE = ('', '')
GRAY = ('bf', '')
GREY = GRAY
PUKE = ('css', '')
GREEN = ('yaml', '')
BLUE = ('md', '#')
YELLOW = ('fix', '')
ORANGE = ('glsl', '#')
RED = ('diff', '-')
RARITY_COLORS = {'common': GREY, 'uncommon': GREEN,
	'rare': BLUE, 'epic': ORANGE, 'legendary': YELLOW}
RARITY_SCORES = {'common': 1, 'uncommon': 2,
	'rare': 3, 'epic': 4, 'legendary': 5}


def colorize(s, color):
	language, point = color
	s = str(s)

	if s:
		return f'```{language}\n{point}' + s.replace('\n', f'\n{point}') + '\n```'
	else:
		return ''


formatting_codes = {
	'0': GREY,
	'1': BLUE,
	'2': GREEN,
	'3': BLUE,
	'4': RED,
	'5': '%s',
	'6': YELLOW,
	'7': GREY,
	'8': GREY,
	'9': BLUE,
	'a': PUKE,
	'b': BLUE,
	'c': ORANGE,
	'd': '%s',
	'e': YELLOW,
	'f': WHITE,
	'k': lambda s: '*' * len(s),
	'l': '**%s**',
	'm': '~%s~',
	'n': '__%s__',
	'o': '*%s*',
	'r': '%s'
}

# §


def minecraft_to_discord(minecraft):
	minecraft = '§r' + minecraft

	def f(match):
		code = match.group(1)
		text = match.group(2)
		format = formatting_codes[code]

		if isinstance(format, str):
			return format % text
		elif isinstance(format, tuple):
			return colorize(text, format)
		elif callable(format):
			return format(text)

	return re.sub('§(.)(.*)?', f, minecraft)


def optimizer(opt_goal, player, weapon_damage, base_str, base_cc, base_cd):
	best = 0
	best_route = []
	best_str = 0
	best_cc = 0
	best_cd = 0

	stat_modifiers = player.stat_modifiers()
	str_mod = stat_modifiers.get('strength', lambda x: x)
	cc_mod = stat_modifiers.get('crit chance', lambda x: x)
	cd_mod = stat_modifiers.get('crit damage', lambda x, y: x)

	counts = player.talisman_counts()

	if opt_goal == 1 or cc_mod(base_cc) > 100:
		for c, u, r, e, l in itertools.product(
				*[Route.routes(counts[key], 4, rarity_num) for rarity_num, key in enumerate(counts.keys())]):
			strength = str_mod(base_str + c.strength + u.strength +
							   r.strength + e.strength + l.strength)
			crit_damage = cd_mod(
				base_cd + c.crit_damage + u.crit_damage + r.crit_damage + e.crit_damage + l.crit_damage, strength)

			d = (5 + weapon_damage + strength // 5) * \
				 (1 + strength / 100) * (1 + crit_damage / 100)

			if d > best:
				best = d
				best_route = [c, u, r, e, l]
				best_str = strength
				best_cc = cc_mod(
					base_cc + c.crit_chance + u.crit_chance + r.crit_chance + e.crit_chance + l.crit_chance)
				best_cd = crit_damage
	else:
		cc_mod = stat_modifiers.get('crit chance', None)
		if cc_mod:
			for c, u, r, e, l in itertools.product(
					*[Route.routes(counts[key], 4, rarity_num) for rarity_num, key in enumerate(counts.keys())]):
				crit_chance = cc_mod(
					base_cc + c.crit_chance + u.crit_chance + r.crit_chance + e.crit_chance + l.crit_chance) // 1
				if crit_chance >= 100:
					strength = str_mod(base_str + c.strength + u.strength +
									   r.strength + e.strength + l.strength)
					crit_damage = cd_mod(
						base_cd + c.crit_damage + u.crit_damage +
							r.crit_damage + e.crit_damage + l.crit_damage,
						strength)

					d = (5 + weapon_damage + strength // 5) * \
						 (1 + strength / 100) * (1 + crit_damage / 100)

					if d > best:
						best = d
						best_route = [c, u, r, e, l]
						best_str = strength
						best_cc = crit_chance
						best_cd = crit_damage
		else:
			for c, u, r, e, l in itertools.product(
					*[Route.routes(counts[key], 4, rarity_num) for rarity_num, key in enumerate(counts.keys())]):
				crit_chance = base_cc + c.crit_chance + u.crit_chance + \
					r.crit_chance + e.crit_chance + l.crit_chance
				if crit_chance >= 100:
					strength = str_mod(base_str + c.strength + u.strength +
									   r.strength + e.strength + l.strength)
					crit_damage = cd_mod(
						base_cd + c.crit_damage + u.crit_damage +
							r.crit_damage + e.crit_damage + l.crit_damage,
						strength)

					d = (5 + weapon_damage + strength // 5) * \
						 (1 + strength / 100) * (1 + crit_damage / 100)

					if d > best:
						best = d
						best_route = [c, u, r, e, l]
						best_str = strength
						best_cc = crit_chance
						best_cd = crit_damage

	return best, best_route, best_str, best_cc, best_cd


class Route:
	def __init__(self, talismans, rarity):
		self.strength, self.crit_chance, self.crit_damage = [
			sum(reforges_list[y][rarity][x] * talismans[y]
				for y in range(len(reforges_list)) if reforges_list[y][rarity])
			for x in range(3)
		]
		self.counts = talismans
		self.rarity = rarity
		self.rarity_str = ["common", "uncommon",
			"rare", "epic", "legendary"][self.rarity]

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
	"""Yield successive n-sized chunks from lst."""
	lst = list(lst)
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
class Bot(discord.AutoShardedClient):
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
					},
					'invite': {
						'function': self.invite,
						'desc': 'Use this command to invite the bot to your server!'
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
					},
					'wiki': {
						'function': self.view_fandom_wiki,
						'desc': f'Displays [Skyblock Fandom Wiki](https://hypixel-skyblock.fandom.com) Article'
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

		self.loop.run_in_executor(None, update_trending)


	async def log(self, *args):
		print(*args, sep='')

	async def on_error(self, *args, **kwargs):
		error = traceback.format_exc().replace('```', '"""')
		await self.get_user(270352691924959243).send(f'```{error[-1900:]}```')
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
		dm = channel.type == discord.ChannelType.private

		if channel in self.hot_channels and self.hot_channels[channel] == user:
			return

		command = message.content[1:] if message.content.startswith('!') else message.content

		if command == f'<@!{self.user.id}>' or command == f'<@{self.user.id}>':
			await self.help(message)
			return

		command = re.split('\s+', command)
		command[0] = command[0].casefold()
		if command[0] == f'<@!{self.user.id}>' or command[0] == f'<@{self.user.id}>':
			command = command[1:]
		elif command[0] == prefix:
			command = command[1:]
		elif not dm:
			return

		if not command:
			return

		name = command[0].casefold()
		args = command[1:]

		if name not in self.callables:
			return

		# whitelisted_servers = [int(server)
		#							 for server in os.getenv('SERVERS').split()]
		# if not dm and not channel.guild.id in whitelisted_servers and len(channel.guild.members) > 50:
		#	  await Embed(
		#		  channel,
		#		  user=user,
		#		  title='Donate 20$ to my PayPal to use Skyblock Simplified on this server',
		#		  description='https://www.paypal.com/pools/c/8mstSPhQNO'
		#	  ).set_footer(
		#		  text='Free for servers under 50 members'
		#	  ).send()
		#	  await self.log('Paywal enforced in server {guild.name}')
		#	  return

		data = self.callables[name]
		security = data['security'] if 'security' in data else 0
		session = 'session' in data and data['session']
		function = data['function']

		if session and channel in self.hot_channels:
			await channel.send(
				f'{user.mention} someone else is currently using me in this channel! Try sending me a DM with your command instead')
			return

		if security == 1 and not channel.permissions_for(user).manage_messages:
			await channel.send(
				f'{user.mention} you do not have permission to use this command here! Try using it on your own discord server')
			return

		await self.log(f'{str(user)} used {name} {args} in {"a DM" if dm else channel.guild.name}')

		if session:
			self.hot_channels[channel] = user

		error = None

		try:
			await function(message, *args)
		except EndSession:
			await channel.send(f'{user.mention} session closed')
		except skypy.NeverPlayedSkyblockError:
			await Embed(
				channel,
				user=user,
				title='No Profiles!',
				description='This user has never played Skyblock'
			).send()
		except skypy.BadGuildError as e:
			await Embed(
				channel,
				user=user,
				description=f'Invalid guild name: {e.guild}'
			).send()
		except skypy.BadNameError as e:
			await Embed(
				channel,
				user=user,
				description=f'Invalid username: {e.uname_or_uuid}'
			).send()
		except skypy.HypixelError:
			await Embed(
				channel,
				user=user,
				title='Hypixel API Error!',
				description='The Hypixel API did not respond to your command'
			).set_footer(
				text='This error usually goes away after about a minute.\nIf not, the Hypixel API is down'
			).send()
		except skypy.ExternalAPIError as e:
			await Embed(
				channel,
				user=user,
				title='API Error!',
				description=str(e)
			).send()
		except discord.errors.Forbidden as e:
			if channel.permissions_for(channel.guild.me).send_messages:
				if channel.permissions_for(channel.guild.me).embed_links:
					await Embed(
						channel,
						user=user,
						title='Insufficient Permissions',
						description='I do not have permissions to do this. Try enabling your DMS or giving me admin'
					).send()
				else:
					await channel.send(
						'Insufficient Permissions: I do not have permissions to do this. Try enabling your DMS or giving me admin')
		except Exception as e:
			await Embed(
				channel,
				user=user,
				title='Error!',
				description='Something terrible happened while running your command\n'
				'The error has been automatically reported to SBS devs'
			).send()
			error = e

		if session:
			self.hot_channels.pop(channel)

		if error:
			raise error from None

	async def args_to_player(self, user, channel, *args):
		player = await skypy.Player(keys, uname=args[0], guild=True)

		if len(args) == 1:
			await player.set_profile_automatically()
		else:
			try:
				await player.set_profile(player.profiles[args[1].capitalize()])
			except KeyError:
				await channel.send(f'{user.mention} invalid profile!')
				return None

		# await update_top_players(player)

		return player

	async def no_args(self, command, user, channel):
		data = self.callables[command]
		usage = f'sbs {command} {data["args"]}' if 'args' in data else command

		await Embed(
			channel,
			user=user,
			title='This command requires arguments!',
			description=f'Correct usage is `{usage}`\n{self.args_message}'
		).send()

	async def current_auctions(self, message, *args):
		user = message.author
		channel = message.channel

		if not args:
			await self.no_args('current', user, channel)
			return

		player = await self.args_to_player(user, channel, *args)

		auctions = await player.auctions()

		if not auctions:
			await Embed(channel, user=user, title='no auctions found').send()

		async def pages(page_num):
			target = auctions[page_num]
			item = target['item']

			embed = Embed(
				channel,
				user=user,
				title=item.name
			).add_field(
				name=None,
				value=minecraft_to_discord(item.description)
			)

			return embed, page_num == len(auctions) - 1

		await self.book(user, channel, pages)

	async def royalty(self, message, *args):
		global db
		lb = db.leaderboards

		user = message.author
		channel = message.channel

		menu = {emoji: name for name, (emoji, _, _) in LEADERBOARDS.items()}

		current = 'Skill Average'
		while True:
			emoji, function, optional_function = LEADERBOARDS[current.casefold()]

			embed = Embed(
				channel,
				user=user,
				title=f'{current} Leaderboard',
				description=None
			)

			players = []

			cursor = lb.find().sort(current, -1).limit(30)

			i = 0
			if optional_function:
				for d in await cursor.to_list(length=None):
					players.append(f'#{str(i + 1).ljust(2)} {d["name"]} [{round(d[current + "_"], 3)}] [{round(d[current], 3)}]')
					i += 1
			else:
				for d in await cursor.to_list(length=None):
					players.append(f'#{str(i + 1).ljust(2)} {d["name"]} [{round(d[current], 3)}]')
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
			current = current.title()
			await msg.delete()

	async def price(self, message, *args):
		user = message.author
		channel = message.channel

		if not args:
			await self.no_args('price', user, channel)
			return

		if len(args) > 1 and args[-1].isdigit():
			if len(args[-1]) > 20:
				await channel.send(f'In what world would you need {args[-1]} of that???')
				return
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
		if size == 0:
			await channel.send(f'{user.mention} there haven\'t been any `{itemname}` sold recently')
			return

		small, big = min(auctions), max(auctions)
		mid = median(auctions)
		lower, upper = mid / 10, mid * 10

		steals = [a for a in auctions if lower >= a]
		auctions = [a for a in auctions if lower < a < upper]

		mid = median(auctions)
		avg = mean(auctions)
		common = mode(auctions)
		std = pstdev(auctions, mu=avg)

		await Embed(
			channel,
			user=user,
			title=f'{itemname} (x{stacksize})',
			description='Powered by https://hypixel-skyblock.com'
		).add_field(
			name=None,
			value=f'```Average: {avg:,.0f}\nMedian: {mid:,.0f}\nMode: {common:,.0f}\nStandard Deviation: {std:,.0f}\nMin: {math.ceil(small):,}\nMax: {math.ceil(big):,}```'
				  f'```There were {len(steals)} steals and {size} total sales```'
		).set_footer(
			text='Statistics are from the last 1500 items sold if possible\nPrices ignored if they are 10 times larger or smaller than the average'
		).send()

	async def sells(self, message, *args):
		page_size = 12

		user = message.author
		channel = message.channel

		if not args:
			await self.no_args('sells', user, channel)
			return

		name = args[0]
		_, uuid = await skypy.fetch_uuid_uname(name)

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
				user=user,
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
		_, uuid = await skypy.fetch_uuid_uname(name)

		async def pages(page_num):
			query = 'query UserHistory($id: String, $type: String, $limit: Int, $skip: Int) {userHistory(id: $id, type: $type, limit: $limit, skip: $skip) {auctions {id seller itemData {texture id name tag quantity lore __typename} bids {bidder timestamp amount __typename} highestBidAmount end __typename} __typename}}'
			r = await craftlink(user, channel, query, operation='UserHistory', id=uuid, limit=page_size, skip=page_num * page_size, type='purchases')
			if r is None:
				return
			r = r['userHistory']['auctions']

			if len(r) == page_size:
				last_page = True
			else:
				last_page = False

			embed = Embed(
				channel,
				user=user,
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

		player = await self.args_to_player(user, channel, *args)

		player.load_all(False)

		api_header = ' '.join(f'{k.capitalize()} {"✅" if v else "❌"}' for k, v in player.enabled_api.items())
		pet = player.pet
		pet_line = f'\nPet > {format_pet(pet)}' if pet else ''

		total_level = 0
		total_xp = 0
		for name, (emoji, function, optional_function) in LEVELS.items():
			if name in skills and not name in cosmetic_skills:
				total_level += optional_function(player)
				total_xp += function(player)

		embed = Embed(
			channel,
			user=user,
			title=f'{player.uname} | {player.profile_name}',
			description=f'```{api_header}```\n'
						f'```Deaths > {player.deaths}\n'
						f'Guild > {player.guild}\n'
						f'Money > {player.bank_balance + player.purse:,.0f}{pet_line}```'
		).add_field(
			name=f'🔰 \t Skills',
			value=f'''```diff
Avg > {player.skill_average:.2f}{"*" if player.uuid in EXPLOITERS else ""}
xp: {total_xp:,.0f}
{(total_level / (len(skills) - len(cosmetic_skills)) / 50 * 100):.1f}% Maxed```'''
		).add_field(
			name=f'🛠️ \t Minions',
			value=f'''```diff
Slots > {player.minion_slots}
Uniques: {player.unique_minions}
{(player.unique_minions / 572 * 100):.1f}% Maxed```'''
		).set_thumbnail(
			url=player.avatar()
		)

		def percent_to_max(current, activity):
			if activity == 'runecrafting':
				return 100 * min(1, current / skypy.runecrafting_xp_requirements[-1])

			if activity in skypy.slayers:
				return 100 * min(1, current / skypy.slayer_level_requirements[activity][-1])

			return 100 * min(1, current / skypy.skill_xp_requirements[-1])

		for name, (emoji, function, optional_function) in LEVELS.items():
			current = function(player)
			percent = percent_to_max(current, name.casefold())
			percent_line = '+ Maxed' if percent == 100 else f'{percent:.1f}% maxed'

			embed.add_field(
				name=f'{emoji}\t{name.capitalize()}',
				value=f'''```diff
Level > {optional_function(player)}
xp: {current:,}
{percent_line}```'''
			)

		if player.uuid in EXPLOITERS:
			embed.add_field(name='Cheater', value=f'***Player has bug abused or excessively macroed skill(s)**', inline=False)

		await embed.send()

	async def pets(self, message, *args):
		user = message.author
		channel = message.channel

		if not args:
			await self.no_args('pets', user, channel)
			return

		player = await self.args_to_player(user, channel, *args)

		player.load_pets()

		pets = '\n'.join(p.name for p in player.pets)

		if player.pets:
			best_pets = {}
			pet_score = 0
			bonus_mf = 0
			chunk_num = 0
			for chunk in chunks(sorted(player.pets, key=lambda pet: (pet.active, pet.xp), reverse=True), 18):
				chunk_num += 1
				embed = Embed(
					channel,
					user=user,
					title=f'{player.uname} | {player.profile_name}'
				).set_thumbnail(
					url=player.avatar()
				)
				for pet in chunk:
					if best_pets.get(pet.internal_name, False):
						if RARITY_SCORES[pet.rarity] > best_pets[pet.internal_name]:
							best_pets[pet.internal_name] = RARITY_SCORES[pet.rarity]
					else:
						best_pets[pet.internal_name] = RARITY_SCORES[pet.rarity]
					progress = 100 * pet.xp / (pet.xp + pet.xp_remaining)
					progress = f'\n{progress:.2f}% to 100' if progress < 100 else ''

					value = colorize(
						f'Level > {pet.level}\nxp: {pet.xp:,.0f}{progress}',
						YELLOW if pet.active else WHITE
					)

					pin = '\t📌' if pet.active else ''
					embed.add_field(
						name=f'{PET_EMOJIS[pet.internal_name]}\t{pet.name}{pin}',
						value=value + colorize(pet.rarity.upper(), RARITY_COLORS[pet.rarity])
					)
				if chunk_num - 1 == len(player.pets) // 18:
					for x in best_pets:
						pet_score += best_pets[x]
					for x in [10,25,50,85,125]:
						bonus_mf += 1 if pet_score >= x else 0
					embed.add_field(
						name=f'Pet Score',
						value=f'You gain {pet_score} points from {len(best_pets)} types. (+{bonus_mf} Magic Find)',
						inline=False
					)
				await embed.send()
		else:
			embed.add_field(name=None, value='```❌ no pets found```')
			await embed.send()

	async def guild(self, message, *args):
		user = message.author
		channel = message.channel

		if not args:
			await self.no_args('guild', user, channel)
			return

		args = ' '.join(args).casefold()

		guild = await skypy.Guild(keys, gname=args)
		guild.load_all(False)
		await asyncio.gather(*[update_top_players(player) for player in guild])

		embed = Embed(
			channel,
			user=user,
			title=f'{guild.gname} | {guild.tag}' if guild.tag else guild.gname,
			description=f'```Skill Average > {guild.skill_average:.3f}\n'
						f'Players > {len(guild)}\n'
						f'Level > {guild.level}\n'
						f'Deaths > {guild.deaths:,}\n'
						f'Average Money > {(guild.bank_balance + guild.purse) / len(guild):,.0f}\n'
						f'Slots > {guild.minion_slots:.3f} ({guild.unique_minions:.0f} crafts)```'
		)

		for name, (emoji, function, optional_function) in LEVELS.items():
			embed.add_field(
				name=f'{emoji}\t{name.title()}',
				value=f'```Level > {optional_function(guild):.3f}\nxp: {function(guild):,.0f}```'
			)

		menu = {}
		prompt = {}
		for name, (emoji, function, optional_function) in LEADERBOARDS.items():
			lb = Embed(
				channel,
				user=user,
				title=f'{guild.gname} {name.title()} Leaderboard'
			)

			if optional_function:
				players = [(player, function(player), optional_function(player)) for player in guild]
			else:
				players = [(player, function(player)) for player in guild]

			players.sort(key=lambda tuple: tuple[1], reverse=True)

			if optional_function:
				players = [f'#{str(index + 1).ljust(2)} {player.uname} [{round(optional_stat, 2)}] [{round(stat, 2):,}]'
						   for index, (player, stat, optional_stat) in enumerate(players)]
			else:
				players = [f'#{str(index + 1).ljust(2)} {player.uname} [{round(stat, 2):,}]'
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

			msg = msg.content.casefold()

			player = await skypy.Player(keys, uname=msg)
			if len(player.profiles) == 0:
				await embed(
					channel,
					user=user,
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

		if len(player.profiles) == 1:
			await player.set_profile(list(player.profiles.values())[0])

		else:
			embed = Embed(
				channel,
				user=user,
				title='Which profile would you like to use?',
				description='**[Sorted by date created]**'
			).add_field(
				name=None,
				value='\n\n'.join(f'> {PROFILE_EMOJIS[profile]}\n`{profile}`' for profile in player.profiles.keys())
			)

			result = await self.reaction_menu(await embed.send(), user, {PROFILE_EMOJIS[profile]: profile for profile in player.profiles.keys()})
			await player.set_profile(player.profiles[result])

		player.load_inventories().load_skills_slayers().load_misc().load_pets()

		if player.enabled_api['skills'] is False or player.enabled_api['inventory'] is False:
			await self.api_disabled(f'{user.name}, your API is disabled!', channel, user)
			return

		if len(player.weapons) == 0:
			await channel.send(f'{user.mention}, you have `no weapons` in your inventory. If you have any items in your inventory or backpacks with no rarity, this will stop sbs from finding your weapons. If you do not have any, DM uwu your profile.')
			return

		if len(player.weapons) == 1:
			weapon = player.weapons[0]
		else:
			valid = False

			while valid is False:
				await Embed(
					channel,
					user=user,
					title='Which weapon would you like to use?'
				).set_footer(
					text='You may use either the weapon name or the weapon number'
				).add_field(
					name=None,
					value=''.join([f'```{i + 1} > ' + weapon.name + '```' for i, weapon in enumerate(player.weapons)])
				).send()

				msg = (await self.respond(user, channel)).content.casefold()

				names = [weapon.name.casefold() for weapon in player.weapons]

				if msg in names:
					weapon = player.weapons[names.index(msg)]
					valid = True
				else:
					try:
						weapon = player.weapons[int(msg) - 1]
						valid = True
					except (IndexError, TypeError, ValueError):
						await channel.send(f'Invalid weapon! Did you make a typo?{CLOSE_MESSAGE}')

		pet = player.pet

		embed = Embed(
			channel,
			user=user,
			title='Is this the correct equipment?'
		).add_field(
			name=f'⚔️\tWeapon',
			value=f'```{weapon.name}```',
			inline=False
		).add_field(
			name=f'{PET_EMOJIS[pet.internal_name] if pet else "🐣"}\tPet',
			value=f'```{format_pet(pet) if pet else None}```',
			inline=False
		)

		for piece, emoji in [('helmet', '⛑️'), ('chestplate', '👚'), ('leggings', '👖'), ('boots', '👞')]:
			embed.add_field(
				name=f'{emoji}\t{piece.capitalize()}',
				value='```' + str(next((a.name for a in player.armor if a.type == piece), None)) + '```',
				inline=False
			)

		embed.add_field(
			name='🏺\tTalismans',
			value=''.join(
				colorize(
					f'{amount} {Route.rarity_grammar(name).capitalize()}',
					RARITY_COLORS[name]
				)
				for name, amount in player.talisman_counts().items())
		)

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

		potion_cc = stats['crit chance']

		optimizers = [
			('💯', 'perfect crit chance'),
			('⚔️', 'maximum damage')
		]

		embed = Embed(
			channel,
			user=user,
			title='You are almost done!'
		).add_field(
			name='What would you like to optimize for?',
			value='\n\n'.join(f'> {emoji}\n`{value}`' for emoji, value in optimizers)
		)

		optimizers = {emoji: index for index, (emoji, _) in enumerate(optimizers)}
		opt_goal = await self.reaction_menu(await embed.send(), user, optimizers)

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
		if pet:
			apply_stats(pet.stats())
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

		# print(*(f"({n} {v})" for n, v in locals().items()))

		best, best_route, best_str, best_cc, best_cd = await self.loop.run_in_executor(None,
			optimizer,
			opt_goal,
			player,
			weapon_damage,
			base_str,
			base_cc,
			base_cd
		)

		if not best_route:
			await Embed(
				channel,
				user=user,
				title='There is no possible setup that will give you 100% crit chance',
				description='Collect more talismans or raise your combat level before trying again'
			).send()
			return

		embed = Embed(
			channel,
			user=user,
			title='Success!'
		)
		for route, color in zip(best_route, [GRAY, GREEN, BLUE, ORANGE, YELLOW]):
			if str(route):
				embed.add_field(
					name=f'**{route.rarity_str.title()}**',
					value=colorize(route, color),
					inline=False
				)
			else:
				embed.add_field(
					name=f'**{route.rarity_str.title()}**',
					value=r'```¯\_(ツ)_/¯```',
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
			value=f'```{cur_str:.0f} strength\n{cur_cd:.0f} crit damage\n{cur_cc - potion_cc:.0f} crit chance```'
				  f'```{zealot_damage:,.0f} to zealots\n{slayer_damage:,.0f} to slayers```'
		)

		embed.add_field(
			name='**After**',
			value=f'```{best_str:.0f} strength\n{best_cd:.0f} crit damage\n{best_cc - potion_cc:.0f} crit chance```'
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

			if resp.content[0] == '+':
				resp.content = resp.content[1:]

			if resp.content.isdigit() is False or len(resp.content) > 20:
				await channel.send(f'{user.mention} Invalid input!')
				return
			stats[stat] = int(resp.content)

		mobs = '\n'.join([k.capitalize() for k in ACTIVITIES.keys()])

		embed = Embed(
			channel,
			user=user,
			title='Which mob will you be targeting with this setup?'
		).add_field(
			name=None,
			value=f'```{mobs}```',
		)

		while True:
			await embed.send()

			resp = (await self.respond(user, channel)).content.casefold()

			if resp in ACTIVITIES:
				break
			else:
				await channel.send(f'{user.mention} choose one of the listed enemies{CLOSE_MESSAGE}')

		msg = await channel.send(
			f'{user.mention} do you want to use **level 5** or **level 6** enchantments? **[react to this message]**')
		enchant_levels = await self.reaction_menu(msg, user, {'5️⃣': CHEAP_MAX_BOOK_LEVELS, '6️⃣': MAX_BOOK_LEVELS})

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
			user=user,
			title=f'{user.name}, you should be doing {damage} damage with those stats'
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

		player = await self.args_to_player(user, channel, *args)

		player.load_inventories()

		if player.enabled_api['inventory'] is False:
			await self.api_disabled(f'{player.uname}, your inventory API is disabled on {player.profile_name.title()}!', channel, user)
			return

		talismans = skypy.talismans.copy()
		for talisman in player.talismans:
			if talisman.active:
				for regex in skypy.talismans.keys():
					if regex.match(talisman.internal_name):
						talismans.pop(regex)

		embed = Embed(
			channel,
			user=user,
			title=f'{user.name}, you are missing {len(talismans)}/{len(skypy.talismans)} talisman{"" if len(talismans) == 1 else "s"}!',
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
				value='```' + '\n'.join(map(str, inactive)) + '``````An unnecessary talisman is any talisman is\nduplicated or part of a talisman family```'
			)

		await embed.send()

	async def help(self, message, *args):
		user = message.author
		channel = message.channel

		dm = user.dm_channel or await user.create_dm()

		embed = Embed(
			dm,
			user=user,
			title='Skyblock Simplified',
			description='Welcome to Skyblock Simplified, a Skyblock bot designed to streamline gameplay\n[Click me](https://discord.com/oauth2/authorize?client_id=671040150251372569&permissions=8&scope=bot) to invite the bot to your server\n'
						f'**React to this message with any of the emojis to view commands**\n{self.args_message}\n'
		).set_footer(
			text='Skyblock Simplified for Hypixel Skyblock | Created by notnotmelon#7218'
		)

		for category, data in self.commands.items():
			embed.add_field(
				name=f'{data["emoji"]}	{category}',
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
				user=user,
				title=category.capitalize(),
				description=f'{self.args_message}\n```{category_data["desc"]}```'
			).add_field(
				name=None,
				value='\n\n'.join([command_desc(name, data) for name, data in category_data['commands'].items()])
			).set_footer(
				text='Skyblock Simplified for Hypixel Skyblock | Created by notnotmelon#7218'
			)

		if channel.type != discord.ChannelType.private:
			await channel.send(f'Sent you a DM with the information {user.mention}!')

		while True:
			msg = await embed.send()

			box = await self.reaction_menu(msg, user, boxes)
			if await self.back(await box.send(), user) is False:
				return

	async def stats(self, message, *args):
		channel = message.channel
		user = message.author

		server_rankings = sorted(self.guilds, key=lambda guild: len(guild.members), reverse=True)[:10]
		server_rankings = f'{"Top Servers".ljust(28)} | Users\n' + '\n'.join(
			[f'{guild.name[:28].ljust(28)} | {len(guild.members)}' for guild in server_rankings])

		_embed = Embed(
			channel,
			user=user,
			title='Discord Stats',
			description=f'This Command was run on shard {(message.guild.shard_id if message.guild else 0) + 1} / {self.shard_count}\n```{server_rankings}```'
		).add_field(
			name='Servers',
			value=f'{self.user.name} is running in {len(self.guilds)} servers with {sum(len(guild.text_channels) for guild in self.guilds)} channels',
			inline=False
		).add_field(
			name='Users',
			value=f'There are currently {sum(len(guild.members) for guild in self.guilds)} users with access to the bot',
			inline=False
		)
		shards = []
		for x in range(self.shard_count): shards.append([0,0,0])
		for x in self.guilds:
			shards[x.shard_id][0] += 1
			shards[x.shard_id][1] += len(x.text_channels)
			shards[x.shard_id][2] += len(x.members)
		for x in range(self.shard_count):
			_embed.add_field(
				name=f'Shard {x + 1}',
				value=f'''{shards[x][0]} servers
{shards[x][1]} channels
{shards[x][2]} members''',
				inline=True
				)
		_embed.add_field(
			name='Heartbeat',
			value=f'This message was delivered in {self.latency * 1000:.0f} milliseconds',
			inline=False
		)
		await _embed.send()

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
			raise EndSession
		if msg.content.casefold() == 'exit':
			raise EndSession

		return msg

	async def reaction_menu(self, message, user, reactions, edit=False):
		if edit:
			await message.clear_reactions()

		for reaction in reactions.keys():
			await message.add_reaction(reaction)

		check = lambda reaction, u: u == user and reaction.message.id == message.id and str(reaction) in reactions

		try:
			reaction, _ = await self.wait_for('reaction_add', check=check, timeout=45)
			return reactions[str(reaction)]
		except asyncio.TimeoutError:
			for reaction in reactions.keys():
				await message.remove_reaction(reaction, self.user)
			for reaction in ['🇹', '🇮', '🇲', '🇪', '🇴', '🇺', '✝️']:
				await message.add_reaction(reaction)
			raise EndSession

	async def back(self, message, user):
		return True if await self.reaction_menu(message, user, {'⬅️': True}) else False

	async def yesno(self, message, user):
		return await self.reaction_menu(message, user, {'✅': True, '❌': False})

	async def book(self, user, channel, pages):
		page_num = 0
		backward = {'⬅️': -1}
		forward = {'➡️': 1}
		both = {'⬅️': -1, '➡️': 1}

		if channel.type != discord.ChannelType.private and channel.guild.me.permissions_in(channel).manage_messages:
			r = await pages(page_num)
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
				page_num += result

				r = await pages(page_num)
				embed, last_page = r

				await msg.edit(embed=embed)
		else:
			while True:
				r = await pages(page_num)
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
				await msg.delete()
				page_num += result

	async def view_trending(self, message, *args):
		channel = message.channel
		user = message.author

		embed = Embed(
			channel,
			user=user,
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

	async def view_fandom_wiki(self, message, *args):
		channel = message.channel
		user = message.author
			
		url = 'https://hypixel-skyblock.fandom.com/wiki/' + ('_'.join(args) or 'Hypixel_SkyBlock_Wiki')
		
		async with (await skypy.session()).get(url, headers={'User-Agent': 'Mozilla/5.0'}) as code:
			code = await code.read()
			soup = BeautifulSoup(code.decode('utf-8'), 'lxml')
		title = None
		
		for x in soup.select('h1'):
			if 'page-header__title' in x.get('class', []):
				title = x.text
				
		image = None
		for x in soup.select('img'):
			if 'pi-image-thumbnail' in x.get('class', []):
				image = x.get('src')
				break
				
		for x in soup.select('aside'):
			if 'portable-infobox' in x.get('class', []):
				x.decompose()
				
		description = None
		for x in soup.select('p'):
			description = x.text
			if 'not found. What do you want to do?' in description:
				for x in soup.select('span'):
					if 'alternative-suggestion' in x.get('class', []):
						article = fandom_wiki(x.text)
						title = article.title
						description = article.description
						image = article.image
						return
						
			elif 'What do you want to do?' in description:
				description = f'Not found'
				break
				
			elif 'caption' in x.get('class', []):
				description = None
				
			elif 'category-page__total-number' in x.get('class', []):
				try:
					description = f'This category has no information, but {x.text.split("(")[1].split(")")[0]} articles are in the category.'
				except IndexError:
					description = 'This category has no information.'
				break
				
			else:
				break
				
		if description is None:
			if name.split(":")[0] == title:
				description = f'Not found'
			else:
				description = f'could not find the {name.split(":")[0]} named {title}.'

		embed = Embed(
			channel,
			user=user,
			title=title,
			description=description
		).set_footer(
			text=f'CC BY-SA-NC 3.0 https://hypixel-skyblock.fandom.com'
		)
		if image:
			embed.set_image(image)

		await embed.send()

	async def api_disabled(self, title, channel, user):
		await Embed(
			channel,
			user=user,
			title=title,
			description='Re-enable them with [skyblock menu > settings > api settings]'
		).set_footer(
			text='Sometimes this message appears even if your API settings are enabled. If so, exit Hypixel and try again. It\'s also possible that Hypixel\'s API servers are down'
		).send()

	async def support_server(self, message, *args):
		await Embed(
			message.channel,
			user=message.author,
			title='Here\'s a link to my support server',
			description='[https://discord.gg/sbs]'
		).set_footer(
			text='(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧'
		).send()

	async def invite(self, message, *args):
		await Embed(
			message.channel,
			user=message.author,
			title='Here\'s an invite link',
			description='[Click me to invite the bot](https://discord.com/oauth2/authorize?client_id=671040150251372569&permissions=8&scope=bot)'
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
	except asyncio.exceptions.TimeoutError:
		await channel.send(f'{user.mention} {url} did not respond after 30 seconds')
		return None
	except (ClientError, ValueError):
		await channel.send(f'{user.mention} {url} did not respond')
		return None

client = motor.motor_asyncio.AsyncIOMotorClient(os.getenv('DATABASE_URI'))
db = client.sbs

async def update_top_players(player):
	global db
	lb = db.leaderboards

	player.load_skills_slayers(False).load_collections(False)

	try:
		if player.uuid in EXPLOITERS:
			for offence in EXPLOITERS[player.uuid]:
				player.skills[offence] *= -1
			player.skill_average = sum(list(player.skills.values())[0:7]) / 7

		document = {
			'name': player.uname,
			'uuid': player.uuid
		}

		for name, (emoji, function, optional_function) in LEADERBOARDS.items():
			document[name.title()] = function(player)
			if optional_function:
				document[f'{name.title()}_'] = optional_function(player)
	except AttributeError:
		await Bot.log(f'Failed to add {player.uname} to leaderboards')
		return

	await lb.replace_one({'uuid': player.uuid}, document, upsert=True)
	await Bot.log(f'Leaderboard updated for {player.uname}')

# Forums parsing ---
trending_threads = []
last_forums_update = datetime.now()
num_trending = 6
trending_timeout = int(os.getenv('TRENDING_TIMEOUT', 30))

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
				loop.run_until_complete(Bot.log(f'Attempting to parse forums page {pagenumber}'))

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
			loop.run_until_complete(Bot.log(
				f'Trending threads updated at {now.strftime(TIME_FORMAT)}. {pagenumber} pages parsed\n',
				'\n'.join([thread['link'] for thread in trending_threads])
			))

		except (Nothing, RuntimeError):
			now = datetime.now(timezone.utc)
			loop.run_until_complete(Bot.log(f'Failed to parse forums at {now.strftime(TIME_FORMAT)}'))
			trending_threads = backup

		loop.run_until_complete(asyncio.sleep(3600 * 2))

discord.Embed = None  # Disable default discord Embed
