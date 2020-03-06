_advancedmode = False
def enable_advanced_mode():
	global _advancedmode
	_advancedmode = True

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

talismans = {
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

skills = ['farming', 'mining', 'combat', 'foraging', 'fishing', 'enchanting', 'alchemy', 'carpentry', 'runecrafting']
cosmetic_skills = ['carpentry', 'runecrafting']
slayers = ['zombie', 'spider', 'wolf']

slayer_rewards = {
    'zombie': (('health', 2), ('health', 2), ('health', 3), ('health', 3), ('health', 4), ('health', 4),
               ('health', 5), ('health', 5), ('health', 6)),
    'spider': (('crit damage', 1), ('crit damage', 1), ('crit damage', 1), ('crit damage', 1), ('crit damage', 2),
               ('crit damage', 2), ('crit chance', 1), ('crit damage', 3), ('crit damage', 3)),
    'wolf': (('speed', 1), ('health', 2), ('speed', 1), ('health', 2), ('crit damage', 1), ('health', 3),
             ('crit damage', 2), ('speed', 1), ('health', 5))
}

slayer_level_requirements = {
	'zombie': [5, 15, 200, 1000, 5000, 20000, 100000, 400000, 1000000],
	'spider': [5, 15, 200, 1000, 5000, 20000, 100000, 400000, 1000000],
	'wolf': [5, 15, 200, 1500, 5000, 20000, 100000, 400000, 1000000]
}

base_stats = {
	'damage': 0,
	'strength': 0, 
	'crit chance': 20,
	'crit damage': 50, 
	'attack speed': 100,
	'health': 100,
	'defense': 0,
	'speed': 100,
	'intelligence': 0
}

profile_names = [
	'Apple',
	'Banana',
	'Blueberry',
	'Coconut',
	'Cucumber',
	'Grapes',
	'Kiwi',
	'Lemon',
	'Lime',
	'Mango',
	'Orange',
	'Papaya',
	'Peach',
	'Pear',
	'Pineapple',
	'Pomegranate',
	'Raspberry',
	'Strawberry',
	'Tomato',
	'Watermelon',
	'Zucchini'
]

'''
pet_xp = [0, 100, 210, 330, 460, 605, 765, 940, 1130, 1340, 1570, 1820, 2095, 2395, 2725, 3085, 3485, 3925, 4415, 4955, 5555, 6215, 6945, 7745, 8625, 9585, 10635, 11785, 13045, 14425, 15935, 17585, 19385, 21345, 23475, 25785, 28285, 30985, 33905, 37065, 40485, 44185, 48185, 52535, 57285, 62485, 68185, 74485, 81485, 89285, 97985, 107685, 118485, 130485, 143785, 158485, 174685, 192485, 211985, 233285, 256485, 281685, 309085, 338885, 371285, 406485, 444685, 486085, 530885, 579285, 631485, 687685, 748085, 812885, 882285, 956485, 1035685, 1120385, 1211085, 1308285, 1412485, 1524185, 1643885, 1772085, 1909285, 2055985, 2212685, 2380385, 2560085, 2752785, 2959485, 3181185, 3418885, 3673585, 3946285, 4237985, 4549685, 4883385, 5241085, 5624785, 6036485, 6478185, 6954885, 7471585, 8033285, 8644985, 9311685, 10038385, 10830085, 11691785, 12628485, 13645185, 14746885, 15938585, 17225285, 18611985, 20108685, 21725385, 23472085, 25358785]

def xp_slice(start):
    diff = pet_xp[start - 1]
    return [xp - diff for xp in pet_xp[start-1:start+99]]

pet_xp = {'common': xp_slice(1), 'uncommon': xp_slice(7), 'rare': xp_slice(12), 'epic': xp_slice(17), 'legendary': xp_slice(21)}
'''

pet_xp = {
    'common': [
        0, 100, 210, 330, 460, 605, 765, 940, 1130, 1340, 1570, 1820, 2095,
        2395, 2725, 3085, 3485, 3925, 4415, 4955, 5555, 6215, 6945, 7745,
        8625, 9585, 10635, 11785, 13045, 14425, 15935, 17585, 19385, 21345,
        23475, 25785, 28285, 30985, 33905, 37065, 40485, 44185, 48185,
        52535, 57285, 62485, 68185, 74485, 81485, 89285, 97985, 107685,
        118485, 130485, 143785, 158485, 174685, 192485, 211985, 233285,
        256485, 281685, 309085, 338885, 371285, 406485, 444685, 486085,
        530885, 579285, 631485, 687685, 748085, 812885, 882285, 956485,
        1035685, 1120385, 1211085, 1308285, 1412485, 1524185, 1643885,
        1772085, 1909285, 2055985, 2212685, 2380385, 2560085, 2752785,
        2959485, 3181185, 3418885, 3673585, 3946285, 4237985, 4549685,
        4883385, 5241085, 5624785
    ],
    'uncommon': [
        0, 175, 365, 575, 805, 1055, 1330, 1630, 1960, 2320, 2720, 3160,
        3650, 4190, 4790, 5450, 6180, 6980, 7860, 8820, 9870, 11020,
        12280, 13660, 15170, 16820, 18620, 20580, 22710, 25020, 27520,
        30220, 33140, 36300, 39720, 43420, 47420, 51770, 56520, 61720,
        67420, 73720, 80720, 88520, 97220, 106920, 117720, 129720, 143020,
        157720, 173920, 191720, 211220, 232520, 255720, 280920, 308320,
        338120, 370520, 405720, 443920, 485320, 530120, 578520, 630720,
        686920, 747320, 812120, 881520, 955720, 1034920, 1119620, 1210320,
        1307520, 1411720, 1523420, 1643120, 1771320, 1908520, 2055220,
        2211920, 2379620, 2559320, 2752020, 2958720, 3180420, 3418120,
        3672820, 3945520, 4237220, 4548920, 4882620, 5240320, 5624020,
        6035720, 6477420, 6954120, 7470820, 8032520, 8644220
    ],
    'rare': [
        0, 275, 575, 905, 1265, 1665, 2105, 2595, 3135, 3735, 4395, 5125,
        5925, 6805, 7765, 8815, 9965, 11225, 12605, 14115, 15765, 17565,
        19525, 21655, 23965, 26465, 29165, 32085, 35245, 38665, 42365, 46365,
        50715, 55465, 60665, 66365, 72665, 79665, 87465, 96165, 105865,
        116665, 128665, 141965, 156665, 172865, 190665, 210165, 231465,
        254665, 279865, 307265, 337065, 369465, 404665, 442865, 484265,
        529065, 577465, 629665, 685865, 746265, 811065, 880465, 954665,
        1033865, 1118565, 1209265, 1306465, 1410665, 1522365, 1642065,
        1770265, 1907465, 2054165, 2210865, 2378565, 2558265, 2750965,
        2957665, 3179365, 3417065, 3671765, 3944465, 4236165, 4547865,
        4881565, 5239265, 5622965, 6034665, 6476365, 6953065, 7469765,
        8031465, 8643165, 9309865, 10036565, 10828265, 11689965, 12626665
    ],
    'epic': [
        0, 440, 930, 1470, 2070, 2730, 3460, 4260, 5140, 6100, 7150, 8300,
        9560, 10940, 12450, 14100, 15900, 17860, 19990, 22300, 24800, 27500,
        30420, 33580, 37000, 40700, 44700, 49050, 53800, 59000, 64700, 71000,
        78000, 85800, 94500, 104200, 115000, 127000, 140300, 155000, 171200,
        189000, 208500, 229800, 253000, 278200, 305600, 335400, 367800,
        403000, 441200, 482600, 527400, 575800, 628000, 684200, 744600,
        809400, 878800, 953000, 1032200, 1116900, 1207600, 1304800, 1409000,
        1520700, 1640400, 1768600, 1905800, 2052500, 2209200, 2376900,
        2556600, 2749300, 2956000, 3177700, 3415400, 3670100, 3942800,
        4234500, 4546200, 4879900, 5237600, 5621300, 6033000, 6474700,
        6951400, 7468100, 8029800, 8641500, 9308200, 10034900, 10826600,
        11688300, 12625000, 13641700, 14743400, 15935100, 17221800,
        18608500
    ],
    'legendary': [
        0, 660, 1390, 2190, 3070, 4030, 5080, 6230, 7490, 8870, 10380,
        12030, 13830, 15790, 17920, 20230, 22730, 25430, 28350, 31510,
        34930, 38630, 42630, 46980, 51730, 56930, 62630, 68930, 75930,
        83730, 92430, 102130, 112930, 124930, 138230, 152930, 169130,
        186930, 206430, 227730, 250930, 276130, 303530, 333330, 365730,
        400930, 439130, 480530, 525330, 573730, 625930, 682130, 742530,
        807330, 876730, 950930, 1030130, 1114830, 1205530, 1302730,
        1406930, 1518630, 1638330, 1766530, 1903730, 2050430, 2207130,
        2374830, 2554530, 2747230, 2953930, 3175630, 3413330, 3668030,
        3940730, 4232430, 4544130, 4877830, 5235530, 5619230, 6030930,
        6472630, 6949330, 7466030, 8027730, 8639430, 9306130, 10032830,
        10824530, 11686230, 12622930, 13639630, 14741330, 15933030,
        17219730, 18606430, 20103130, 21719830, 23466530, 25353230
    ]
}

pet_stats = {
    'SKELETON_HORSE': {
        'name': 'Skeleton Horse', 
        'stats': {
        },
        'type': 'combat',
        'icon': '/head/47effce35132c86ff72bcae77dfbb1d22587e94df3cbc2570ed17cf8973a'
    },
    'SNOWMAN': {
        'name': 'Snowman', 
        'stats': {
            'damage': lambda lvl: lvl // 3,
            'strength': lambda lvl: lvl // 3,
            'crit damage': lambda lvl: lvl // 3
        },
        'type': 'combat',
        'icon': '/head/11136616d8c4a87a54ce78a97b551610c2b2c8f6d410bc38b858f974b113b208'
    },
    'BAT': {
        'name': 'Bat', 
        'stats': {
        },
        'type': 'mining',
        'icon': '/head/382fc3f71b41769376a9e92fe3adbaac3772b999b219c9d6b4680ba9983e527'
    },
    'SHEEP': {
        'name': 'Sheep', 
        'stats': {
        },
        'type': 'alchemy',
        'icon': '/head/64e22a46047d272e89a1cfa13e9734b7e12827e235c2012c1a95962874da0'
    },
    'CHICKEN': {
        'name': 'Chicken', 
        'stats': {
        },
        'type': 'farming',
        'icon': '/head/7f37d524c3eed171ce149887ea1dee4ed399904727d521865688ece3bac75e'
    },
    'WITHER_SKELETON': {
        'name': 'Wither Skeleton', 
        'stats': {
            'strength': lambda lvl: lvl // 4,
            'crit chance': lambda lvl: lvl // 20,
            'crit damage': lambda lvl: lvl // 4
        },
        'type': 'combat',
        'icon': '/head/f5ec964645a8efac76be2f160d7c9956362f32b6517390c59c3085034f050cff'
    },
    'SILVERFISH': {
        'name': 'Silverfish', 
        'stats': {
        },
        'type': 'mining',
        'icon': '/head/da91dab8391af5fda54acd2c0b18fbd819b865e1a8f1d623813fa761e924540'
    },
    'RABBIT': {
        'name': 'Rabbit', 
        'stats': {
        },
        'type': 'farming',
        'icon': '/head/117bffc1972acd7f3b4a8f43b5b6c7534695b8fd62677e0306b2831574b'
    },
    'HORSE': {
        'name': 'Horse', 
        'stats': {
        },
        'type': 'combat',
        'icon': '/head/36fcd3ec3bc84bafb4123ea479471f9d2f42d8fb9c5f11cf5f4e0d93226'
    },
    'PIGMAN': {
        'name': 'Pigman', 
        'stats': {
            'strength': lambda lvl: lvl // 2
        }, # lvl * 0.4 damage and lvl * 0.2 strength to Pigman Sword (All), Additional Damage lvl * 0.25% to mobs above lvl 100 (Slayers, Legendary)
        'type': 'combat',
        'icon': '/head/63d9cb6513f2072e5d4e426d70a5557bc398554c880d4e7b7ec8ef4945eb02f2'
    },
    'WOLF': {
        'name': 'Wolf', 
        'stats': {
            'crit damage': lambda lvl: lvl // 10
        },
        'type': 'combat',
        'icon': '/head/dc3dd984bb659849bd52994046964c22725f717e986b12d548fd169367d494'
    },
    'OCELOT': {
        'name': 'Ocelot', 
        'stats': {
        },
        'type': 'foraging',
        'icon': '/head/5657cd5c2989ff97570fec4ddcdc6926a68a3393250c1be1f0b114a1db1'
    },
    'LION': {
        'name': 'Lion', 
        'stats': {
            'damage': lambda lvl: lvl * 0.2,
            'strength': lambda lvl: lvl // 2
        }, # First Strike lvl * 0.5% (Zealots, All), Additional Damage lvl * 0.3% to mobs below lvl 80 (Zealots, All)
        'type': 'foraging',
        'icon': '/head/38ff473bd52b4db2c06f1ac87fe1367bce7574fac330ffac7956229f82efba1'
    },
    'ENDER_DRAGON': {
        'name': 'Dragon', 
        'stats': {
            'strength': lambda lvl: lvl // 2,
            'crit chance': lambda lvl: lvl // 10,
            'crit damage': lambda lvl: lvl // 2
        }, # lvl * 0.5 damage and lvl * 0.3 strength to AotD (All), lvl * 0.1% stats boosts (Legendary)
        'type': 'combat',
        'icon': '/head/aec3ff563290b13ff3bcc36898af7eaa988b6cc18dc254147f58374afe9b21b9'
    },
    'GUARDIAN': {
        'name': 'Guardian', 
        'stats': {
        },
        'type': 'fishing',
        'icon': '/head/221025434045bda7025b3e514b316a4b770c6faa4ba9adb4be3809526db77f9d'
    },
    'ENDERMAN': {
        'name': 'Enderman', 
        'stats': {
            'crit damage': lambda lvl: lvl * 0.75
        },
        'type': 'combat',
        'icon': '/head/6eab75eaa5c9f2c43a0d23cfdce35f4df632e9815001850377385f7b2f039ce1'
    },
    'BLUE_WHALE': {
        'name': 'Whale', 
        'stats': {
        },
        'type': 'fishing',
        'icon': '/head/dab779bbccc849f88273d844e8ca2f3a67a1699cb216c0a11b44326ce2cc20'
    },
    'GIRAFFE': {
        'name': 'Giraffe', 
        'stats': {
            # No info :(
        },
        'type': 'unknown',
        'icon': '/head/6eab75eaa5c9f2c43a0d23cfdce35f4df632e9815001850377385f7b2f039ce1'
    },
    'PHOENIX': {
        'name': 'Phoenix', 
        'stats': {
            'strength': lambda lvl: lvl // 2 + 10
        },
        'type': 'combat',
        'icon': '/head/23aaf7b1a778949696cb99d4f04ad1aa518ceee256c72e5ed65bfa5c2d88d9e'
    },
    'BEE': {
        'name': 'Bee', 
        'stats': {
        },
        'type': 'farming',
        'icon': '/head/7e941987e825a24ea7baafab9819344b6c247c75c54a691987cd296bc163c263'
    },
    'MAGMA_CUBE': {
        'name': 'Magma Cube', 
        'stats': {
            'strength': lambda lvl: lvl // 5
        }, # Additonal Damage lvl * 0.25% to slimes (All), Ember Armor Stats boost lvl * 1% (Legendary)
        'type': 'combat',
        'icon': '/head/38957d5023c937c4c41aa2412d43410bda23cf79a9f6ab36b76fef2d7c429'
    },
    'FLYING_FISH': {
        'name': 'Flying Fish', 
        'stats': {
            'strength': lambda lvl: lvl // 2
        }, # Diver's Armor Stats boost lvl * 0.3% (Legendary)
        'type': 'fishing',
        'icon': '/head/40cd71fbbbbb66c7baf7881f415c64fa84f6504958a57ccdb8589252647ea'
    },
    'SQUID': {
        'name': 'Squid',
        'stats': {
        }, # lvl * 0.4 Damage and lvl * 0.2 Strength to Ink Wand (Legendary)
        'type': 'fishing',
        'icon': '/head/01433be242366af126da434b8735df1eb5b3cb2cede39145974e9c483607bac'
    },
    'PARROT': {
        'name': 'Parrot', 
        'stats': {
            'crit damage': lambda lvl: lvl // 10
        }, # lvl * 0.25 + 5 strength to nearby players (Legendary)
        'type': 'alchemy',
        'icon': '/head/5df4b3401a4d06ad66ac8b5c4d189618ae617f9c143071c8ac39a563cf4e4208'
    },
    'TIGER': {
        'name': 'Tiger', 
        'stats': {
            'strength': lambda lvl: lvl // 10 + 5,
            'crit chance': lambda lvl: lvl // 20,
            'crit damage': lambda lvl: lvl // 2
        },
        'type': 'combat',
        'icon': '/head/fc42638744922b5fcf62cd9bf27eeab91b2e72d6c70e86cc5aa3883993e9d84'
    },
    'TURTLE': {
        'name': 'Turtle', 
        'stats': {
        },
        'type': 'combat',
        'icon': '/head/212b58c841b394863dbcc54de1c2ad2648af8f03e648988c1f9cef0bc20ee23c'
    },
    'SPIDER': {
        'name': 'Spider', 
        'stats': {
            # No info :(
        },
        'type': 'unknown',
        'icon': '/head/6eab75eaa5c9f2c43a0d23cfdce35f4df632e9815001850377385f7b2f039ce1'
    },
    'BLAZE': {
        'name': 'Blaze', 
        'stats': {
        }, # Blaze Armor Stats boost lvl * 0.4% (All), 2x Hot Potato Books (Legendary),
        'type': 'combat',
        'icon': '/head/b78ef2e4cf2c41a2d14bfde9caff10219f5b1bf5b35a49eb51c6467882cb5f0'
    },
    'JERRY': {
        'name': 'Jerry', 
        'stats': {
        },
        'type': 'combat',
        'icon': '/head/822d8e751c8f2fd4c8942c44bdb2f5ca4d8ae8e575ed3eb34c18a86e93b'
    }
}

fairy_soul_hp_bonus = [
	3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8,
	8, 9, 9, 10, 10, 11, 11, 12, 12,
	13, 13, 14, 14, 15, 15, 16, 16,
	17, 17, 18, 18, 19, 19, 20, 20, 21, 21
]

skill_xp_requirements = [50, 175, 375, 675, 1175, 1925, 2925, 4425, 6425, 9925, 14925, 22425, 32425, 47425, 67425, 97425, 147425, 222425, 322425, 522425, 822425, 1222425, 1722425, 2322425, 3022425, 3822425, 4722425, 5722425, 6822425, 8022425, 9322425, 10722425, 12222425, 13822425, 15522425, 17322425, 19222425, 21222425, 23322425, 25522425, 27822425, 30222425, 32722425, 35322425, 38022425, 40822425, 43922425, 47322425, 51022425, 55022425]

runecrafting_xp_requirements = [50, 150, 275, 435, 635, 885, 1200, 1600, 2100, 2725, 3510, 4510, 5760, 7360, 9360, 11825, 14950, 18950, 23950, 30150, 37950, 47750, 59950, 75250] # Shamelessly stolen from sky.lea.moe

minion_slot_requirements = [0, 0, 0, 0, 0, 5, 15, 30, 50, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300, 350, 400, 450, 500, 550]

guild_level_requirements = [100000, 150000, 250000, 500000, 750000, 1000000, 1250000, 1500000, 2000000, 2500000, 3000000] # every level after 2.5 mil needs 3mil

tiered_talismans = {
	'BAT_RING': ['BAT_ARTIFACT'],
	'BAT_TALISMAN': ['BAT_RING', 'BAT_ARTIFACT'],
	'CANDY_RING': ['CANDY_ARTIFACT'],
	'CANDY_TALISMAN': ['CANDY_RING', 'CANDY_ARTIFACT'],
	'CROOKED_ARTIFACT': ['SEAL_OF_THE_FAMILY'],
	'FEATHER_RING': ['FEATHER_ARTIFACT'],
	'FEATHER_TALISMAN': ['FEATHER_RING', 'FEATHER_ARTIFACT'],
	'HEALING_TALISMAN': ['HEALING_RING'],
	'HUNTER_TALISMAN': ['HUNTER_RING'],
	'INTIMIDATION_RING': ['INTIMIDATION_ARTIFACT'],
	'INTIMIDATION_TALISMAN': ['INTIMIDATION_RING', 'INTIMIDATION_ARTIFACT'],
	'POTION_AFFINITY_TALISMAN': ['RING_POTION_AFFINITY', 'ARTIFACT_POTION_AFFINITY'],
	'RED_CLAW_RING': ['RED_CLAW_ARTIFACT'],
	'RED_CLAW_TALISMAN': ['RED_CLAW_RING', 'RED_CLAW_ARTIFACT'],
	'RING_POTION_AFFINITY': ['ARTIFACT_POTION_AFFINITY'],
	'SEA_CREATURE_RING': ['SEA_CREATURE_ARTIFACT'],
	'SEA_CREATURE_TALISMAN': ['SEA_CREATURE_RING', 'SEA_CREATURE_ARTIFACT'],
	'SHADY_RING': ['CROOKED_ARTIFACT', 'SEAL_OF_THE_FAMILY'],
	'SPIDER_RING': ['SPIDER_ARTIFACT'],
	'SPIDER_TALISMAN': ['SPIDER_RING', 'SPIDER_ARTIFACT'],
	'WOLF_TALISMAN': ['WOLF_RING'],
	'ZOMBIE_RING': ['ZOMBIE_ARTIFACT'],
	'ZOMBIE_TALISMAN': ['ZOMBIE_RING', 'ZOMBIE_ARTIFACT']
 }
		
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

class SkyblockError(Exception):
	"""A general exception from the skyblock library"""


class NeverPlayedSkyblockError(SkyblockError):
	"""This user has never played skyblock before!"""
		
class ExternalAPIError(SkyblockError):
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
	
class LoadError(SkyblockError):
	"""You tried to load a module that was already loaded"""
	def __init__(self, reason): 
		self.reason = reason

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
				raise BadNameError(f'Malformed uuid or username {uname_or_uuid}')
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
							raise BadNameError('Malformed uuid or username') from None
							
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
				raise ExternalAPIError('You are being ratelimited by api.mojang.com') from None
		else:
			raise BadNameError('Malformed uuid or username') from None

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
				raise LoadError(f'You tried to load module {load}, but it was already loaded!')
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
					
				elif data['cause'] == 'Key throttle!':
					await asyncio.sleep(0.5)
					return await self.__call_api__(api, **kwargs)
					
				elif data['cause'] == 'Invalid API key!':
					raise APIKeyError(f'Invalid key {kwargs["key"]}!')
					
				elif data['cause'] == 'Internal error':
					raise HypixelInternalError(f'Hypixel\'s servers could not complete your request')
					
				else:
					raise ExternalAPIError(data['cause'])
		except asyncio.TimeoutError:
			return await self.__call_api__(api, **kwargs)
	
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
				raise BadNameError('Bad guildname')
			self.data = (await self.__call_api__('/guild', id=self.gid))['guild']
		else:
			raise SkyblockError('You need to provide either a guildname or guild id!')

		if self.data is None:
			raise BadNameError('Bad guildname')

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
		for player in asyncio.as_completed([Player(self._api_keys, uuid=member['uuid']) for member in self.data['members']]):
			try:
				player = await player
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
			raise SkyblockError('You need to provide either a minecraft username or uuid!')

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
				except HypixelInternalError:
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
				except HypixelInternalError:
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
					('fishing', 'skyblock_angler')
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
			raise SkyblockError('This player already has their profile set!')
		self._profile_set = True
		
		self.__loads__ = {
			'pets': False,
			'inventories': False,
			'collections': False,
			'skills slayers': False,
			'deaths': False,
			'banking': False,
			'misc': False
		}
		
		self.profile = profile
		for cute_name, id in self.profiles.items():
			if id == profile:
				self.profile_name = cute_name
				break
		else:
			raise SkyblockError('Invalid profile ID!')

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