import random
import os

class Player:
    def __init__(self, name, player_class, max_stamina, max_mana, base_attack):
        self.name = name
        self.player_class = player_class
        self.player_subclass = None
        self.level = 1
        self.skill_points = 0
        self.coin = 0
        self.equipment = {'weapon': None, 'head': None, 'chest': None, 'pants': None, 'boots': None, 'hands': None}

        # Stats
        self.base_attack = base_attack 
        self.defense = 10

        self.max_health = 100
        self.health = self.max_health
        self.health_regen = 10

        self.max_stamina = max_stamina
        self.stamina = self.max_stamina
        self.stamina_regen = 10

        self.max_mana = max_mana
        self.mana = self.max_mana
        self.mana_regen = 10
        # Inventory
        # Potion template {Type:count}
        self.potion_inventory = {'Health Potion(+20)': 3, 'Mana Potion(+30)': 2, 'Stamina Potion(+30)': 1}
        # Equipment template {EQUIPID:{type:value,name:name,attack:value,defense:value,class:value}}
        # How to distinguish b/w weapon and equips?? IDS!!! edit1: switched to it being "type" (weapon/head/chest/pants/boots/hands)
        # NEW TEMPLATE
        # {EQUIPID: {id: value, type: string, name: string, attack: value, defense: value, class: string}}
        self.equipment_inventory = {'1':{'id': '1', 'type': 'weapon', 'name': 'Excalibur','attack': 50, 'defense': 10, 'class': 'physical'},
                                    '2':{'id': '2', 'type': 'weapon', 'name': 'idk what to call1','attack': 30, 'defense': 10, 'class': 'physical'},
                                    '3':{'id': '3', 'type': 'weapon', 'name': 'idk what to call2','attack': 10, 'defense': 10, 'class': 'physical'}
                                    }
    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False
    
    def add_hp(self, value):
        self.health = min(self.health + value, self.max_health)
    
    def add_stamina(self, value):
        self.stamina =  min(self.stamina + value, self.max_stamina)

    def add_mana(self, value):
        self.mana =  min(self.mana + value, self.max_mana)
    
    def add_defense(self,value):
        self.defense = self.defense + value
    
    def add_attack(self, value):
        self.base_attack = self.base_attack + value
    
    def remove_health(self, value):
        self.health = max(self.health - value, 0)

    def remove_stamina(self, value):
        self.stamina = max(self.stamina - value, 0)
        if self.stamina == 0:
            print("You are exhuasted, You lose 10 hp.")
            self.remove_health(10)
            
    def remove_mana(self,value):
        self.mana = max(self.mana - value, 0)

    def remove_defense(self,value):
        self.defense = max(self.defense - value,0)
    
    def remove_attack(self,value):
        self.base_attack = self.base_attack - value
        if self.base_attack < 0:
            print("HOW YOU SO WEAK? PATHETIC LMAO")
            print("*cries in asian*")   

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
        print(f"Defense: {self.defense}")
        print(f"Attack: {self.base_attack}")
        print(f"{'-' * 30}")
        print(f"Coins: {self.coin}")
        print(f"Skill Points: {self.skill_points}")
        
        print("\nEquipment:")
        for slot, item in self.equipment.items():
            if item is None:
                print(f"  {slot.capitalize()}: {item}")
            else:
                print(f"  {slot.capitalize()}: {item['name']} | Attack:{item['attack']} | Defense:{item['defense']}")
        
        print(f"\n{'*' * 30}\n")

    def display_equipment_inventory(self):
        print("Equipment Inventory:")
        for equipment_id, equipment in self.equipment_inventory.items():
            print(f"{equipment_id}: {equipment['name']} - Type: {equipment['type']}, Attack: {equipment['attack']}, Defense: {equipment['defense']}, Class: {equipment['class']}")

    def display_potion_inventory(self):
        print("Potion Inventory:")
        for i, (item, quantity) in enumerate(self.potion_inventory.items(), 1):
            print(f"{i}. {item} ({quantity})")
    
    def equip(self, id):
        if id in self.equipment_inventory:
            if self.equipment_inventory[id]['class'] == self.player_class:
                equip = self.equipment_inventory[id]
                # to remove the item from inventory if the equipment slot is empty
                if self.equipment[equip['type']] is None:
                    self.equipment[equip['type']] = equip
                    # adding stats
                    self.add_attack(equip['attack'])
                    self.add_defense(equip['defense'])

                    del self.equipment_inventory[id]
                    print(f"You have equipped {equip['name']}.")
                # messed up equipment swapper
                else:
                    temp_equip = self.equipment[equip['type']]

                    self.equipment[equip['type']] = equip
                    # removing prev stats
                    self.remove_attack(temp_equip['attack'])
                    self.remove_defense(temp_equip['defense'])

                    self.add_attack(equip['attack'])
                    self.add_defense(equip['defense']) 

                    del self.equipment_inventory[id]
                    self.equipment_inventory[temp_equip['id']] = temp_equip
                    print(f"You have swapped {temp_equip['name']} with {equip['name']}.")
            else:
                print("You can not equip this due to class restriction.")
        else:
            print("You don't have that item in your inventory.")

    def use_potion(self, ch):
        if ch == '1':
            if self.potion_inventory['Health Potion(+20)'] != 0:
                self.add_hp(20)
                self.potion_inventory['Health Potion(+20)'] -= 1
                print("You have gained 20 hp pts.")
            else:
                print("You have 0 Health Potions.")
        if ch == '2':
            if self.potion_inventory['Mana Potion(+30)'] != 0:
                self.add_mana(30)
                self.potion_inventory['Mana Potion(+30)'] -= 1
                print("You have gained 30 mana pts.")
            else:
                print("You have 0 Mana Potions.")
        if ch == '3':
            if self.potion_inventory['Stamina Potion(+30)'] != 0:
                self.add_mana(30)
                self.potion_inventory['Stamina Potion(+30)'] -= 1
                print("You have gained 30 stamina pts.")
            else:
                print("You have 0 Stamina Potions.")

    def show_inventory(self):
        ch = input("(1)Potion Inventory | (2)Equipment Inventory | (0)exit: ")
        while ch not in ['1', '2', '0']:
            print("Wrong choice...")
            ch = input("(1)Potion Inventory | (2)Equipment Inventory | (0)exit: ")
        if ch == '1':
            self.display_potion_inventory()
            ch = input("(1)Health Potion | (2)Mana Potion | (3)Stamina Potion | (0)Exit: ")
            while ch not in ['1', '2', '3', '0']:
                print("Wrong choice...")
                ch = input("(1)Health Potion | (2)Mana Potion | (3)Stamina Potion | (0)Exit: ")
            if ch == '0':
                return
            else:
                self.use_potion(ch)
        elif ch == '2':
            self.display_equipment_inventory()
            ch = input("Input Equipment ID to Equip | (0)Exit: ")
            if ch == '0':
                return
            else:
                self.equip(ch)
        elif ch == '0':
            return
        else:
            print("Wrong choice...")

#player = Player('icy', 'physical',50,50,50)

