import random

def create_player(name):

    if name == '' or name == ' ':
        name = 'Hero'

    player = {
        'name': name,
        'max_hp': 10,
        'current_hp': 10,
        'min_dmg': 1,
        'max_dmg': 7,
        'crit_chance': 20,
        'crit_mult': 2
    }
    return player

def player_attack(player):

    player_damage = random.randint(player['min_dmg'], player['max_dmg'])
    crit_roll = random.randint(1, 100)

    if crit_roll <= player['crit_chance']:
        player_damage *= player['crit_mult']
        print(f"Critical hit! {player['name']} dealt {player_damage} damage!")

    else:
        print(f"{player['name']} dealt {player_damage} damage.")

    return player_damage

