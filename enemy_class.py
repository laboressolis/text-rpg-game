import random
from player_class import Player



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

    def attack_player(self):
        dmg = random.randint(10,self.attack)
        return dmg

    def drop_items(self, player):
        from basic_functions import items
        from basic_functions import reallyfasttyping
        from player_class import health_pot, stamina_pot, mana_pot
        # 30 - drops nothing
        # 20 - drops items 
        # 19 - drops skillspts
        # 18 - drops potions
        # 10 - drops 2 items and and skill pts
        # 3 - drop 2 items and 2x skill pts and 1 potion
        probabilities = [0.03, 0.1, 0.18, 0.19, 0.2, 0.3]
        random_number = random.uniform(0,1)
        if random_number < probabilities[0]:
            key1, value1 = random.choice(list(items.items()))
            key2, value2 = random.choice(list(items.items()))
            potion_drops = [health_pot, stamina_pot,mana_pot]
            skillpoints = [1,6,7,2,8,12,5,3,7,6,8,4,9,2,17,11,15,6,8,9,4,6,7]
            drop1 = {key1:value1}
            drop2 = {key2:value2}
            drop3 = random.choice(potion_drops)
            drop4 = random.choice(skillpoints)
            prompts = [f"You discover {value1['name']}(Atk:{value1['attack']}|Def:{value1['defense']}) and {value2['name']}(Atk:{value2['attack']}|Def:{value2['defense']}) among the remains of the defeated {self.name}, a satisfying reward for your skill. You also gain {drop3} potions and {drop4} skill points. \n",
                      f'The {self.name} drops an item {value1['name']}(Atk:{value1['attack']}|Def:{value1['defense']}) and {value2['name']}(Atk:{value2['attack']}|Def:{value2['defense']}). You also receive {drop3} potions and {drop4} skill points. \n',
                      f'Upon defeating the {self.name}, you discover a {value1['name']}(Atk:{value1['attack']}|Def:{value1['defense']}) and {value2['name']}(Atk:{value2['attack']}|Def:{value2['defense']}) among its belongings. You also get {drop3} potions and {drop4} skill points. \n',
                      f"You collect a {value1['name']}(Atk:{value1['attack']}|Def:{value1['defense']}) and {value2['name']}(Atk:{value2['attack']}|Def:{value2['defense']}) as a reward for defeating the {self.name}. You also obtain {drop3} potions and {drop4} skill points. \n",]
            reallyfasttyping(random.choice(prompts))
            player.add_item(drop1)        
            player.add_item(drop1)   
            player.add_item(drop1)   
            player.skill_points += drop4    
        elif random_number < probabilities[1]:
            key1, value1 = random.choice(list(items.items()))
            key2, value2 = random.choice(list(items.items()))
            skillpoints = [1,6,7,2,8,12,5,3,7,6,8,4,9,2,17,11,15,6,8,9,4,6,7]
            drop1 = {key1:value1}
            drop2 = {key2:value2}
            drop3 = random.choice(skillpoints)
            prompts = [f"You discover {value1['name']}(Atk:{value1['attack']}|Def:{value1['defense']}) and {value2['name']}(Atk:{value2['attack']}|Def:{value2['defense']}) among the remains of the defeated {self.name}, a satisfying reward for your skill. You also gain {drop3} skill points. \n",
                       f'The {self.name} drops an item {value1['name']}(Atk:{value1['attack']}|Def:{value1['defense']}) and {value2['name']}(Atk:{value2['attack']}|Def:{value2['defense']}). You also gain {drop3} skill points. \n',
                       f'Upon defeating the {self.name}, you discover a {value1['name']}(Atk:{value1['attack']}|Def:{value1['defense']}) and {value2['name']}(Atk:{value2['attack']}|Def:{value2['defense']}) among its belongings. You also gain {drop3} skill points. \n',
                       f"You collect a {value1['name']}(Atk:{value1['attack']}|Def:{value1['defense']}) and {value2['name']}(Atk:{value2['attack']}|Def:{value2['defense']}) as a reward for defeating the {self.name}. You also gain {drop3} skill points. \n",]
            reallyfasttyping(random.choice(prompts))
            player.add_item(drop1)
            player.add_item(drop2)
            player.skill_points += drop3
        elif random_number < probabilities[2]:
            drops = [health_pot, stamina_pot,mana_pot]
            drop = random.choice(drops)
            prompts = [f"A {drop} potion is among the spoils dropped by the defeated {self.name}. \n",
                       f"The {self.name} drops a {drop} potion for you to pick up. \n",
                       f"You find a {drop} potion in the loot dropped by the {self.name}. \n",
                       f"The {self.name} drops a {drop} potion for you to pick up. \n"]
            reallyfasttyping(random.choice(prompts))
            player.add_item(drop)
        elif random_number < probabilities[3]:
            skillpoints = [1,6,7,2,8,12,5,3,7,6,8,4,9,2,17,11,15,6,8,9,4,6,7]
            drop = random.choice(skillpoints)
            prompts = [f"You gain {drop} skill points from the defeated {self.name}. \n",
                       f"You collect {drop} skill points from the loot dropped by the {self.name}. \n",
                       f"You receive {drop} skill points as a reward for overcoming the {self.name}. \n",
                       f"The defeated {self.name} grants you {drop} skill points. \n"]
            reallyfasttyping(random.choice(prompts))
            player.skill_points += drop
        elif random_number < probabilities[4]:
            key, value = random.choice(list(items.items()))
            drop = {key:value}
            prompts = [f'You discover {value['name']}(Atk:{value['attack']}|Def:{value['defense']}) among the remains of the defeated {self.name}, a satisfying reward for your skill. \n',
                       f'The {self.name} drops an item {value['name']}(Atk:{value['attack']}|Def:{value['defense']}). \n',
                       f'Upon defeating the {self.name}, you discover a {value['name']}(Atk:{value['attack']}|Def:{value['defense']}) among its belongings. \n',
                       f"You collect a {value['name']}(Atk:{value['attack']}|Def:{value['defense']}) as a reward for defeating the {self.name}. \n"]
            reallyfasttyping(random.choice(prompts))
            player.add_item(drop)
        else:

            prompts = ['Awww rip it dropped nothing. \n',
                       'Looks like it dropped nothing. \n',
                       f'{self.name} dropped nothing. \n',
                       f'No loot this time as the defeated {self.name} leaves nothing behind. \n',
                       f'The {self.name} meets its end, but alas, no loot is left behind for you. \n']
            reallyfasttyping(random.choice(prompts))
   
player = Player('icy', 'physical',15,50,50)
enemy = Enemy('Banshee', 160, 160, 35, 'normal')