import random

def create_player(name):

    if name == '' or name == ' ':
        name = 'Hero'

    player = {
        'name': name,
        'max_hp': 10,
        'current_hp': 10,
        'armour': 0.00,
        'min_dmg': 2,
        'max_dmg': 7,
        'crit_chance': 10,
        'crit_mult': 2,
        'mp': 3,
        'max_mp': 3,
        'speed': 1,
        'act_item': None
    }
    return player

def player_attack(player):

    player_damage = random.randint(player['min_dmg'], player['max_dmg'])
    crit_roll = random.randint(1, 100)

    if crit_roll <= player['crit_chance']:
        player_damage *= player['crit_mult']
        
    else:
        player_damage = player_damage

    return player_damage

def player_fireball(player):
    player_damage = 8
    crit_roll = random.randint(1, 100)

    if crit_roll <= player['crit_chance']:
        player_damage *= player['crit_mult']

    else:
        player_damage = player_damage

    return player_damage

def player_heal(player):
    heal_amnt = random.randint(5, 7)
    return heal_amnt