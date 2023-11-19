class Player():
    def __init__(self):
        self.skill_points = 500
        self.skills_obtained = {'1': {'id': '1', 'name': 'Punch', 'attack': 50, 'skillpts': 0}}
        self.skills_selected = {'4': {'id': '4', 'name': 'Power Strike', 'attack': 120, 'skillpts': 2}}
        self.max_skills = 5

    def select_skill(self):
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
        id = input("Enter Skill ID: ")
        not_obtained_skills = {key: value for key, value in SKILL_TREE.items() if key not in self.skills_obtained} 
        
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
        def print_skills(skill_tree, page=1, skills_per_page=10):
            start_index = (page - 1) * skills_per_page
            end_index = start_index + skills_per_page
            paged_skills = list(skill_tree.values())[start_index:end_index]
            print(f"=== Skill Page {page} ===")
            for skill in paged_skills:
                if skill not in self.skills_obtained.values():
                    print(f"{skill['id']}: {skill['name']} (Attack: {skill['attack']}, Skill Points: {skill['skillpts']})")
        current_page = 1
        total_pages = len(SKILL_TREE) // 10 + (len(SKILL_TREE) % 10 > 0) # ChatGPT Thanks :thumbsup:
        while True:
            print_skills(SKILL_TREE, current_page)
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
        def print_skills(obtained_skills, page=1, skills_per_page=5):
            start_index = (page - 1) * skills_per_page
            end_index = start_index + skills_per_page
            paged_skills = list(obtained_skills.values())[start_index:end_index]
            print(f"=== Skill Page {page} ===")
            for skill in paged_skills:
                    print(f"{skill['id']}: {skill['name']} (Attack: {skill['attack']}, Skill Points: {skill['skillpts']})")
        current_page = 1
        total_pages = len(SKILL_TREE) // 10 + (len(SKILL_TREE) % 10 > 0)
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
        if len(self.skills_selected) != 0:
            def print_skills(obtained_skills, page=1, skills_per_page=5):
                start_index = (page - 1) * skills_per_page
                end_index = start_index + skills_per_page
                paged_skills = list(obtained_skills.values())[start_index:end_index]
                print(f"=== Skill Page {page} ===")
                for skill in paged_skills:
                        print(f"{skill['id']}: {skill['name']} (Attack: {skill['attack']}, Skill Points: {skill['skillpts']})")
            current_page = 1
            total_pages = len(SKILL_TREE) // 10 + (len(SKILL_TREE) % 10 > 0)
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

player = Player()

player.display_selected_skills()