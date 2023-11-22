import os
import sys
import json
import time
import random
import msvcrt
from enemy_class import Enemy



def clear_screen():
    '''Clears The Screen'''
    os.system('cls')

def clear_lines(num_lines):
    for _ in range(num_lines):
        print("\033[F\033[K", end="") 
    sys.stdout.flush()

def typing(message):
    '''Typing Mech'''
    for letter in message:
        time.sleep(random.choice([0.3, 0.11, 0.08, 0.07,0.07, 0.07, 0.06, 0.06, 0.05, 0.01]))
        sys.stdout.write(letter)
        sys.stdout.flush()
    time.sleep(.1)
    return ""

def fasttyping(message):
    for letter in message:
        time.sleep(random.choice([0.11, 0.01, 0.08, 0.01,0.01, 0.07, 0.06, 0.06, 0.05, 0.01]))
        sys.stdout.write(letter)
        sys.stdout.flush()
    time.sleep(.1)
    return ''

def reallyfasttyping(message):
    for letter in message:
        time.sleep(random.choice([0.01, 0.01, 0.08, 0.001, 0.01, 0.007, 0.06, 0.007, 0.005, 0.01]))
        sys.stdout.write(letter)
        sys.stdout.flush()
    time.sleep(.1)
    return ''

def speechbreak():
    print("Press any key to continue....", end='')
    msvcrt.getch()

def load_items():
    with open(r'Data\items.json', 'r') as file:
        loaded_items = json.load(file)
        return loaded_items

def load_physical_skills():
    with open(r'Data\physical_skill_tree.json', 'r') as file:
        loaded_skill_tree = json.load(file)
        return loaded_skill_tree
    
def load_magical_skills():
    with open(r'Data\magical_skill_tree.json', 'r') as file:
        loaded_skill_tree = json.load(file)
        return loaded_skill_tree

def load_enemies():
    with open(r'Data\enemies.json', 'r') as file:
        loaded_enemies = json.load(file)
        enemies = [Enemy(enemy['name'], enemy['health'], enemy['max_health'],
                         enemy['attack'], enemy['type']) for enemy in loaded_enemies]
        return enemies


def createcharacter():
    pass

def newline():
    print()


items = load_items()

enemies = load_enemies()