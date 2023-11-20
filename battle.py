from player_class import Player
from enemy_class import Enemy
from basic_functions import items, enemies
from basic_functions import clear_screen, typing, fasttyping
import random

random_enemy = random.choice(enemies)
player = Player('icy', 'physical',50,50,50)

def battle(enemy, player):
    fasttyping(f"You have encountered {enemy.name}({enemy.health}). \n")
    while enemy.isEnemyAlive() and player.isPlayerAlive():
        print('1. Attack')
        print('2. Defend')
        print('3. Flee')
        x = input()

battle(random_enemy, player)