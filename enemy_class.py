import random

class Enemy:
    def __init__(self, health, max_health, attack, type):
        self.health = health
        self.max_health = max_health
        self.attack = attack
        self.type = type

    def isEnemyalive(self):
        if self.health > 0:
            return True
        else:
            return False
    def add_hp(self, value):
        self.health = min(self.health + value, self.max_health)
    
    def remove_health(self, value):
        self.health = max(self.health - value, 0)
    
    

