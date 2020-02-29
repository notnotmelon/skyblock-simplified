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

'''
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

def xp_slice(start):
    if start != 0:
        diff = pet_xp[start - 1]
    else:
        diff = 0
        
    return [xp - diff for xp in pet_xp[start:start+100]]

pet_xp = {'common': xp_slice(0), 'uncommon': xp_slice(6), 'rare': xp_slice(11), 'epic': xp_slice(16), 'legendary': xp_slice(20)}
'''

pet_xp = {
    'common': [
        0, 100, 210, 330, 460, 605, 765, 940,
        1130, 1340, 1570, 1820, 2095, 2395, 2725, 3085,
        3485, 3925, 4415, 4955, 5555, 6215, 6945, 7745,
        8625, 9585, 10635, 11785, 13045, 14425, 15935,
        17585, 19385, 21345, 23475, 25785, 28285, 30985,
        33905, 37065, 40485, 44185, 48185, 52535, 57285,
        62485, 68185, 74485, 81485, 89285, 97985, 107685,
        118485, 130485, 143785, 158485, 174685, 192485,
        211985, 233285, 256485, 281685, 309085, 338885, 
        371285, 406485, 444685, 486085, 530885, 579285, 
        631485, 687685, 748085, 812885, 882285, 956485,
        1035685, 1120385, 1211085, 1308285, 1412485, 
        1524185, 1643885, 1772085, 1909285, 2055985,
        2212685, 2380385, 2560085, 2752785, 2959485,
        3181185, 3418885, 3673585, 3946285, 4237985,
        4549685, 4883385, 5241085, 5624785], 
    'uncommon': [
        160, 335, 525, 735, 965, 1215, 
        1490, 1790, 2120, 2480, 2880, 3320, 3810, 
        4350, 4950, 5610, 6340, 7140, 8020, 8980, 
        10030, 11180, 12440, 13820, 15330, 16980, 
        18780, 20740, 22870, 25180, 27680, 30380, 
        33300, 36460, 39880, 43580, 47580, 51930, 
        56680, 61880, 67580, 73880, 80880, 88680, 
        97380, 107080, 117880, 129880, 143180, 
        157880, 174080, 191880, 211380, 232680, 
        255880, 281080, 308480, 338280, 370680, 
        405880, 444080, 485480, 530280, 578680, 
        630880, 687080, 747480, 812280, 881680, 
        955880, 1035080, 1119780, 1210480, 1307680, 
        1411880, 1523580, 1643280, 1771480, 1908680, 
        2055380, 2212080, 2379780, 2559480, 2752180, 
        2958880, 3180580, 3418280, 3672980, 3945680, 
        4237380, 4549080, 4882780, 5240480, 5624180,
        6035880, 6477580, 6954280, 7470980, 8032680,
        8644380
    ], 
    'rare': [
        250, 525, 825, 1155, 1515, 1915, 2355,
        2845, 3385, 3985, 4645, 5375, 6175, 7055, 8015,
        9065, 10215, 11475, 12855, 14365, 16015, 17815,
        19775, 21905, 24215, 26715, 29415, 32335, 35495,
        38915, 42615, 46615, 50965, 55715, 60915, 66615,
        72915, 79915, 87715, 96415, 106115, 116915, 
        128915, 142215, 156915, 173115, 190915, 210415,
        231715, 254915, 280115, 307515, 337315, 369715,
        404915, 443115, 484515, 529315, 577715, 629915, 
        686115, 746515, 811315, 880715, 954915, 1034115, 
        1118815, 1209515, 1306715, 1410915, 1522615,
        1642315, 1770515, 1907715, 2054415, 2211115, 
        2378815, 2558515, 2751215, 2957915, 3179615,
        3417315, 3672015, 3944715, 4236415, 4548115, 
        4881815, 5239515, 5623215, 6034915, 6476615, 
        6953315, 7470015, 8031715, 8643415, 9310115, 
        10036815, 10828515, 11690215, 12626915
    ], 
    'epic': [
        400, 840, 1330, 1870, 2470, 3130, 3860,
        4660, 5540, 6500, 7550, 8700, 9960, 11340, 12850,
        14500, 16300, 18260, 20390, 22700, 25200, 27900,
        30820, 33980, 37400, 41100, 45100, 49450, 54200,
        59400, 65100, 71400, 78400, 86200, 94900, 104600,
        115400, 127400, 140700, 155400, 171600, 189400, 
        208900, 230200, 253400, 278600, 306000, 335800, 
        368200, 403400, 441600, 483000, 527800, 576200, 
        628400, 684600, 745000, 809800, 879200, 953400,
        1032600, 1117300, 1208000, 1305200, 1409400, 
        1521100, 1640800, 1769000, 1906200, 2052900, 
        2209600, 2377300, 2557000, 2749700, 2956400, 
        3178100, 3415800, 3670500, 3943200, 4234900, 
        4546600, 4880300, 5238000, 5621700, 6033400, 
        6475100, 6951800, 7468500, 8030200, 8641900, 
        9308600, 10035300, 10827000, 11688700, 12625400, 
        13642100, 14743800, 15935500, 17222200, 18608900
    ], 
    'legendary': [
        600, 1260, 1990, 2790, 3670, 4630, 
        5680, 6830, 8090, 9470, 10980, 12630, 14430, 16390,
        18520, 20830, 23330, 26030, 28950, 32110, 35530,
        39230, 43230, 47580, 52330, 57530, 63230, 69530,
        76530, 84330, 93030, 102730, 113530, 125530, 138830,
        153530, 169730, 187530, 207030, 228330, 251530, 276730,
        304130, 333930, 366330, 401530, 439730, 481130, 525930,
        574330, 626530, 682730, 743130, 807930, 877330, 951530,
        1030730, 1115430, 1206130, 1303330, 1407530, 1519230,
        1638930, 1767130, 1904330, 2051030, 2207730, 2375430,
        2555130, 2747830, 2954530, 3176230, 3413930, 3668630,
        3941330, 4233030, 4544730, 4878430, 5236130, 5619830,
        6031530, 6473230, 6949930, 7466630, 8028330, 8640030,
        9306730, 10033430, 10825130, 11686830, 12623530, 13640230,
        14741930, 15933630, 17220330, 18607030, 20103730, 21720430,
        23467130, 25353830
    ]
}

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
