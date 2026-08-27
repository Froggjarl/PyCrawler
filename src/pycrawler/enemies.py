import random

enemy_types = ['slime', 'goblin', 'wizard']

def create_ran_enemy(type):

    if type == 'slime':
        enemy = {
            'name': 'Slime',
            'max_hp': 7,
            'current_hp': 7,
            'min_dmg': 1,
            'max_dmg': 3,
            'crit_chance': 5,
            'crit_mult': 1.3
        }
    elif type == 'goblin':
        enemy = {
            'name': 'Goblin',
            'max_hp': 10,
            'current_hp': 10,
            'min_dmg': 2,
            'max_dmg': 3,
            'crit_chance': 10,
            'crit_mult': 1.3
        }
    elif type == 'wizard':
        enemy = {
            'name': 'Wizard',
            'max_hp': 8,
            'current_hp': 8,
            'min_dmg': 3,
            'max_dmg': 5,
            'crit_chance': 15,
            'crit_mult': 1.3
        }
    return enemy

def enemy_attack(enemy):

    enemy_damage = random.randint(enemy['min_dmg'], enemy['max_dmg'])
    crit_roll = random.randint(1, 100)

    if crit_roll <= enemy['crit_chance']:
        enemy_damage *= enemy['crit_mult']
        
    else:
        enemy_damage = enemy_damage

    return enemy_damage

