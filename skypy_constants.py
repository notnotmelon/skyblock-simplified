sword_enchants = [
    'sharpness',
    'critical',
    'ender_slayer',
    'execute',
    'first_strike',
    'giant_killer',
    'lethality',
    'life_steal',
    'looting',
    'luck',
    'scavenger',
    'vampirism',
    'bane_of_arthropods',
    'smite',
    'dragon_hunter'
]

bow_enchants = [
    'power',
    'aiming',
    'dragon_hunter',
    'infinite_quiver',
    'power',
    'snipe',
    'punch',
    'flame',
    'piercing'
]

rod_enchants = [
    'angler',
    'blessing',
    'caster',
    'frail',
    'luck_of_the_sea',
    'lure',
    'magnet',
    'looting'
]

skill_rewards = {
    'foraging': {
        0: {
            'strength': 1
        },
        15: {
            'strength': 2
        }
    },
    'combat': {
        0: {
            'crit chance': 1,
            'ench modifer': 4
        }
    }
}

talismen = {
    'FARMING_TALISMAN': 'Farming Talisman',
    'VACCINE_TALISMAN': 'Vaccine Talisman',
    'SPEED_TALISMAN': 'Speed Talisman',
    'WOOD_TALISMAN': 'Wood Affinity Talisman',
    'SKELETON_TALISMAN': 'Skeleton Talisman',
    'COIN_TALISMAN': 'Talisman of Coins',
    'MAGNETIC_TALISMAN': 'Magnetic Talisman',
    'GRAVITY_TALISMAN': 'Gravity Talisman', 
    'VILLAGE_TALISMAN': 'Village Affinity Talisman',
    'MINE_TALISMAN': 'Mine Affinity Talisman',
    'NIGHT_VISION_CHARM': 'Night Vision Charm',
    'LAVA_TALISMAN': 'Lava Talisman',
    'SCAVENGER_TALISMAN': 'Scavenger Talisman', 
    'WOLF_PAW': 'Wolf Paw',
    'FIRE_TALISMAN': 'Fire Talisman',    
    'BROKEN_PIGGY_BANK': 'Broken Piggy Bank',
	'CRACKED_PIGGY_BANK': 'Cracked Piggy Bank',
    'PIGGY_BANK': 'Piggy Bank',
    'PIGS_FOOT': 'Pig\'s Foot', 
    'FROZEN_CHICKEN': 'Frozen Chicken',
    'FISH_AFFINITY_TALISMAN': 'Fish Affinity Talisman',
    'FARMER_ORB': 'Farmer Orb',
    'HASTE_RING': 'Haste Ring',
    'NEW_YEAR_CAKE_BAG': 'New Year Cake Bag',
    'NIGHT_CRYSTAL': 'Night Crystal', 
	'DAY_CRYSTAL': 'Day Crystal',
    'FEATHER_ARTIFACT': 'Feather Artifact',
    'ARTIFACT_POTION_AFFINITY': 'Potion Affinity Artifact',
    'HEALING_RING': 'Healing Ring', 
    'CANDY_ARTIFACT': 'Candy Artifact',
    'EXPERIENCE_ARTIFACT': 'Experience Artifact',
    'MELODY_HAIR': '♪ Melody\'s Hair ♪',
    'SEA_CREATURE_ARTIFACT': 'Sea Creature Artifact',
    'INTIMIDATION_ARTIFACT': 'Intimidation Artifact',
    'WOLF_RING': 'Wolf Ring',
    'BAT_ARTIFACT': 'Bat Artifact',
    'DEVOUR_RING': 'Devour Ring',
    'ZOMBIE_ARTIFACT': 'Zombie Artifact',
    'SPIDER_ARTIFACT': 'Spider Artifact',
    'ENDER_ARTIFACT': 'Ender Artifact',
    'TARANTULA_TALISMAN': 'Tarantula Talisman',
    'SURVIVOR_CUBE': 'Survivor Cube',
    'WITHER_ARTIFACT': 'Wither Artifact',
    'WEDDING_RING_9': 'Legendary Ring of Love',
    'RED_CLAW_ARTIFACT': 'Red Claw Artifact',
    'BAIT_RING': 'Bait Ring',
    'SEAL_OF_THE_FAMILY': 'Seal of the Family',
    'HUNTER_RING': 'Hunter Ring',
    'CAMPFIRE_TALISMAN_29': 'Campfire God Badge 30',
	'ETERNAL_CRYSTAL': 'Eternal Crystal'
}

