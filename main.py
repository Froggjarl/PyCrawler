import random
from player import create_player
from player import player_attack
from player import player_fireball
from enemies import create_ran_enemy
from enemies import enemy_attack
from enemies import enemy_types
from loot import gen_loot
from loot import loot_table
#from print_graphics import print_enemy

xp = 0
score = 0


print("""
██████╗ ██╗   ██╗ ██████╗██████╗  █████╗ ██╗    ██╗██╗     ███████╗██████╗ 
██╔══██╗╚██╗ ██╔╝██╔════╝██╔══██╗██╔══██╗██║    ██║██║     ██╔════╝██╔══██╗
██████╔╝ ╚████╔╝ ██║     ██████╔╝███████║██║ █╗ ██║██║     █████╗  ██████╔╝
██╔═══╝   ╚██╔╝  ██║     ██╔══██╗██╔══██║██║███╗██║██║     ██╔══╝  ██╔══██╗
██║        ██║   ╚██████╗██║  ██║██║  ██║╚███╔███╔╝███████╗███████╗██║  ██║
╚═╝        ╚═╝    ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚══╝╚══╝ ╚══════╝╚══════╝╚═╝  ╚═╝
""")

player = create_player(input('Choose a name for your character: '))

while player['current_hp'] > 0:

    enemy_defeated = False

    enemy = create_ran_enemy(random.choice(enemy_types))

    print(f"{player['name']} encountered a {enemy['name']}!")

    #print_enemy(enemy)

    while player['current_hp'] > 0 and enemy_defeated == False:
        print(f'\nHP: {player['current_hp']}/{player['max_hp']}')
        print(f'MP: {'/' * player['mp']}')
        print(f'XP: {xp}')
        print(f"What will {player['name']} do?\n[1] Attack\n[2] Fireball Spell")
        player_act = input(': ')

        if player_act not in ['1', '2']:
            print("\nYou can't do nothing!")
            continue

        if player_act == '1':
            player_damage = player_attack(player)
            enemy['current_hp'] -= player_damage
            print(f"\n{player['name']} dealt {player_damage} damage to {enemy['name']}! {enemy['name']} has {enemy['current_hp']} HP left.")

        if player_act == '2':
            if player['mp'] <= 0:
                print("\nYou don't have enough mana to cast Fireball!")
                continue
            else:
                player['mp'] -= 1
                player_damage = player_fireball(player)
                enemy['current_hp'] -= player_damage
                print(f"\n{player['name']} cast Fireball and dealt {player_damage} damage to {enemy['name']}! {enemy['name']} has {enemy['current_hp']} HP left.")

        if enemy['current_hp'] <= 0:
            print(f"\n{enemy['name']} has been defeated!\n")
            score += 1
            xp += 1

            if xp % 3 == 0:
                loot = gen_loot(loot_table, player)
                print(f"{player['name']} found a {loot}!\n")

            enemy_defeated = True
            break

        enemy_damage = int(enemy_attack(enemy))
        player['current_hp'] -= enemy_damage
        print(f"\n{enemy['name']} dealt {enemy_damage} damage to {player['name']}!")
        if player['current_hp'] <= 0:
            break

if player['current_hp'] <= 0:
        print(f"\n{player['name']} has been defeated by {enemy['name']}! Game Over.")
        print(f"Final score: {score}")
        