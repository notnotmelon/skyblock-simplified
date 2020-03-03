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
	'''
	player = await skypy.Player(keys, uname='oddipoddi')
	await player.set_profile(list(player.profiles.values())[0])
	for item in player.armor:
		pprint(item.__nbt__)
		print(item.stats())
		print(item.stats(use_reforge=False))
		print('\n--------------------------------\n')
	'''
	pprint(skypy.decode_inventory_data('H4sIAAAAAAAAAFWPsU7DMBRFr9OWJh6KkJAY8RcwsMBaBUgQbVIVWFjQA1vBwo0j2wH6RfmPfFiFGVmPzj3S5UAGpjkAliDRkr0wzHLbt4FxTAI1E2SllurOUOOjdeCYS+07Q/sM05V1Ko10hvNxuHpy9KWMIBfnUuhW+LA3SvRetw3OohA+tBeFo64zEYnS2s8LnI7D9aV4VO82jnJrjbTfbWwuxoHGwTxXeb1e11WKaUU7hZOI/yfAcXz7ExwtQ3D6rQ/Kp39XsCi2y81mdV8Vr2VdPwAJjm5oR42KefwCgrOR1/sAAAA=')[0].__nbt__)

try:
	asyncio.run(main())
except Exception as e:
	print(e)
	
input()