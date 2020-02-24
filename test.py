import skypy
import skypy_constants
import asyncio
import os
from pprint import pprint

if os.environ.get('API_KEY') is None:
    import dotenv
    dotenv.load_dotenv()
	
keys = os.getenv('API_KEY').split()

async def main():
	player = await skypy.Player(keys, uname='oddipoddi')
	await player.set_profile(list(player.profiles.values())[0])
	for item in player.armor:
		pprint(item.__nbt__)
		print(item.stats())
		print(item.stats(use_reforge=False))
		print('\n--------------------------------\n')

try:
	asyncio.run(main())
except Exception as e:
	print(e)
	
input()