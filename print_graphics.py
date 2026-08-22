from pathlib import Path

gob_path = Path(__file__).parent / "assets" / "enemies" / "gob.txt"
wiz_path = Path(__file__).parent / "assets" / "enemies" / "wizard.txt"
slime_path = Path(__file__).parent / "assets" / "enemies" / "slime.txt"

def print_enemy(enemy):
    if enemy['name'] == 'Goblin':
        with open(gob_path, 'r', encoding='utf-8') as gob:
            print(gob.read())

    elif enemy['name'] == 'Slime':
        with open(slime_path, 'r', encoding='utf-8') as slime:
            print(slime.read())

    elif enemy['name'] == 'Wizard':
        with open(wiz_path, 'r', encoding='utf-8') as wiz:
            print(wiz.read())

