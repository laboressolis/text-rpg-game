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
        
def print_character_status(character):
    print(f"{character.name} - Health: {character.health}, Mana: {character.mana}, Stamina: {character.stamina}")
    
def player_attack(player, enemy):
    print("Choose Your Attack:")
    print("1. Physical Attack: ")
    print("2. Magical Attack: ")

    attack_choice = input("Enter your choice (1 or 2): ")
    if attack_choice == "1":
        if player.stamina >= 10:  
            player.stamina -= 10
            return random.randint(player.attack - 5, player.attack + 5)
        else:
            print("Not enough stamina for a physical attack!")
            return 0  
    elif attack_choice == "2":
        if player.mana >= 20:  
            player.mana -= 20
            return random.randint(player.attack - 3, player.attack + 7)
        else:
            print("Not enough mana for a magical attack!")
            return 0  
    else:
        print("Invalid choice. Performing a default physical attack.")
        return random.randint(player.attack - 5, player.attack + 5)
    

def perform_item_effect(player, item_name):
    if item_name == 'Health Potion':
        player.health += 20
    if item_name == 'Mana Potion':
        player.mana += 30
    elif item_name == "Stamina Potion":
        player.stamina += 40
    elif item_name == "Defense Potion":
        player.defense += 5

def perform_player_defense(player):
    # Placeholder function for player defense logic
    print("You defend and regain stamina and mana.")
    player.stamina += 10
    player.mana += 15

def flee():
    # Placeholder function for player run logic
    if random.random() < 0.3:  # 30% chance to trip and fail to flee
        print("You tripped and failed to flee!")
        return False
    else:
        print("You successfully fled!")
        return True
    
def use_inventory(player):
    print("Inventory:")
    for i, (item, quantity) in enumerate(player.inventory.items(), 1):
        print(f"{i}. {item} ({quantity})")

    choice = input("Enter the item number to use, or 0 to cancel: ")
    if choice == "0":
        return

    try:
        item_index = int(choice) - 1
        selected_item = list(player.inventory.keys())[item_index]
        if selected_item in ["Health Potion", "Mana Potion", "Stamina Potion", "Defense Potion"]:
            player.use_item(selected_item)
            perform_item_effect(player, selected_item)
        else:
            print("Invalid choice!")
    except (ValueError, IndexError):
        print("Invalid choice!")

