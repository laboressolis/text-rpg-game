""" 
items = {
    '1':{'id': '1', 'type': 'weapon', 'name': 'Excalibur','attack': 50, 'defense': 10, 'class': 'physical'},
    '2': {'id': '2', 'type': 'armor', 'name': 'Dragonplate Shield', 'attack': 0, 'defense': 30, 'class': 'physical'},
    '3': {'id': '3', 'type': 'potion', 'name': 'Elixir of Vitality', 'healing': 30, 'class': 'healing'},
    '4': {'id': '4', 'type': 'weapon', 'name': 'Stormcaller', 'attack': 40, 'defense': 5, 'class': 'magical'},
    '5': {'id': '5', 'type': 'armor', 'name': 'Spectral Robes', 'attack': 10, 'defense': 25, 'class': 'magical'},
    '6': {'id': '6', 'type': 'consumable', 'name': 'Smoke Bomb', 'effect': 'Invisibility', 'class': 'utility'}
}

item = {'1':{'id': '1', 'type': 'weapon', 'name': 'Excalibur','attack': 50, 'defense': 10, 'class': 'physical'}}
 """


""" import random

x = random.randint(5,2)
print(x) """

""" import sys
import time



def clear_last_lines(num_lines):
    for _ in range(num_lines):
        print("\033[F\033[K", end="") 
    sys.stdout.flush()
 """