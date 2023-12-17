from player_class import Player
from enemy_class import Enemy
from basic_functions import items, enemies
from basic_functions import typing, fasttyping, reallyfasttyping, clear_lines, clear_screen
import random
import time

random_enemy = random.choice(enemies)
player = Player('icy', 'physical',15,50,50)

def battle(enemy, player):
    fasttyping(f"You have encountered {enemy.name}({enemy.health}). \n")
    while enemy.isEnemyAlive() and player.isPlayerAlive():
        print(f"{player.name}:{player.health}/{player.max_health} | {enemy.name}:{enemy.health}/{enemy.max_health}")
        print('Attack(1) | Defend(2) | Rest(3) | Inventory(4) |Flee(5) ')
        choice = input()
        clear_lines(3)
        while choice not in ['1','2','3','4','5']:
            fasttyping("uh oh! Wrong Choice? \n")
            print('Attack(1) | Defend(2) | Rest(3) | Inventory(4) |Flee(5) ')
            choice = input()
            clear_lines(3)
        if choice == '1':
            damage = player.attack()
            enemy.remove_hp(damage)
            typing(f"You dealt {damage} damage to {enemy.name}. \n")
            time.sleep(1)
            if enemy.health <= 0:
                reallyfasttyping("You have won the battle!")
                enemy.drop_items(player)
                time.sleep(2.5)
                clear_lines(2)
            else:
                damage = enemy.attack_player()
                print(f"{enemy.name} deals {damage} damage to you.")
                clear_lines(1)
            enemy_damage = enemy.attack_player()
            player.remove_health(enemy_damage)
            fasttyping(f"You took {enemy_damage} damage from {enemy.name} \n")
            time.sleep(1.8)
            clear_lines(8)
        elif choice == '2':
            damage = enemy.attack_player()
            dmg_taken = player.player_defense(damage)
            player.health -= dmg_taken
            if dmg_taken == 0:
                typing("You defended. You took no damage. \n")
            else:
                typing(f"You defended against {enemy.name}'s attack. You took {dmg_taken} damage. \n")
            mana_add = random.choice([7,11,34,12,18,9,3,5])
            stamina_add = random.choice([7,11,34,12,18,9,3,5])
            player.add_mana(mana_add)
            player.add_stamina(stamina_add)
            fasttyping(f"You gained {mana_add} mana points. \n")
            fasttyping(f"You gained {stamina_add} stamina points. \n")
            time.sleep(1.5)
            clear_lines(6)
        elif choice == '3':
            damage = enemy.attack_player()
            player.health -= damage
            mana_inc= random.choice([30,20,24,26,67,43,12,34,37])
            stamina_inc= random.choice([30,20,24,26,67,43,12,34,37])
            health_inc= random.choice([30,20,24,26,67,43,12,34,37])
            player.add_mana(mana_inc)
            player.add_stamina(stamina_inc)
            player.add_hp(health_inc)
            fasttyping(f"You took {damage} damage from {enemy.name}. \n")
            fasttyping(f"You regenerated {health_inc} health points. \n")
            fasttyping(f"You regenerated {mana_inc} mana. \n")
            fasttyping(f"You regenerated {stamina_inc} stamina.\n")
            time.sleep(1.8)
            clear_lines(4)
        elif choice == '4':
            player.show_inventory()

        
        elif choice == '5':
            fasttyping("You try to flee. \n")
            if player.flee():
                fasttyping("Phew! That was one heck of an escape, right? \n")
                break
            else:
                random_number = random.choice([3,4,2,4,5,6,1,7])
                fasttyping(f"Awww! You tripped an fell and took {random_number} damage.\n")
                player.health -= random_number
            clear_lines(3)
        
battle(random_enemy,player)