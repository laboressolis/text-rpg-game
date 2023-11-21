# RPG Text Game in Python

This is my first Text Based RPG game in py.
Embark on an epic journey, face formidable enemies, and shape your destiny.

## Getting Started

1. Clone the repository:
    ```bash
    git clone https://github.com/laboressolis/text-rpg-game.git
    ```

2. Navigate to the project directory:
    ```bash
    cd rpg-text-game
    ```

3. Run the game:
    ```bash
    python main.py
    ```

## Features

- **Class System:** Player Classes to enchance your gameplay.
- **Coin System:** Earn and spend coins to enhance your character.
- **Skill System:** Customize your abilities using skills from a JSON file (`skills.json`).
- **Weapons:** Equip powerful weapons loaded from a JSON file (`items.json`).
- **Item Drops:** Collect loot from defeated enemies.
- **Enraged Enemies:** Beware, enemies have a chance to get enraged, boosting their stats.
- **Epik Story:** Immerse yourself in an epic narrative that unfolds as you progress.

## Mistakes I've made throughout this journey.

- **[20:11:2023]:** I messed up the skill system. I completely forgot the fact that I have a class system and different classes will have different skill sets.
How did I fix it?
I was to lazy to rework the skill system to add a 'class' id... so I just made different json files for different classes and returned differnet skill tree depending on the player's class.
- **[21:11:2023]:** Well Well Well...*sign*.. I forgot skills would cost mana or stamina... ￣へ￣
How did I fix it?
Added the mana and stamina id to skill data... (I already made the function while accounting for mana and stamina but didnt add it the skill data :/)