slayer_rewards = {
    'zombie': (('health', 2), ('health', 2), ('health', 3), ('health', 3), ('health', 4), ('health', 4),
               ('health', 5), ('health', 5), ('health', 6)),
    'spider': (('crit damage', 1), ('crit damage', 1), ('crit damage', 1), ('crit damage', 1), ('crit damage', 2),
               ('crit damage', 2), ('crit chance', 1), ('crit damage', 3), ('crit damage', 3)),
    'wolf': (('speed', 1), ('health', 2), ('speed', 1), ('health', 2), ('crit damage', 1), ('health', 3),
             ('crit damage', 2), ('speed', 1), ('health', 5))
}

pet_xp = [0, 100, 210, 330, 460, 605, 765, 
            940, 1130, 1340, 1570, 1820, 2095, 2395, 2725,
            3085, 3485, 3925, 4415, 4955, 5555, 6215, 6945,
            7745, 8625, 9585, 10635, 11785, 13045, 14425,
            15935, 17585, 19385, 21345, 23475, 25785, 28285,
            30985, 33905, 37065, 40485, 44185, 48185, 52535,
            57285, 62485, 68185, 74485, 81485, 89285, 97985,
            107685, 118485, 130485, 143785, 158485, 174685,
            192485, 211985, 233285, 256485, 281685, 309085,
            338885, 371285, 406485, 444685, 486085, 530885,
            579285, 631485, 687685, 748085, 812885, 882285,
            956485, 1035685, 1120385, 1211085, 1308285, 1412485,
            1524185, 1643885, 1772085, 1909285, 2055985, 2212685,
            2380385, 2560085, 2752785, 2959485, 3181185, 3418885,
            3673585, 3946285, 4237985, 4549685, 4883385, 5241085,
            5624785, 6036485, 6478185, 6954885, 7471585, 8033285,
            8644985, 9311685, 10038385, 10830085, 11691785, 12628485,
            13645185, 14746885, 15938585, 17225285, 18611985, 20108685,
            21725385, 23472085, 25358785]
            
pet_xp = {'common': pet_xp[0:100], 'uncommon': pet_xp[7:107], 'rare': pet_xp[12:112], 'epic': pet_xp[17:117], 'legendary': pet_xp[21:121]}

'''
pet_stats = {
    'SKELETON_HORSE': {
        'name': 'Skeleton Horse', 
        'stats': {
            'speed': lambda lvl: lvl // 10,
            'strength': lambda lvl: lvl + 5
        }
    }
}
'''

fairy_soul_hp_bonus = [3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16,
                       17, 17, 18, 18, 19, 19, 20, 20, 21, 21]

skill_exp_requirements = [50, 125, 200, 300, 500, 750, 1000, 1500, 2000, 3500, 5000,
                          7500, 10000, 15000, 20000, 30000, 50000, 75000, 100000, 200000, 300000,
                          400000, 500000, 600000, 700000, 800000, 900000, 1000000, 1100000, 1200000, 1300000,
                          1400000, 1500000, 1600000, 1700000, 1800000, 1900000, 2000000, 2100000, 2200000, 2300000,
                          2400000, 2500000, 2600000, 2700000, 2800000, 3100000, 3400000, 3700000, 4000000]

runecrafting_exp_requirements = [50, 100, 125, 160, 200, 250, 315, 400, 500, 625, 785, 1000,
                                 1250, 1600, 2000, 2465, 3125, 4000, 5000, 6200, 7800, 9800, 12200,
                                 15300]  # Shamelessly stolen from sky.lea.moe

minion_slot_requirements = [0, 0, 0, 0, 0, 5, 15, 30, 50, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300, 350, 400, 450, 500, 550]

guild_level_requirements = [100000, 150000, 250000, 500000, 750000, 1000000, 1250000, 1500000, 2000000, 2500000, 3000000] # every level after 2.5 mil needs 3mil

tiered_talismen = (  # Helps me filter useless talismen
    ('POTION_AFFINITY_TALISMAN', 'RING_POTION_AFFINITY', 'ARTIFACT_POTION_AFFINITY'),
    ('FEATHER_TALISMAN', 'FEATHER_RING', 'FEATHER_ARTIFACT'),
    ('SEA_CREATURE_TALISMAN', 'SEA_CREATURE_RING', 'SEA_CREATURE_ARTIFACT'),
    ('HEALING_TALISMAN', 'HEALING_RING'),
    ('CANDY_TALISMAN', 'CANDY_RING', 'CANDY_ARTIFACT'),
    ('INTIMIDATION_TALISMAN', 'INTIMIDATION_RING', 'INTIMIDATION_ARTIFACT'),
    ('SPIDER_TALISMAN', 'SPIDER_RING', 'SPIDER_ARTIFACT'),
    ('RED_CLAW_TALISMAN', 'RED_CLAW_RING', 'RED_CLAW_ARTIFACT'),
    ('HUNTER_TALISMAN', 'HUNTER_RING'),
    ('ZOMBIE_TALISMAN', 'ZOMBIE_RING', 'ZOMBIE_ARTIFACT'),
    ('BAT_TALISMAN', 'BAT_RING', 'BAT_ARTIFACT'),
    ('SHADY_RING', 'CROOKED_ARTIFACT', 'SEAL_OF_THE_FAMILY'),
    ('WOLF_TALISMAN', 'WOLF_RING')
)

