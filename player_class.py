
import random
import time


health_pot = 'Health Potion(+20)'
mana_pot = 'Mana Potion(+30)'
stamina_pot = 'Stamina Potion(+30)'

class Player:
    def __init__(self, name, player_class, max_stamina, max_mana, base_attack):
        self.name = name
        self.player_class = player_class
        self.player_subclass = None
        self.level = 1 #not implemented idk exp systems
        self.skill_points = 0
        self.coin = 0 #shops not implemented
        self.equipment = {'weapon': {'id': '1', 'type': 'weapon', 'name': 'Wooden Sword', 'attack': 10, 'defense': 0, 'class': 'physical'}, 
                          'chest': {'id': '2', 'type': 'chest', 'name': 'Chainmail Chestplate', 'attack': 0, 'defense': 30, 'class': 'physical'}, 
                          'pants': {'id': '3', 'type': 'pants', 'name': 'Chainmail Pants', 'attack': 0, 'defense': 10, 'class': 'physical'}, 
                          'boots': {'id': '4', 'type': 'boots', 'name': 'Chainmail Boots', 'attack': 0, 'defense': 5, 'class': 'physical'}, 
                          'head': {'id': '5', 'type': 'head', 'name': 'Chainmail Helmet', 'attack': 0, 'defense': 15, 'class': 'physical'}, 
                          'hands': {'id': '6', 'type': 'hands', 'name': 'Chainmail Gloves', 'attack': 5, 'defense': 5, 'class': 'physical'}}
        
        # template {'id': 1, 'name': 'Punch', 'attack': 5}
        self.skills_obtained = {'1': {'id': '1', 'name': 'Punch', 'attack': 30, 'skillpts': 0, 'stamina_cost': 5, 'mana_cost': 0}, 
                                '2': {'id': '2', 'name': 'Kick', 'attack': 35, 'skillpts': 0, 'stamina_cost': 6, 'mana_cost': 0}, 
                                '3': {'id': '3', 'name': 'Slash', 'attack': 40, 'skillpts': 0, 'stamina_cost': 7, 'mana_cost': 0}, 
                                '4': {'id': '4', 'name': 'Bash', 'attack': 38, 'skillpts': 0, 'stamina_cost': 8, 'mana_cost': 0}
                                }
        self.skills_selected = {'1': {'id': '1', 'name': 'Punch', 'attack': 30, 'skillpts': 0, 'stamina_cost': 5, 'mana_cost': 0}, 
                                '2': {'id': '2', 'name': 'Kick', 'attack': 35, 'skillpts': 0, 'stamina_cost': 6, 'mana_cost': 0}, 
                                '3': {'id': '3', 'name': 'Slash', 'attack': 40, 'skillpts': 0, 'stamina_cost': 7, 'mana_cost': 0}, 
                                '4': {'id': '4', 'name': 'Bash', 'attack': 38, 'skillpts': 0, 'stamina_cost': 8, 'mana_cost': 0}}
        self.max_skills = 5

        # Stats
        self.base_attack = base_attack

        self.combined_attack = (self.base_attack + 
                                self.equipment['weapon']['attack'] + self.equipment['head']['attack'] + 
                                self.equipment['chest']['attack'] + self.equipment['pants']['attack'] + 
                                self.equipment['boots']['attack'] + self.equipment['hands']['attack'])

        self.defense = 10
        self.combined_defense = (self.defense + 
                                self.equipment['weapon']['defense'] + self.equipment['head']['defense'] + 
                                self.equipment['chest']['defense'] + self.equipment['pants']['defense'] + 
                                self.equipment['boots']['defense'] + self.equipment['hands']['defense'])
        
        self.defense_dynamic_factor = 0.2

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
        self.potion_inventory = {health_pot: 3, mana_pot: 2, stamina_pot: 1}
        # Equipment template {EQUIPID:{type:value,name:name,attack:value,defense:value,class:value}}
        # How to distinguish b/w weapon and equips?? IDS!!! edit1: switched to it being "type" (weapon/head/chest/pants/boots/hands)
        # NEW TEMPLATE
        # {EQUIPID: {id: value, type: string, name: string, attack: value, defense: value, class: string}}
        # YO FUCK THIS SHTI
        self.equipment_inventory = {}
    
    def skill_set(self):
        from basic_functions import load_magical_skills, load_physical_skills
        if self.player_class == 'physical':
            return load_physical_skills()
        else:
            return load_magical_skills

    def isPlayerAlive(self):
        if self.health > 0:
            return True
        else:
            return False
    
    def passive_regeneration(self):
        self.health = min(self.health + 20, self.max_health)
        self.mana = min(self.mana + 20, self.max_mana)
        self.stamina = min(self.stamina + 20, self.max_stamina)
    
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
            if self.potion_inventory[health_pot] != 0:
                self.add_hp(20)
                self.potion_inventory[health_pot] -= 1
                print("You have gained 20 hp pts.")
            else:
                print("You have 0 Health Potions.")
        if ch == '2':
            if self.potion_inventory[mana_pot] != 0:
                self.add_mana(30)
                self.potion_inventory[mana_pot] -= 1
                print("You have gained 30 mana pts.")
            else:
                print("You have 0 Mana Potions.")
        if ch == '3':
            if self.potion_inventory[stamina_pot] != 0:
                self.add_mana(30)
                self.potion_inventory[stamina_pot] -= 1
                print("You have gained 30 stamina pts.")
            else:
                print("You have 0 Stamina Potions.")

    def show_inventory(self):
        from basic_functions import clear_lines
        ch = input("(1)Potion Inventory | (2)Equipment Inventory | (0)exit: ")
        clear_lines(1)
        while ch not in ['1', '2', '0']:
            print("Wrong choice...")
            ch = input("(1)Potion Inventory | (2)Equipment Inventory | (0)exit: ")
            clear_lines(2)
        if ch == '1':
            self.display_potion_inventory()
            ch = input("(1)Health Potion | (2)Mana Potion | (3)Stamina Potion | (0)Exit: ")
            clear_lines(5)
            while ch not in ['1', '2', '3', '0']:
                print("Wrong choice...")
                ch = input("(1)Health Potion | (2)Mana Potion | (3)Stamina Potion | (0)Exit: ")
                clear_lines(2)
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

    def add_item(self,item):
        if item == health_pot:
            self.potion_inventory[health_pot] += 1
        elif item == mana_pot:
            self.potion_inventory[mana_pot] += 1
        elif item == stamina_pot:
            self.potion_inventory[stamina_pot] += 1
        else:
            if type(item) == dict:
                for key in item:
                    self.equipment_inventory[key] = item[key]
                    print(f'''Item "{self.equipment_inventory[key]['name']}" was added to your inventory.''')
            else:
                print("Wrong Item Data")
    
    def select_skills(self):
        id = input("Enter Skill ID: ")
        if len(self.skills_selected) == self.max_skills:
            print("You have reached the max limit of selected skills.")
        else:
            if id not in self.skills_selected:
                self.skills_selected[id] = self.skills_obtained[id]
                print(f'You have selected {self.skills_selected[id]['name']}.')

            else:
                print("You have that skill already selected.")

    def deselect_skill(self):
        id = input("Enter Skill ID: ")
        if len(self.skills_selected) == 0:
            print("You have no skills selected: ")
        else:
            del self.skills_selected[id]
    
    def buy_skill(self):
        skills = self.skill_set() # Fix [20:11:2023]
        id = input("Enter Skill ID: ")
        not_obtained_skills = {key: value for key, value in skills.items() if key not in self.skills_obtained} 
        
        if id in not_obtained_skills:
            if self.skill_points > not_obtained_skills[id]['skillpts']:
                self.skills_obtained[id] = not_obtained_skills[id]
                self.skill_points = self.skill_points - self.skills_obtained[id]['skillpts']
                print(f"You have obtained {self.skills_obtained[id]['name']}")
            else:
                print(f"You don't have enough skill points (Current Skills Points:{self.skill_points}) for that skill.")
        else:
            print("There is no available skill with that skill id.")

    def display_all_skills(self):
        skills = self.skill_set() # Fix [20:11:2023]
        def print_skills(skill_tree, page=1, skills_per_page=10):
            start_index = (page - 1) * skills_per_page
            end_index = start_index + skills_per_page
            paged_skills = list(skill_tree.values())[start_index:end_index]
            print(f"=== Skill Page {page} ===")
            for skill in paged_skills:
                if skill not in self.skills_obtained.values():
                    print(f"{skill['id']}: {skill['name']} (Attack: {skill['attack']}, Skill Points: {skill['skillpts']})")
        current_page = 1
        total_pages = len(skills) // 10 + (len(skills) % 10 > 0) # ChatGPT Thanks :thumbsup:
        while True:
            print_skills(skills, current_page)
            user_input = input("(l)Next Page | (k)Previous Page | (q)Back | (b)Buy Skill: ")
            while user_input not in ['l','k','b','q']:
                print("Wrong Input.")
                user_input = input("(l)Next Page | (k)Previous Page | (q)Back | (b)Buy Skill: ")
            if user_input == 'l' and current_page < total_pages:
                current_page += 1
            elif user_input == 'k' and current_page > 1:
                current_page -= 1
            elif user_input == 'q':
                break
            elif user_input == 'b':
                self.buy_skill()
 
    def display_obtained_skills(self):
        skills = self.skill_set() # Fix [20:11:2023]
        def print_skills(obtained_skills, page=1, skills_per_page=5):
            start_index = (page - 1) * skills_per_page
            end_index = start_index + skills_per_page
            paged_skills = list(obtained_skills.values())[start_index:end_index]
            print(f"=== Skill Page {page} ===")
            for skill in paged_skills:
                    print(f"{skill['id']}: {skill['name']} (Attack: {skill['attack']}, Skill Points: {skill['skillpts']})")
        current_page = 1
        total_pages = len(skills) // 10 + (len(skills) % 10 > 0)
        while True:
            print_skills(self.skills_obtained,current_page)
            user_input = input("(l)Next Page | (k)Previous Page | (q)Back | (s)Select Skill: ")
            while user_input not in ['l','k','s','q']:
                user_input = input("(l)Next Page | (k)Previous Page | (q)Back | (s)Select Skill: ")
            if user_input == 'l' and current_page < total_pages:
                current_page += 1
            elif user_input == 'k' and current_page > 1:
                current_page -= 1
            elif user_input == 'q':
                break
            elif user_input == 's':
                self.select_skill()
      
    def display_selected_skills(self):
        # I know I made a dum move here with the len(self.skills_selected) but eh
        skills = self.skill_set() # Fix [20:11:2023]
        if len(self.skills_selected) != 0:
            def print_skills(obtained_skills, page=1, skills_per_page=5):
                start_index = (page - 1) * skills_per_page
                end_index = start_index + skills_per_page
                paged_skills = list(obtained_skills.values())[start_index:end_index]
                print(f"=== Skill Page {page} ===")
                for skill in paged_skills:
                        print(f"{skill['id']}: {skill['name']} (Attack: {skill['attack']}, Skill Points: {skill['skillpts']})")
            current_page = 1
            total_pages = len(skills) // 10 + (len(skills) % 10 > 0)
            while True:
                if len(self.skills_selected) == 0:
                    print("You have no selected skills.")
                    break
                print_skills(self.skills_selected,current_page)
                user_input = input("(l)Next Page | (k)Previous Page | (q)Back | (s)Deselect Skill: ")
                while user_input not in ['l','k','s','q']:
                    user_input = input("(l)Next Page | (k)Previous Page | (q)Back | (s)Deselect Skill: ")
                if user_input == 'l' and current_page < total_pages:
                    current_page += 1
                elif user_input == 'k' and current_page > 1:
                    current_page -= 1
                elif user_input == 'q':
                    break
                elif user_input == 's':
                    self.deselect_skill()
        else:
            print("You have no selected skills.")
    
    def attack(self):
        from basic_functions import reallyfasttyping, clear_lines
        list_skills = list(self.skills_selected.values())
        keys = list(self.skills_selected.keys())
        print(f"Mana:{self.mana} | Stamina:{self.stamina}")
        for tempskill in list_skills:
            print(f"{tempskill['id']}: {tempskill['name']} (Attack: {tempskill['attack']} | Mana:{tempskill["mana_cost"]} | Stamina:{tempskill["stamina_cost"]})")
        id = input("Enter Skill ID to attack: ")
        while id not in keys:
            print("uh oh! Wrong Skill id?")
            id = input("Enter Skill ID to attack: ")
        skill = self.skills_selected[id]
        if self.stamina >= skill['stamina_cost'] and self.mana > skill['mana_cost']:
            probabilities = [0.1, 0.3, 0.4, 0.2]
            total_attack_val = self.combined_attack + skill['attack']
            range1 = int(0.1 * total_attack_val)
            range2 = int(0.3 * total_attack_val)+ range1
            range3 = int(0.4 * total_attack_val) + range2            
            # Subtracting the stamina and mana cost
            self.stamina = self.stamina - skill['stamina_cost']
            self.mana = self.mana - skill['mana_cost']

            random_number = random.uniform(0, 1)

            # [21:11:23] It was throwing n 'ValueError: empty range in randrange(37, 9)' error fixed it by making sure the limits are okay.
            if random_number < probabilities[0]:
                return self.combined_attack
            elif random_number < probabilities[1]:
                lower_bound = min(range1, self.combined_attack - 1)
                upper_bound = max(range1, self.combined_attack - 1)
                return random.randint(lower_bound, upper_bound)
            elif random_number < probabilities[2]:
                lower_bound = min(range2, range1 - 1)
                upper_bound = max(range2, range1 - 1)
                return random.randint(lower_bound, upper_bound)
            else:
                return random.randint(0,range3- 1)
        else:
            reallyfasttyping("You don't have enough Mana or Stamina for it. \n")
            reallyfasttyping("You deal no damage. \n")
            time.sleep(0.8)
            clear_lines(2)
            return 0
        
    def player_defense(self,attack_val):
        # mb here
        def calc_effective_defense():
            # dynamic_multiplier = 1 + dynamic_factor * (current_health / max_health)
            dynamic_multiplier = 1 + self.defense_dynamic_factor * (self.health / self.max_health)
            effective_defense = self.combined_defense * dynamic_multiplier
            return effective_defense
        effective_defense = calc_effective_defense()
        reduced_damage = max(0, attack_val - effective_defense)
        return reduced_damage
    
    def flee(self):
        probabilities = [0.4,0.6]

        random_number = random.uniform(0,1)

        if random_number < probabilities[0]:
            '''if player escapes then True'''
            return True
        else:
            return False
        
    
    
