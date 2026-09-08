import random
import os
from importlib.metadata import version, metadata
from .player import create_player
from .player import player_attack
from .player import player_fireball
from .player import player_heal
from .enemies import create_ran_enemy
from .enemies import enemy_attack
from .enemies import enemy_types
from .loot import gen_loot
from .loot import loot_table
#from print_graphics import print_enemy
from .print_graphics import clear_all

def main(): # Battle Logic
    pkg_version = version('pycrawler-roguelike')

    uber_bomb = None
    xp = 0
    score = 0
    enemy_skip = 0
    player_skip = 0

    clear_all()

    print(f"""
██████╗ ██╗   ██╗ ██████╗██████╗  █████╗ ██╗    ██╗██╗     ███████╗██████╗ 
██╔══██╗╚██╗ ██╔╝██╔════╝██╔══██╗██╔══██╗██║    ██║██║     ██╔════╝██╔══██╗
██████╔╝ ╚████╔╝ ██║     ██████╔╝███████║██║ █╗ ██║██║     █████╗  ██████╔╝
██╔═══╝   ╚██╔╝  ██║     ██╔══██╗██╔══██║██║███╗██║██║     ██╔══╝  ██╔══██╗
██║        ██║   ╚██████╗██║  ██║██║  ██║╚███╔███╔╝███████╗███████╗██║  ██║
╚═╝        ╚═╝    ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚══╝╚══╝ ╚══════╝╚══════╝╚═╝  ╚═╝
Version: {pkg_version}
    """)

    player = create_player(input('Choose a name for your character: '))

    clear_all()

    while player['current_hp'] > 0:

        if uber_bomb != None:
            print(uber_bomb)
            uber_bomb = None
        else:
            pass

        if xp % 3 == 0 and xp > 0:
            loot, desc = gen_loot(loot_table, player)
            print(f"{player['name']} found a {loot}! {desc}\n")

        if xp % 4 == 0 and xp > 0:
            player['mp'] += 1

        enemy_defeated = False

        enemy = create_ran_enemy(random.choice(enemy_types))

        print(f"{player['name']} encountered a {enemy['name']}!")

        #print_enemy(enemy)

        while player['current_hp'] > 0 and enemy_defeated == False:
            print(f'\nHP: {player['current_hp']}/{player['max_hp']}')
            print(f'MP: {'/' * player['mp']}')
            print(f'XP: {xp}')
            print(f"What will {player['name']} do?\n[1] Attack\n[2] Fireball Spell\n[3] Heal Spell\n[4] {player['act_item']}")
            player_act = input(': ')

            if player_act not in ['1', '2', '3', '4']:
                print("\nInvalid Action.")
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

            if player_act == '3':
                if player['mp'] < 1:
                    print("\nYou don't have enough mana to cast Heal!")
                    continue
                else:
                    if player['current_hp'] >= player['max_hp']:
                        print("\nAlready at max HP")
                        continue
                    else:
                        heal = min(9, player['max_hp'] - player['current_hp'])
                        player['mp'] -= 1
                        player['current_hp'] += heal
                        #if player['current_hp'] > player['max_hp']:
                            #player['current_hp'] = player['max_hp']
                            #print(f"\n{player['name']} healed {player['current_hp'] - heal} HP")
                        #else:
                        print(f"\n{player['name']} healed {heal} HP")

            if player_act == '4':
                if player['act_item'] == 'Flashbang':
                    enemy_skip = 2
                    player['act_item'] = None
                    print(f"\n{player['name']} used a Flashbang! {enemy['name']} is stunned.")

                elif player['act_item'] == 'Uber Bomb':
                    enemy['current_hp'] = 0
                    player['current_hp'] -= 1
                    player['act_item'] = None
                    uber_bomb = f"{player['name']} used the Uber Bomb! {enemy['name']} was annihilated, but it was pretty big, so {player['name']} was hurt a bit too.\n"
                else:
                    print("\nYou don't have an item to use!")
                    continue
                
            if enemy['current_hp'] <= 0:
                clear_all()
                print(f"\n{enemy['name']} has been defeated!\n")
                score += 1
                xp += 1
                enemy_defeated = True
                break

            if enemy_skip > 0:
                enemy_skip -= 1
                print(f"\n{enemy['name']}'s turn was skipped!")
                continue
            
            enemy_damage = round((enemy_attack(enemy)))
            player['current_hp'] -= round((enemy_damage - (enemy_damage * player['armour'])))
            print(f"\n{enemy['name']} dealt {enemy_damage} damage to {player['name']}!")

            if player['current_hp'] <= 0:
                break

    if player['current_hp'] <= 0:
        clear_all()
        print(f"\n{player['name']} has been defeated by a {enemy['name']}! Game Over.")
        print(f"Final score: {score}")


if __name__ == "__main__":
    main()