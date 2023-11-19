import random

class Player:
    def __init__(self, combined_attack):
        self.combined_attack= combined_attack

    def attack(self):
        probabilities = [0.1, 0.3, 0.4, 0.2]

        range1 = int(0.1 * self.combined_attack)
        range2 = int(0.3 * self.combined_attack)+ range1
        range3 = int(0.4 * self.combined_attack) + range2

        random_number = random.uniform(0, 1)

        if random_number < probabilities[0]:
            print("Crit!")
            return self.combined_attack
        elif random_number < probabilities[1]:
            return random.randint(range1, self.combined_attack- 1)
        elif random_number < probabilities[2]:
            return random.randint(range2, range1- 1)
        else:
            return random.randint(0,range3- 1)

attack = 100 
player = Player(attack)
for i in range(10):
    attack_val = player.attack()
    print(attack_val)
