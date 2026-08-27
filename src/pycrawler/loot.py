import random


loot_table = ['Mana Potion', 'Health Potion', 'Sturdy Sword', 'Sturdy Shield']

def gen_loot(loot_table, player):
    loot = random.choice(loot_table)
    #Mana Potion
    if loot == loot_table[0]:
        player['mp'] = 3
        desc = f"{player['name']}'s mana was refilled"
    #Health Potion
    elif loot == loot_table[1]:
        player['current_hp'] = player['max_hp']
        desc = f"{player['name']}'s health was refilled"
    #Sturdy Sword
    elif loot == loot_table[2]:
        if player['min_dmg'] < 7:
            player['min_dmg'] += 1
            desc = f"This sword is sharper than {player['name']}'s old one"
        else:
            player['max_dmg'] += 1
            desc = f"This sword is sharper than {player['name']}'s old one"
    #Sturdy Shield
    elif loot == loot_table[3]:
        player['armour'] += 0.05
        desc = f"{player['name']}'s armour was increased"

    return loot, desc
