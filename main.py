import random

from player import create_player
from enemies import create_ran_enemy
from enemies import enemy_types

player = create_player(input('Choose a name: '))

print(player)

enemy = create_ran_enemy(random.choice(enemy_types))

print(enemy)