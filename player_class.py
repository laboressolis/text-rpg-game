import random
import os

class Player:
    def __init__(self, name, player_class, max_stamina, max_mana, max_defense, base_attack):
        self.name = name
        self.player_class = player_class
        self.player_subclass = None
        self.level = 1
        self.skill_points = 0
        self.coin = 0
        self.equipment = {'weapon': None, 'head': None, 'chest': None, 'pants': None, 'boots': None, 'hands': None}

        # Stats
        self.base_attack = base_attack

        self.max_health = 100
        self.health = self.max_health
        self.health_regen = 10

        self.max_stamina = max_stamina
        self.stamina = self.max_stamina
        self.stamina_regen = 10

        self.max_mana = max_mana
        self.mana = self.max_mana
        self.mana_regen = 10
        
        self.max_defense = max_defense
        self.defense = self.max_defense

        # Inventory
        # Potion template {Type:count}
        self.potion_inventory = {'health_potion': 3, 'mana_potion': 2, 'defense_potion': 1}
        # Equipment template {EQUIPID:{type:value,name:name,attack:value,defense:value,class:value}}
        # How to distinguish b/w weapon and equips??
        # NEW TEMPLATE
        # {EQUIPID: {id: value, type: string, name: string, attack: value, defense: value, class: string}}
        self.equipment_inventory = {1:{'id': 1, 'type': 'weapon', 'name': 'Excalibur','attack': 20, 'defense': 0, 'class': 'physical'}}

    def player_status(self):
        print(f"\n{'*' * 30}")
        print(f"{'*' * 10} PLAYER STATUS {'*' * 10}")
        print(f"{'*' * 30}\n")
        
        print(f"Player: {self.name}")
        print(f"Class: {self.player_class}")
        print(f"Level: {self.level}")
        print(f"{'-' * 30}")
        print(f"Health: {self.health}/{self.max_health} (+{self.health_regen} regen)")
        print(f"Stamina: {self.stamina}/{self.max_stamina} (+{self.stamina_regen} regen)")
        print(f"Mana: {self.mana}/{self.max_mana} (+{self.mana_regen} regen)")
        print(f"Defense: {self.defense}/{self.max_defense}")
        print(f"{'-' * 30}")
        print(f"Base Attack: {self.base_attack}")
        print(f"Coins: {self.coin}")
        print(f"Skill Points: {self.skill_points}")
        
        print("\nEquipment:")
        for slot, item in self.equipment.items():
            print(f"  {slot.capitalize()}: {item}")
        
        print(f"\n{'*' * 30}\n")

    def display_player_status(self):
        print(f"")

    def display_equipment_inventory(self):
        print("Equipment Inventory:")
        for equipment_id, equipment in self.equipment_inventory.items():
            print(f"{equipment_id}: {equipment['name']} - Type: {equipment['type']}, Attack: {equipment['attack']}, Defense: {equipment['defense']}, Class: {equipment['class']}")

    def display_potion_inventory(self):
        print("Potion Inventory:")
        for i, (item, quantity) in enumerate(self.potion_inventory.items(), 1):
            print(f"{i}. {item} ({quantity})")

# player = Player('icy','physical',50,50,50,20)

