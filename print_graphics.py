from pathlib import Path

gob_path = Path(__file__).parent / "assets" / "enemies" / "gob.txt"
wiz_path = Path(__file__).parent / "assets" / "enemies" / "wizard.txt"
slime_path = Path(__file__).parent / "assets" / "enemies" / "slime.txt"

def print_enemy(enemy):
    if enemy['name'] == 'Goblin':
        with open(gob_path, 'r') as gob:
            print(gob.read())

    elif enemy['name'] == 'Slime':
        with open(slime_path, 'r') as slime:
            print(slime.read())

    elif enemy['name'] == 'Wizard':
        with open(wiz_path, 'r') as wiz:
            print(wiz.read())

