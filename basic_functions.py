import os
import sys
import time
import random
import msvcrt
from enemy_class import Enemy


def clear_screen():
    '''Clears The Screen'''
    os.system('cls')

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

def speechbreak():
    print("Press any key to continue....", end='')
    msvcrt.getch()

def load_enemies(filename):
    enemies = []
    with open(filename, 'r') as file:
        for line in file:
            name, health, attack, defense = line.strip().split(',')
            enemies.append(Enemy(name,int(health), int(attack), int(defense)))
        return enemies
    
def load_items(filename):
    items = {}
    with open(filename, 'r') as file:
        for line in file:
            item_id, item_name = line.strip().split(',')
            items[int(item_id)] = item_name
    return items

def createcharacter():
    pass


def newline():
    print()
