import random

class Enemy:
    def __init__(self,name ,health, max_health, attack, type):
        self.name = name
        self.health = health
        self.max_health = max_health
        self.attack = attack
        self.type = type

    def isEnemyAlive(self):
        if self.health > 0:
            return True
        else:
            return False
    
    def isEnraged(self):
        # if health is less than 20% of max health
        if self.health > (self.max_health * 0.2):
            random_number = random.uniform(0,1)
            probability = 0.1
            if random_number < probability:
                print(f'{self.name} is enranged.')
                self.health += 50
                self.attack += 30

    def add_hp(self, value):
        self.health = min(self.health + value, self.max_health)
    
    def remove_hp(self, value):
        self.health = max(self.health - value, 0)

    
    

