import json

""" 

items = {
    '1':{'id': '1', 'type': 'weapon', 'name': 'Excalibur','attack': 50, 'defense': 10, 'class': 'physical'},
    '2': {'id': '2', 'type': 'armor', 'name': 'Dragonplate Shield', 'attack': 0, 'defense': 30, 'class': 'physical'},
    '3': {'id': '3', 'type': 'potion', 'name': 'Elixir of Vitality', 'healing': 30, 'class': 'healing'},
    '4': {'id': '4', 'type': 'weapon', 'name': 'Stormcaller', 'attack': 40, 'defense': 5, 'class': 'magical'},
    '5': {'id': '5', 'type': 'armor', 'name': 'Spectral Robes', 'attack': 10, 'defense': 25, 'class': 'magical'},
    '6': {'id': '6', 'type': 'consumable', 'name': 'Smoke Bomb', 'effect': 'Invisibility', 'class': 'utility'}
}

with open('items.json', 'w') as file:
    json.dump(items, file, indent=4) 

"""


def load_skills():
    with open('Data\items.json', 'r') as file:
        loaded_items = json.load(file)
        return loaded_items
    
x = load_skills()
print(x)