reforges = {
    'clean': (
        {'strength': 0, 'crit chance': 0, 'crit damage': 0, 'attack speed': 1, 'health': 1, 'defense': 1, 'speed': 1,
         'intelligence': 0},
        {'strength': 0, 'crit chance': 0, 'crit damage': 0, 'attack speed': 1, 'health': 1, 'defense': 2, 'speed': 1,
         'intelligence': 0},
        {'strength': 0, 'crit chance': 0, 'crit damage': 0, 'attack speed': 2, 'health': 2, 'defense': 4, 'speed': 1,
         'intelligence': 0},
        {'strength': 0, 'crit chance': 0, 'crit damage': 0, 'attack speed': 2, 'health': 2, 'defense': 7, 'speed': 1,
         'intelligence': 0},
        {'strength': 0, 'crit chance': 0, 'crit damage': 0, 'attack speed': 2, 'health': 2, 'defense': 10, 'speed': 1,
         'intelligence': 0}
    ),
    'demonic': (
        {'strength': 1, 'crit chance': 0, 'crit damage': 0, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 3},
        {'strength': 2, 'crit chance': 0, 'crit damage': 0, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 6},
        {'strength': 2, 'crit chance': 0, 'crit damage': 0, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 10},
        {'strength': 3, 'crit chance': 0, 'crit damage': 0, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 15},
        {'strength': 5, 'crit chance': 0, 'crit damage': 0, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 20}
    ),
    'fierce': (
        {'strength': 1, 'crit chance': 1, 'crit damage': 1, 'attack speed': 0, 'health': 0, 'defense': 1, 'speed': 0,
         'intelligence': 0},
        {'strength': 2, 'crit chance': 1, 'crit damage': 2, 'attack speed': 0, 'health': 0, 'defense': 2, 'speed': 0,
         'intelligence': 0},
        {'strength': 2, 'crit chance': 1, 'crit damage': 2, 'attack speed': 0, 'health': 0, 'defense': 2, 'speed': 0,
         'intelligence': 0},
        {'strength': 3, 'crit chance': 1, 'crit damage': 3, 'attack speed': 0, 'health': 0, 'defense': 3, 'speed': 0,
         'intelligence': 0},
        {'strength': 5, 'crit chance': 2, 'crit damage': 5, 'attack speed': 0, 'health': 0, 'defense': 5, 'speed': 0,
         'intelligence': 0}
    ),
    'forceful': (
        {'strength': 2, 'crit chance': 0, 'crit damage': 0, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 4, 'crit chance': 0, 'crit damage': 0, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 7, 'crit chance': 0, 'crit damage': 0, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 10, 'crit chance': 0, 'crit damage': 0, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 15, 'crit chance': 0, 'crit damage': 0, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0}
    ),
    'godly': (
        {'strength': 1, 'crit chance': 1, 'crit damage': 1, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 1},
        {'strength': 2, 'crit chance': 2, 'crit damage': 2, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 2},
        {'strength': 4, 'crit chance': 2, 'crit damage': 3, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 2},
        {'strength': 7, 'crit chance': 3, 'crit damage': 6, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 3},
        {'strength': 10, 'crit chance': 5, 'crit damage': 8, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 5}
    ),
    'heavy': (
        {'strength': 0, 'crit chance': 0, 'crit damage': -1, 'attack speed': 0, 'health': 1, 'defense': 3, 'speed': 0,
         'intelligence': 0},
        {'strength': 0, 'crit chance': 0, 'crit damage': -2, 'attack speed': 0, 'health': 2, 'defense': 6, 'speed': 0,
         'intelligence': 0},
        {'strength': 0, 'crit chance': 0, 'crit damage': -2, 'attack speed': 0, 'health': 4, 'defense': 10, 'speed': 0,
         'intelligence': 0},
        {'strength': 0, 'crit chance': 0, 'crit damage': -3, 'attack speed': 0, 'health': 7, 'defense': 15, 'speed': 0,
         'intelligence': 0},
        {'strength': 0, 'crit chance': 0, 'crit damage': -5, 'attack speed': 0, 'health': 10, 'defense': 20, 'speed': 0,
         'intelligence': 0}
    ),
    'keen': (
        {'strength': 1, 'crit chance': 1, 'crit damage': 1, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 2, 'crit chance': 1, 'crit damage': 1, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 2, 'crit chance': 2, 'crit damage': 2, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 3, 'crit chance': 2, 'crit damage': 2, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 5, 'crit chance': 3, 'crit damage': 3, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0}
    ),
    'light': (
        {'strength': 0, 'crit chance': 0, 'crit damage': 1, 'attack speed': 1, 'health': 1, 'defense': 1, 'speed': 1,
         'intelligence': 0},
        {'strength': 0, 'crit chance': 0, 'crit damage': 2, 'attack speed': 2, 'health': 2, 'defense': 2, 'speed': 1,
         'intelligence': 0},
        {'strength': 0, 'crit chance': 0, 'crit damage': 2, 'attack speed': 2, 'health': 2, 'defense': 2, 'speed': 2,
         'intelligence': 0},
        {'strength': 0, 'crit chance': 0, 'crit damage': 3, 'attack speed': 3, 'health': 3, 'defense': 3, 'speed': 2,
         'intelligence': 0},
        {'strength': 0, 'crit chance': 0, 'crit damage': 5, 'attack speed': 5, 'health': 5, 'defense': 5, 'speed': 3,
         'intelligence': 0}
    ),
    'mythic': (
        {'strength': 1, 'crit chance': 0, 'crit damage': 0, 'attack speed': 0, 'health': 1, 'defense': 1, 'speed': 1,
         'intelligence': 3},
        {'strength': 2, 'crit chance': 0, 'crit damage': 0, 'attack speed': 0, 'health': 2, 'defense': 2, 'speed': 1,
         'intelligence': 7},
        {'strength': 2, 'crit chance': 0, 'crit damage': 0, 'attack speed': 0, 'health': 2, 'defense': 2, 'speed': 1,
         'intelligence': 12},
        {'strength': 3, 'crit chance': 0, 'crit damage': 0, 'attack speed': 0, 'health': 3, 'defense': 3, 'speed': 1,
         'intelligence': 18},
        {'strength': 5, 'crit chance': 0, 'crit damage': 0, 'attack speed': 0, 'health': 5, 'defense': 5, 'speed': 1,
         'intelligence': 25}
    ),
    'pure': (
        {'strength': 1, 'crit chance': 1, 'crit damage': 1, 'attack speed': 1, 'health': 1, 'defense': 1, 'speed': 1,
         'intelligence': 1},
        {'strength': 2, 'crit chance': 2, 'crit damage': 2, 'attack speed': 2, 'health': 2, 'defense': 2, 'speed': 1,
         'intelligence': 2},
        {'strength': 2, 'crit chance': 2, 'crit damage': 2, 'attack speed': 2, 'health': 2, 'defense': 2, 'speed': 1,
         'intelligence': 2},
        {'strength': 3, 'crit chance': 3, 'crit damage': 3, 'attack speed': 3, 'health': 3, 'defense': 3, 'speed': 1,
         'intelligence': 3},
        {'strength': 5, 'crit chance': 5, 'crit damage': 5, 'attack speed': 5, 'health': 5, 'defense': 5, 'speed': 1,
         'intelligence': 5}
    ),
    'smart': (
        {'strength': 0, 'crit chance': 0, 'crit damage': 0, 'attack speed': 0, 'health': 0, 'defense': 1, 'speed': 0,
         'intelligence': 5},
        {'strength': 0, 'crit chance': 0, 'crit damage': 0, 'attack speed': 0, 'health': 0, 'defense': 2, 'speed': 0,
         'intelligence': 10},
        {'strength': 0, 'crit chance': 0, 'crit damage': 0, 'attack speed': 0, 'health': 0, 'defense': 2, 'speed': 0,
         'intelligence': 18},
        {'strength': 0, 'crit chance': 0, 'crit damage': 0, 'attack speed': 0, 'health': 0, 'defense': 3, 'speed': 0,
         'intelligence': 32},
        {'strength': 0, 'crit chance': 0, 'crit damage': 0, 'attack speed': 0, 'health': 0, 'defense': 5, 'speed': 0,
         'intelligence': 50}
    ),
    'strong': (
        {'strength': 1, 'crit chance': 0, 'crit damage': 1, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 2, 'crit chance': 0, 'crit damage': 2, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 4, 'crit chance': 0, 'crit damage': 4, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 7, 'crit chance': 0, 'crit damage': 7, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 10, 'crit chance': 0, 'crit damage': 10, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0}
    ),
    'superior': (
        {'strength': 1, 'crit chance': 1, 'crit damage': 1, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 2, 'crit chance': 1, 'crit damage': 1, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 4, 'crit chance': 1, 'crit damage': 1, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 7, 'crit chance': 1, 'crit damage': 1, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 10, 'crit chance': 1, 'crit damage': 1, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0}
    ),
    'titanic': (
        {'strength': 0, 'crit chance': 0, 'crit damage': 0, 'attack speed': 0, 'health': 3, 'defense': 3, 'speed': 0,
         'intelligence': 0},
        {'strength': 0, 'crit chance': 0, 'crit damage': 0, 'attack speed': 0, 'health': 6, 'defense': 6, 'speed': 0,
         'intelligence': 0},
        {'strength': 0, 'crit chance': 0, 'crit damage': 0, 'attack speed': 0, 'health': 10, 'defense': 10, 'speed': 0,
         'intelligence': 0},
        {'strength': 0, 'crit chance': 0, 'crit damage': 0, 'attack speed': 0, 'health': 15, 'defense': 15, 'speed': 0,
         'intelligence': 0},
        {'strength': 0, 'crit chance': 0, 'crit damage': 0, 'attack speed': 0, 'health': 20, 'defense': 20, 'speed': 0,
         'intelligence': 0}
    ),
    'unpleasant': (
        {'strength': 0, 'crit chance': 1, 'crit damage': 1, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 1},
        {'strength': 0, 'crit chance': 2, 'crit damage': 2, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 1},
        {'strength': 0, 'crit chance': 3, 'crit damage': 3, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 2},
        {'strength': 0, 'crit chance': 6, 'crit damage': 6, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 3},
        {'strength': 0, 'crit chance': 8, 'crit damage': 8, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 5}
    ),
    'wise': (
        {'strength': 0, 'crit chance': 0, 'crit damage': 0, 'attack speed': 0, 'health': 1, 'defense': 0, 'speed': 1,
         'intelligence': 10},
        {'strength': 0, 'crit chance': 0, 'crit damage': 0, 'attack speed': 0, 'health': 2, 'defense': 0, 'speed': 1,
         'intelligence': 20},
        {'strength': 0, 'crit chance': 0, 'crit damage': 0, 'attack speed': 0, 'health': 2, 'defense': 0, 'speed': 1,
         'intelligence': 35},
        {'strength': 0, 'crit chance': 0, 'crit damage': 0, 'attack speed': 0, 'health': 2, 'defense': 0, 'speed': 2,
         'intelligence': 65},
        {'strength': 0, 'crit chance': 0, 'crit damage': 0, 'attack speed': 0, 'health': 5, 'defense': 0, 'speed': 2,
         'intelligence': 100}
    ),
    'zealous': (
        {'strength': 1, 'crit chance': 1, 'crit damage': 1, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 1},
        {'strength': 2, 'crit chance': 2, 'crit damage': 2, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 2},
        {'strength': 2, 'crit chance': 2, 'crit damage': 2, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 2},
        {'strength': 3, 'crit chance': 3, 'crit damage': 3, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 3},
        {'strength': 5, 'crit chance': 5, 'crit damage': 5, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 5}
    ),
    'epic': (
        {'strength': 2, 'crit chance': 0, 'crit damage': 1, 'attack speed': 1, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 4, 'crit chance': 0, 'crit damage': 2, 'attack speed': 2, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 7, 'crit chance': 0, 'crit damage': 4, 'attack speed': 2, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 10, 'crit chance': 0, 'crit damage': 7, 'attack speed': 3, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 15, 'crit chance': 0, 'crit damage': 10, 'attack speed': 5, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0}
    ),
    'fair': (
        {'strength': 1, 'crit chance': 1, 'crit damage': 1, 'attack speed': 1, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 1},
        {'strength': 2, 'crit chance': 2, 'crit damage': 2, 'attack speed': 2, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 2},
        {'strength': 2, 'crit chance': 2, 'crit damage': 2, 'attack speed': 2, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 2},
        {'strength': 3, 'crit chance': 3, 'crit damage': 3, 'attack speed': 3, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 3},
        {'strength': 5, 'crit chance': 5, 'crit damage': 5, 'attack speed': 5, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 5}
    ),
    'fast': (
        {'strength': 1, 'crit chance': 0, 'crit damage': 0, 'attack speed': 2, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 2, 'crit chance': 0, 'crit damage': 0, 'attack speed': 4, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 4, 'crit chance': 0, 'crit damage': 0, 'attack speed': 7, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 7, 'crit chance': 0, 'crit damage': 0, 'attack speed': 10, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 10, 'crit chance': 0, 'crit damage': 0, 'attack speed': 15, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0}
    ),
    'gentle': (
        {'strength': 0, 'crit chance': 0, 'crit damage': 0, 'attack speed': 1, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 0, 'crit chance': 0, 'crit damage': 0, 'attack speed': 2, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 0, 'crit chance': 0, 'crit damage': 0, 'attack speed': 4, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 0, 'crit chance': 0, 'crit damage': 0, 'attack speed': 7, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 0, 'crit chance': 0, 'crit damage': 0, 'attack speed': 10, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0}
    ),
    'heroic': (
        {'strength': 3, 'crit chance': 0, 'crit damage': 0, 'attack speed': 1, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 3},
        {'strength': 6, 'crit chance': 0, 'crit damage': 0, 'attack speed': 2, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 6},
        {'strength': 10, 'crit chance': 0, 'crit damage': 0, 'attack speed': 2, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 10},
        {'strength': 15, 'crit chance': 0, 'crit damage': 0, 'attack speed': 3, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 15},
        {'strength': 20, 'crit chance': 0, 'crit damage': 0, 'attack speed': 5, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 20}
    ),
    'hurtful': (
        {'strength': 1, 'crit chance': 1, 'crit damage': 1, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 2, 'crit chance': 1, 'crit damage': 1, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 2, 'crit chance': 2, 'crit damage': 2, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 3, 'crit chance': 2, 'crit damage': 2, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 5, 'crit chance': 3, 'crit damage': 3, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0}
    ),
    'legendary': (
        {'strength': 2, 'crit chance': 1, 'crit damage': 1, 'attack speed': 2, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 3},
        {'strength': 4, 'crit chance': 2, 'crit damage': 2, 'attack speed': 4, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 7},
        {'strength': 7, 'crit chance': 4, 'crit damage': 4, 'attack speed': 7, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 12},
        {'strength': 10, 'crit chance': 7, 'crit damage': 7, 'attack speed': 10, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 18},
        {'strength': 15, 'crit chance': 10, 'crit damage': 10, 'attack speed': 15, 'health': 0, 'defense': 0,
         'speed': 0, 'intelligence': 25}
    ),
    'neat': (
        {'strength': 0, 'crit chance': 1, 'crit damage': 2, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 0, 'crit chance': 2, 'crit damage': 4, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 0, 'crit chance': 4, 'crit damage': 7, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 0, 'crit chance': 7, 'crit damage': 10, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 0, 'crit chance': 10, 'crit damage': 15, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0}
    ),
    'odd': (
        {'strength': 0, 'crit chance': 1, 'crit damage': 1, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': -5},
        {'strength': 0, 'crit chance': 2, 'crit damage': 2, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': -10},
        {'strength': 0, 'crit chance': 4, 'crit damage': 4, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': -18},
        {'strength': 0, 'crit chance': 7, 'crit damage': 7, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': -32},
        {'strength': 0, 'crit chance': 10, 'crit damage': 10, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': -50}
    ),
    'rich': (
        {'strength': 0, 'crit chance': 1, 'crit damage': 2, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 3},
        {'strength': 0, 'crit chance': 2, 'crit damage': 2, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 6},
        {'strength': 0, 'crit chance': 4, 'crit damage': 4, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 10},
        {'strength': 0, 'crit chance': 7, 'crit damage': 7, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 15},
        {'strength': 0, 'crit chance': 10, 'crit damage': 15, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 20}
    ),
    'spicy': (
        {'strength': 1, 'crit chance': 1, 'crit damage': 5, 'attack speed': 1, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 2, 'crit chance': 1, 'crit damage': 10, 'attack speed': 2, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 2, 'crit chance': 1, 'crit damage': 18, 'attack speed': 4, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 3, 'crit chance': 1, 'crit damage': 32, 'attack speed': 7, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 5, 'crit chance': 1, 'crit damage': 50, 'attack speed': 10, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0}
    ),
    'deadly': (
        {'strength': 1, 'crit chance': 1, 'crit damage': 1, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 1},
        {'strength': 2, 'crit chance': 2, 'crit damage': 2, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 2},
        {'strength': 4, 'crit chance': 4, 'crit damage': 4, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 4},
        {'strength': 7, 'crit chance': 7, 'crit damage': 7, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 7},
        {'strength': 10, 'crit chance': 10, 'crit damage': 10, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 10}
    ),
    'fine': (
        {'strength': 1, 'crit chance': 1, 'crit damage': 1, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 2, 'crit chance': 2, 'crit damage': 2, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 4, 'crit chance': 2, 'crit damage': 2, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 7, 'crit chance': 3, 'crit damage': 3, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 10, 'crit chance': 5, 'crit damage': 5, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0}
    ),
    'grand': (
        {'strength': 3, 'crit chance': 0, 'crit damage': 0, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 7, 'crit chance': 0, 'crit damage': 0, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 12, 'crit chance': 0, 'crit damage': 0, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 17, 'crit chance': 0, 'crit damage': 0, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 25, 'crit chance': 0, 'crit damage': 0, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0}
    ),
    'hasty': (
        {'strength': 1, 'crit chance': 3, 'crit damage': 0, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 2, 'crit chance': 7, 'crit damage': 0, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 2, 'crit chance': 12, 'crit damage': 0, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 3, 'crit chance': 18, 'crit damage': 0, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 5, 'crit chance': 25, 'crit damage': 0, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0}
    ),
    'rapid': (
        {'strength': 1, 'crit chance': 0, 'crit damage': 5, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 2, 'crit chance': 0, 'crit damage': 10, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 4, 'crit chance': 0, 'crit damage': 18, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 7, 'crit chance': 0, 'crit damage': 32, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 10, 'crit chance': 0, 'crit damage': 50, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0}
    ),
    'unreal': (
        {'strength': 2, 'crit chance': 2, 'crit damage': 2, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 4, 'crit chance': 4, 'crit damage': 4, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 7, 'crit chance': 7, 'crit damage': 7, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 10, 'crit chance': 10, 'crit damage': 10, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 15, 'crit chance': 15, 'crit damage': 15, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0}
    ),
    'bizarre': (
        {'strength': 1, 'crit chance': -1, 'crit damage': -1, 'attack speed': 0, 'health': 1, 'defense': 0, 'speed': 0,
         'intelligence': 3},
        {'strength': 2, 'crit chance': -2, 'crit damage': -2, 'attack speed': 0, 'health': 1, 'defense': 0, 'speed': 0,
         'intelligence': 6},
        {'strength': 2, 'crit chance': -2, 'crit damage': -2, 'attack speed': 0, 'health': 1, 'defense': 0, 'speed': 0,
         'intelligence': 10},
        {'strength': 3, 'crit chance': -3, 'crit damage': -3, 'attack speed': 0, 'health': 1, 'defense': 0, 'speed': 0,
         'intelligence': 15},
        {'strength': 5, 'crit chance': -5, 'crit damage': -5, 'attack speed': 0, 'health': 1, 'defense': 0, 'speed': 0,
         'intelligence': 20}
    ),
    'itchy': (
        {'strength': 1, 'crit chance': 0, 'crit damage': 3, 'attack speed': 1, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 2, 'crit chance': 0, 'crit damage': 5, 'attack speed': 2, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 2, 'crit chance': 0, 'crit damage': 8, 'attack speed': 2, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 3, 'crit chance': 0, 'crit damage': 12, 'attack speed': 3, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 5, 'crit chance': 0, 'crit damage': 15, 'attack speed': 5, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0}  # !!!
    ),
    'ominous': (
        {'strength': 1, 'crit chance': 0, 'crit damage': 1, 'attack speed': 0, 'health': 1, 'defense': 1, 'speed': 0,
         'intelligence': 1},
        {'strength': 2, 'crit chance': 0, 'crit damage': 2, 'attack speed': 0, 'health': 2, 'defense': 2, 'speed': 0,
         'intelligence': 2},
        {'strength': 2, 'crit chance': 0, 'crit damage': 2, 'attack speed': 0, 'health': 2, 'defense': 2, 'speed': 0,
         'intelligence': 2},
        {'strength': 3, 'crit chance': 0, 'crit damage': 3, 'attack speed': 0, 'health': 3, 'defense': 3, 'speed': 0,
         'intelligence': 3},
        {'strength': 5, 'crit chance': 0, 'crit damage': 5, 'attack speed': 0, 'health': 5, 'defense': 5, 'speed': 0,
         'intelligence': 5}
    ),
    'pleasant': (
        {'strength': 0, 'crit chance': 0, 'crit damage': 1, 'attack speed': 1, 'health': 1, 'defense': 1, 'speed': 0,
         'intelligence': 1},
        {'strength': 0, 'crit chance': 0, 'crit damage': 2, 'attack speed': 1, 'health': 1, 'defense': 2, 'speed': 0,
         'intelligence': 2},
        {'strength': 0, 'crit chance': 0, 'crit damage': 2, 'attack speed': 1, 'health': 2, 'defense': 2, 'speed': 0,
         'intelligence': 2},
        {'strength': 0, 'crit chance': 0, 'crit damage': 3, 'attack speed': 1, 'health': 2, 'defense': 3, 'speed': 1,
         'intelligence': 3},
        {'strength': 0, 'crit chance': 0, 'crit damage': 5, 'attack speed': 1, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0}  # !!!
    ),
    'pretty': (
        {'strength': 0, 'crit chance': 0, 'crit damage': 0, 'attack speed': 1, 'health': 1, 'defense': 0, 'speed': 0,
         'intelligence': 3},
        {'strength': 0, 'crit chance': 0, 'crit damage': 0, 'attack speed': 2, 'health': 2, 'defense': 0, 'speed': 0,
         'intelligence': 6},
        {'strength': 0, 'crit chance': 0, 'crit damage': 0, 'attack speed': 2, 'health': 2, 'defense': 0, 'speed': 1,
         'intelligence': 10},
        {'strength': 0, 'crit chance': 0, 'crit damage': 0, 'attack speed': 3, 'health': 3, 'defense': 0, 'speed': 1,
         'intelligence': 15},
        {'strength': 0, 'crit chance': 0, 'crit damage': 0, 'attack speed': 5, 'health': 5, 'defense': 0, 'speed': 0,
         'intelligence': 20}  # !!!
    ),
    'shiny': (
        {'strength': 0, 'crit chance': 0, 'crit damage': 0, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 0, 'crit chance': 0, 'crit damage': 0, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 0, 'crit chance': 0, 'crit damage': 0, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 0, 'crit chance': 0, 'crit damage': 0, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0},
        {'strength': 0, 'crit chance': 0, 'crit damage': 0, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0}  # !!!
    ),
    'simple': (
        {'strength': 1, 'crit chance': 0, 'crit damage': 0, 'attack speed': 0, 'health': 1, 'defense': 1, 'speed': 0,
         'intelligence': 0},
        {'strength': 1, 'crit chance': 0, 'crit damage': 0, 'attack speed': 0, 'health': 1, 'defense': 1, 'speed': 0,
         'intelligence': 0},
        {'strength': 1, 'crit chance': 0, 'crit damage': 0, 'attack speed': 0, 'health': 1, 'defense': 1, 'speed': 0,
         'intelligence': 0},
        {'strength': 1, 'crit chance': 0, 'crit damage': 0, 'attack speed': 0, 'health': 1, 'defense': 1, 'speed': 0,
         'intelligence': 0},
        {'strength': 1, 'crit chance': 0, 'crit damage': 0, 'attack speed': 0, 'health': 1, 'defense': 1, 'speed': 0,
         'intelligence': 0}
    ),
    'strange': (
        {'strength': 1, 'crit chance': 1, 'crit damage': 1, 'attack speed': 1, 'health': 0, 'defense': 1, 'speed': 0,
         'intelligence': -5},
        {'strength': 2, 'crit chance': 2, 'crit damage': 2, 'attack speed': 2, 'health': 0, 'defense': 1, 'speed': 0,
         'intelligence': -10},
        {'strength': 1, 'crit chance': 1, 'crit damage': 1, 'attack speed': 1, 'health': 0, 'defense': 1, 'speed': 0,
         'intelligence': -18},
        {'strength': 1, 'crit chance': 1, 'crit damage': 1, 'attack speed': 1, 'health': 0, 'defense': 1, 'speed': 0,
         'intelligence': -32},
        {'strength': 0, 'crit chance': 0, 'crit damage': 0, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0}  # !!!
    ),
    'vivid': (
        {'strength': 1, 'crit chance': 0, 'crit damage': 0, 'attack speed': 0, 'health': 1, 'defense': 1, 'speed': 0,
         'intelligence': 0},
        {'strength': 1, 'crit chance': 0, 'crit damage': 0, 'attack speed': 0, 'health': 2, 'defense': 1, 'speed': 0,
         'intelligence': 0},
        {'strength': 1, 'crit chance': 0, 'crit damage': 0, 'attack speed': 0, 'health': 2, 'defense': 1, 'speed': 1,
         'intelligence': 0},
        {'strength': 2, 'crit chance': 0, 'crit damage': 0, 'attack speed': 0, 'health': 2, 'defense': 1, 'speed': 1,
         'intelligence': 0},
        {'strength': 0, 'crit chance': 0, 'crit damage': 0, 'attack speed': 0, 'health': 0, 'defense': 0, 'speed': 0,
         'intelligence': 0}  # !!!
    )
}
