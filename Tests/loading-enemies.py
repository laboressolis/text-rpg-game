import json
from enemy_class import Enemy
def load_skills():
    with open('Data\enemies.json', 'r') as file:
        loaded_enemies = json.load(file)
        enemies = [Enemy(enemy['name'], enemy['health'], enemy['max_health'],
                         enemy['attack'], enemy['type']) for enemy in loaded_enemies]
        return enemies
    

r = load_skills()

print(r)






""" import json


enemies = [
    {'name': 'Orc', 'health': 240, 'max_health': 240, 'attack': 50, 'type': 'elite'},
    {'name': 'Goblin', 'health': 120, 'max_health': 120, 'attack': 25, 'type': 'normal'},
    {'name': 'Troll', 'health': 300, 'max_health': 300, 'attack': 40, 'type': 'elite'},
    {'name': 'Skeleton', 'health': 80, 'max_health': 80, 'attack': 30, 'type': 'normal'},
    {'name': 'Dark Knight', 'health': 350, 'max_health': 350, 'attack': 60, 'type': 'boss'},
    {'name': 'Spider', 'health': 100, 'max_health': 100, 'attack': 20, 'type': 'normal'},
    {'name': 'Witch', 'health': 180, 'max_health': 180, 'attack': 45, 'type': 'elite'},
    {'name': 'Ghost', 'health': 150, 'max_health': 150, 'attack': 35, 'type': 'normal'},
    {'name': 'Dragon', 'health': 500, 'max_health': 500, 'attack': 80, 'type': 'boss'},
    {'name': 'Harpy', 'health': 200, 'max_health': 200, 'attack': 55, 'type': 'elite'},
    {'name': 'Zombie', 'health': 120, 'max_health': 120, 'attack': 25, 'type': 'normal'},
    {'name': 'Minotaur', 'health': 280, 'max_health': 280, 'attack': 50, 'type': 'elite'},
    {'name': 'Werewolf', 'health': 180, 'max_health': 180, 'attack': 40, 'type': 'normal'},
    {'name': 'Vampire', 'health': 220, 'max_health': 220, 'attack': 60, 'type': 'elite'},
    {'name': 'Slime', 'health': 80, 'max_health': 80, 'attack': 15, 'type': 'normal'},
    {'name': 'Specter', 'health': 130, 'max_health': 130, 'attack': 30, 'type': 'normal'},
    {'name': 'Chimera', 'health': 400, 'max_health': 400, 'attack': 70, 'type': 'boss'},
    {'name': 'Banshee', 'health': 160, 'max_health': 160, 'attack': 35, 'type': 'normal'},
    {'name': 'Demon', 'health': 300, 'max_health': 300, 'attack': 65, 'type': 'elite'},
]

with open('enemies.json', 'w') as file:
    json.dump(enemies, file, indent=4)
 """

""" class Enemy:
    def __init__(self,name ,health, max_health, attack, type):
        self.name = name
        self.health = health
        self.max_health = max_health
        self.attack = attack
        self.type = type
         """