
def create_player(name='Hero'):

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

