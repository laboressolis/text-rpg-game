import random


class Enemy:
    def __init__(self, name, health, attack, defense, item_drops = None):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.item_drop = item_drops or []
    def is_alive(self):
        return self.health > 0
    def damage(self, damage):
        self.health = max(0, self.health - damage)
    def drop_items(self):
        return random.choice(self.item_drops) if self.item_drops else None