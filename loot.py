import random


loot_table = ['Mana Potion', 'Health Potion', 'Sturdy Sword', 'Sturdy Shield', 'Mana Gem']

def gen_loot(loot_table, player):
    loot = random.choice(loot_table)

    if loot == loot_table[0]:
        player['mp'] = 3

    elif loot == loot_table[1]:
        player['current_hp'] = player['max_hp']

    elif loot == loot_table[2]:
        player['min_dmg'] += 1

    elif loot == loot_table[3]:
        player['max_hp'] += 2
        player['current_hp'] += 4

    elif loot == loot_table[4]:
        player['mp'] += 3

    return loot

