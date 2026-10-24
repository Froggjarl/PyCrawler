import random


loot_table = ['Mana Potion', 'Health Potion', 'Sturdy Sword', 'Sturdy Shield', 'Flashbang', 'Uber Bomb', 'Hermes Slippers']

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

    elif loot == loot_table[4]:
        player['act_item'] = 'Flashbang'
        desc = "Maybe this could stun an enemy..."

    elif loot == loot_table[5]:
        player['act_item'] = 'Uber Bomb'
        desc = "This looks powerful... maybe a little too powerful..."

    elif loot == loot_table[6]:
        player['speed'] += 1
        desc = f"{player['name']}'s speed was increased"

    return loot, desc
