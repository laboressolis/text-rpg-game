import random

class Player:
    def __init__(self, name, health, attack, defense, mana, stamina):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.mana = mana
        self.stamina = stamina
        self.inventory = {"Health Potion": 0, "Mana Potion": 0, "Stamina Potion": 0, "Defense Potion": 0}

    def regenerate(self):
        self.mana += 10
        self.stamina += 15
    def use_item(self,item_name):
        if self.inventory[item_name] > 0:
            self.inventory[item_name] -= 1
            return True
        else:
            print(f"You don't have any {item_name}.\n")
            return False
        

    
