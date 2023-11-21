import json

""" 
SKILL_TREE = {
    '1': {'id': '1', 'name': 'Punch', 'attack': 50, 'skillpts': 0},
    '2': {'id': '2', 'name': 'Slash', 'attack': 100, 'skillpts': 0},
    '3': {'id': '3', 'name': 'Rapid Punch', 'attack': 40, 'skillpts': 5},
    '4': {'id': '4', 'name': 'Power Strike', 'attack': 120, 'skillpts': 2},
    '5': {'id': '5', 'name': 'Cleave', 'attack': 90, 'skillpts': 3},
    '6': {'id': '6', 'name': 'Whirlwind Slash', 'attack': 80, 'skillpts': 1},
    '7': {'id': '7', 'name': 'Double Punch', 'attack': 60, 'skillpts': 4},
    '8': {'id': '8', 'name': 'Sword Mastery', 'attack': 30, 'skillpts': 2},
    '9': {'id': '9', 'name': 'Brutal Strike', 'attack': 110, 'skillpts': 3},
    '10': {'id': '10', 'name': 'Thrust', 'attack': 70, 'skillpts': 1},
    '11': {'id': '11', 'name': 'Mighty Cleave', 'attack': 100, 'skillpts': 2},
    '12': {'id': '12', 'name': 'Fists of Fury', 'attack': 55, 'skillpts': 4},
    '13': {'id': '13', 'name': 'Blade Dance', 'attack': 95, 'skillpts': 3},
    '14': {'id': '14', 'name': 'Thunder Punch', 'attack': 65, 'skillpts': 1},
    '15': {'id': '15', 'name': 'Sword Whirl', 'attack': 85, 'skillpts': 2},
    '16': {'id': '16', 'name': 'Heavy Impact', 'attack': 130, 'skillpts': 0},
    '17': {'id': '17', 'name': 'Counter Slash', 'attack': 75, 'skillpts': 0},
    '18': {'id': '18', 'name': 'Savage Strike', 'attack': 105, 'skillpts': 0},
    '19': {'id': '19', 'name': 'Frenzy Punch', 'attack': 45, 'skillpts': 0},
    '20': {'id': '20', 'name': 'Sword Spin', 'attack': 110, 'skillpts': 0},
    '21': {'id': '21', 'name': 'Jab', 'attack': 50, 'skillpts': 0},
    '22': {'id': '22', 'name': 'Sword Slam', 'attack': 115, 'skillpts': 0},
    '23': {'id': '23', 'name': 'Swift Strikes', 'attack': 95, 'skillpts': 0},
    '24': {'id': '24', 'name': 'Piercing Thrust', 'attack': 60, 'skillpts': 0},
    '25': {'id': '25', 'name': 'Blade Fury', 'attack': 120, 'skillpts': 0},
    '26': {'id': '26', 'name': 'Rising Uppercut', 'attack': 70, 'skillpts': 0},
    '27': {'id': '27', 'name': 'Dagger Dance', 'attack': 80, 'skillpts': 0},
    '28': {'id': '28', 'name': 'Crushing Blow', 'attack': 125, 'skillpts': 0},
    '29': {'id': '29', 'name': 'Sword Storm', 'attack': 100, 'skillpts': 0},
    '30': {'id': '30', 'name': 'Blitz Punch', 'attack': 55, 'skillpts': 0}
}

with open('skill_tree.json', 'w') as file:
    json.dump(SKILL_TREE, file, indent=4)

 """

""" skill_tree = {
    '1': {'id': '1', 'name': 'Fireball', 'attack': 30, 'skillpts': 5},
    '2': {'id': '2', 'name': 'Ice Shard', 'attack': 25, 'skillpts': 4},
    '3': {'id': '3', 'name': 'Thunderstrike', 'attack': 35, 'skillpts': 6},
    '4': {'id': '4', 'name': 'Earthquake', 'attack': 40, 'skillpts': 7},
    '5': {'id': '5', 'name': 'Wind Cutter', 'attack': 28, 'skillpts': 5},
    '6': {'id': '6', 'name': 'Aqua Blast', 'attack': 32, 'skillpts': 6},
    '7': {'id': '7', 'name': 'Lightning Bolt', 'attack': 38, 'skillpts': 8},
    '8': {'id': '8', 'name': 'Magma Eruption', 'attack': 42, 'skillpts': 9},
    '9': {'id': '9', 'name': 'Blizzard', 'attack': 27, 'skillpts': 5},
    '10': {'id': '10', 'name': 'Solar Flare', 'attack': 45, 'skillpts': 10}
} """




# Load the skill tree from the JSON file
""" def load_skills():
    with open('Tests\skill_tree.json', 'r') as file:
        loaded_skill_tree = json.load(file)
        return loaded_skill_tree """




skill_tree = {
    '1': {'id': '1', 'name': 'Punch', 'attack': 30, 'skillpts': 0, 'stamina_cost': 5, 'mana_cost': 0},
    '2': {'id': '2', 'name': 'Kick', 'attack': 35, 'skillpts': 0, 'stamina_cost': 6, 'mana_cost': 0},
    '3': {'id': '3', 'name': 'Slash', 'attack': 40, 'skillpts': 0, 'stamina_cost': 7, 'mana_cost': 0},
    '4': {'id': '4', 'name': 'Bash', 'attack': 38, 'skillpts': 0, 'stamina_cost': 8, 'mana_cost': 0},
    '5': {'id': '5', 'name': 'FirePunch', 'attack': 45, 'skillpts': 5, 'stamina_cost': 9, 'mana_cost': 15},
    '6': {'id': '6', 'name': 'Swipe', 'attack': 32, 'skillpts': 3, 'stamina_cost': 5, 'mana_cost': 0},
    '7': {'id': '7', 'name': 'Crush', 'attack': 42, 'skillpts': 5, 'stamina_cost': 8, 'mana_cost': 0},
    '8': {'id': '8', 'name': 'Thrust', 'attack': 36, 'skillpts': 7, 'stamina_cost': 6, 'mana_cost': 0},
    '9': {'id': '9', 'name': 'Strike', 'attack': 33, 'skillpts': 3, 'stamina_cost': 7, 'mana_cost': 0},
    '10': {'id': '10', 'name': 'Lunge', 'attack': 39, 'skillpts': 5, 'stamina_cost': 7, 'mana_cost': 0}
}
with open('Data/physical_skill_tree.json', 'w') as file:
    json.dump(skill_tree, file, indent=4)