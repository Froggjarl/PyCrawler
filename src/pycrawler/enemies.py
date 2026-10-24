import random

# remeber, easy crashes come from an unused enemy type, so make sure every enemy type actaully has a stat dictionary
enemy_types = ['slime', 'goblin', 'wizard', 'goober', 'troll'] # Enemy list

def create_ran_enemy(type):

    if type == 'slime':
        enemy = {
            'name': '\033[1m'+'Slime'+'\033[0m',
            'max_hp': 7,
            'current_hp': 7,
            'min_dmg': 1,
            'max_dmg': 3,
            'crit_chance': 5,
            'crit_mult': 1.3,
            'speed': 1
        }
    elif type == 'goblin':
        enemy = {
            'name': '\033[1m'+'Goblin'+'\033[0m',
            'max_hp': 10,
            'current_hp': 10,
            'min_dmg': 2,
            'max_dmg': 3,
            'crit_chance': 10,
            'crit_mult': 1.3,
            'speed': 1
        }
    elif type == 'wizard':
        enemy = {
            'name': '\033[1m'+'Wizard'+'\033[0m',
            'max_hp': 8,
            'current_hp': 8,
            'min_dmg': 3,
            'max_dmg': 5,
            'crit_chance': 15,
            'crit_mult': 1.3,
            'speed': 1
        }
    elif type == 'goober':
        enemy = {
            'name': '\033[1m'+'Goober'+'\033[0m',
            'max_hp': 5,
            'current_hp': 5,
            'min_dmg': 1,
            'max_dmg': 2,
            'crit_chance': 10,
            'crit_mult': 1.3,
            'speed': 2
        }
    elif type == 'troll':
        enemy = {
            'name': '\033[1m'+'Troll'+'\033[0m',
            'max_hp': 12,
            'current_hp': 12,
            'min_dmg': 4,
            'max_dmg': 6,
            'crit_chance': 10,
            'crit_mult': 1.3,
            'speed': 0.5
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

