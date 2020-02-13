'''
What's new in version 5?
Skyblock API support :o
Talisman optimizer is now a Discord bot :o
Tarantula helmet support :o
Potion support :o
Superior support
Mastiff support
Fishing rod support
Major speed and memory improvements
'''

import os
import discord
import skypy
import traceback
from itertools import product, chain
import math

if os.environ.get('API_KEY') is None:
	import dotenv
	dotenv.load_dotenv()

env = os.getenv('ENV')
print(env)
api_key = os.getenv('API_KEY')

notnotmelon = 270352691924959243
Plutie = 181152738086748160

damaging_potions = [
	{'name': 'critical', 'stats': {'crit chance': [
		0, 10, 15, 20, 25], 'crit damage': [0, 10, 20, 30, 40]}},
	{'name': 'strength', 'stats': {'strength': [
		0, 5.25, 13.125, 21, 31.5, 42, 52.5, 63, 78.75]}},	# Assume cola
	{'name': 'spirit', 'stats': {'crit damage': [0, 10, 20, 30, 40]}},
	{'name': 'archery', 'stats': {
		'enchantment modifier': [0, 13.125, 26.25, 52.5, 78.75]}}
]

# list of all enchantment powers per level. can be a function or a number
enchantment_values = {
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

# list of relevant enchants for common mobs
activities = {
	'Slayer Bosses': [
		'giant_killer',
		'sharpness',
		'power',
		'spiked_hook',
		'smite',
		'bane_of_arthropods',
		'execute'
	],
	'Dragons': [
		'giant_killer',
		'sharpness',
		'power',
		'spiked_hook',
		'ender_slayer',
		'execute',
		'dragon_hunter',
		'snipe'
	],
	'Zealots': [
		'giant_killer',
		'sharpness',
		'power',
		'spiked_hook',
		'ender_slayer',
		'first_strike'
	],
	'Sea Creatures': [
		'giant_killer',
		'sharpness',
		'power',
		'spiked_hook',
		'first_strike',
		'impaling'
	],
	'Players': [
		'giant_killer',
		'sharpness',
		'power',
		'spiked_hook',
		'execute',
		'snipe'
	],
	'Magma Boss': [
		'giant_killer',
		'sharpness',
		'power',
		'spiked_hook',
		'cubism',
		'execute',
		'snipe'
	],
	'Horseman': [
		'giant_killer',
		'sharpness',
		'power',
		'spiked_hook',
		'execute',
		'snipe'
	],
	'Other': [
		'giant_killer',
		'sharpness',
		'power',
		'spiked_hook',
		'smite',
		'bane_of_arthropods',
		'first_strike'
	]
}

relavant_reforges = {
	'forceful': (None, None, (7, 0, 0), (10, 0, 0), (15, 0, 0)),
	'itchy': ((1, 0, 3), (2, 0, 5), (2, 0, 8), (3, 0, 12), (5, 0, 15)),
	# 'unpleasant': ((0, 1, 1), None, (0, 3, 2), (0, 6, 3), (0, 8, 5)), -- too laggy not worth keeping
	'strong': (None, None, (4, 0, 4), (7, 0, 7), (10, 0, 10)),
	'godly': ((1, 1, 1), (2, 2, 2), (4, 2, 3), (7, 3, 6), (10, 5, 8))
}
reforges_list = list(relavant_reforges.values())


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

	def __repr__(self):
		return ', '.join([f'{c} '
						  f'{"godly/zealous" if self.rarity < 2 and name == "godly" else name} '
						  f'{rarity_grammar(self.rarity_str, c)}'
						  for name, c in zip(relavant_reforges.keys(), self.counts) if c != 0])


def rarity_grammar(rarity, count=0):
	# I really did have to bring the grammar. You know how it goes
	if count == 1:
		return rarity
	return f'{rarity[:-1]}ies' if rarity[-1] == 'y' else f'{rarity}s'


'''
from lang import *

server_languages = {
	652148034448261150: {
		657398578431393852: english,
		658711562143662080: french,
		658711589511233557: german,
		658711683790929950: spanish,
		658711612235972629: polish,
		659950470785138737: hebrew,
		671767272418967563: russian,
		671768786147213322: czech
	},	# main server
	# sb hispanic
	651266868685832193: {'channel': 652329734201540620, 'language': spanish},
	# skyborn
	604420816817356822: {'channel': 657439787053219842, 'language': english},
	# altpapier
	554389777055612949: {'channel': 657532302988935170, 'language': german},
	# sb fr
	636691537673060430: {'channel': 658070418938134568, 'language': french},
	# axegaming
	650438966041903115: {'channel': 650439295894683681, 'language': french}
}

channel_whitelist = list(chain.from_iterable([lang['channel']] if 'channel' in lang else list(
	lang.keys()) for lang in server_languages.values()))
'''


class Bot(discord.Client):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.sessions = {}
		self.last_warning = None

	async def log(self, *message):
		print(*message)
		await self.log_channel.send(' '.join(message))

	async def on_ready(self):
		self.log_channel = self.get_channel(654753097897213953)
		self.notnotmelon = self.get_user(notnotmelon)
		self.Plutie = self.get_user(Plutie)
		print(f'Logged on as {self.user}!')

		self.commands = {
			'stats': {
				'security': 0,
				'command': self.stats,
				'desc': 'Displays stats about the bot including number of servers and users'
			},
			'start event': {
				'category': 'skill events',
				'security': 1,
				'command': self.start_event,
				'desc': 'Starts a skyblock event'
			},
			'view leaderboard': {
				'category': 'skill events',
				'security': 0,
				'command': self.view_lb,
				'desc': 'Displays the leaderboard for the current event'
			},
			'end event': {
				'category': 'skill events',
				'security': 1,
				'command': self.end_event,
				'desc': 'Ends the current event and displays the winners'
			},
			'talisman optimizer': {
				'category': 'talisman',
				'security': 0,
				'command': self.optimize_talismans,
				'desc': 'Optimizes your talismans to their best reforges'
			},
			'view missing talismans': {
				'category': 'talisman',
				'security': 0,
				'command': self.view_missing_talismans,
				'desc': 'Displays a list of a players missing talismans'
			},
			'': {
				'security': 0,
				'command': self.help
			},
			'help': {
				'security': 0,
				'command': self.help,
				'desc': 'Opens the menu that you are looking at now'
			}
		}

		def command_desc(name, data):
			moderators = "\n\t - Can only be used by moderators" if data["security"] == 1 else ""
			return f'{self.user.mention} {name}\n > {data["desc"]}{moderators}'

		fields = {}
		for name, data in self.commands.items():
			if 'desc' in data:
				if 'category' not in data:
					data['category'] = '\u200b'
				if data['category'] in fields:
					fields[data['category']
						] += f'\n\n{command_desc(name, data)}'
				else:
					fields[data['category']] = command_desc(name, data)

		self.help_embed = discord.Embed.from_dict({
			'title': 'Hypixel Skyblock',
			'description': 'Welcome to notnotmelon\'s multipurpose Discord bot for Hypixel Skyblock.\n'
			'Use any of the commands below to get started',
			'fields': [{'name': name, 'value': value} for name, value in fields.items()],
			'footer': {'text': 'Discord Bot for Hypixel Skyblock | Created by notnotmelon#7218'}
		})

	async def on_message(self, message):
		user = message.author

		if user.bot:
			return

		if message.channel != user.dm_channel and self.user.mention not in message.mentions:
			return
		'''if env == 'local' and user != self.notnotmelon:
			await message.channel.send('I am down for updates right now, please check back later')
			return
		'''
		for name, command in self.commands.items():
			if message.content.lower().endswith(name):
				if command['security'] == 1 and not user.ban_members:
					await message.channel.send('You do not have permission to use this command here! Try using it on your own discord server')
				else:
					await command['command'](message)
				break

	async def optimize_talismans(self, message):
		pass

	async def view_missing_talismans(self, message):
	player = self.query_player(message)

	async def help(self, message):
		if message.channel != message.author.dm_channel:
		await message.channel.send(f'Sent you a DM with information {message.author.mention}!')
		await message.author.send(embed=self.help_embed)

	async def stats(self, message):
		await message.channel.send(embed=discord.Embed(
			title='Hypixel Skyblock Discord Stats'
		).add_field(
			name='Servers',
			value=f'The Hypixel Skyblock bot is running in {len(self.guilds)} with {sum([len(guild.text_channels) for guild in self.guilds])}'
		).add_field(
			name='Users',
			value=f'There are currently {sum([len(guild.members) for guild in self.guilds])} users with access to the bot'
		))

		async def query_player(self, user, channel):
				def check(message):
						return message.channel == channel and message.author == user

				valid = False

				while valid is False:
						await channel.send('What is your Minecraft username?')
						msg = await self.wait_for('message', check=check).lower()

						try:
								player = skypy.Player(keys, uname=msg)
								if len(player.profiles) == 0:
										await channel.send('You have no profiles? Please report this')

								else:
										valid = True

						except skypy.NeverPlayedSkyblockError:
								await channel.send('You have never played skyblock')
								return await self.ask_uname(message)

						except skypy.SkyblockError:
								await channel.send('Invalid username')
								return await self.ask_uname(message)

		if len(player.profiles) == 1:
			player.set_profile(list(player.profiles.values())[0])

		else:
			await channel.send(embed=discord.Embed(
				title='Which profile do you want to use?',
				description='Sorted by date created'
			).add_field(
				name='\u200b',
				value='\n\n'.join(player.profiles.keys())
			))

			valid = False

			while valid is False:
							msg = await self.wait_for('message', check=check).lower()

				if msg in player.profiles:
					player.set_profile(player.profiles[msg])
					valid = True

				else:
					channel.send('Invalid profile! Did you make a typo?')

		return player

client = Bot()
print(os.getenv('DISCORD_TOKEN')
client.run(api_key)