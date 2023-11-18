from basic_functions import typing, fasttyping, clear_screen, speechbreak, newline
from basic_functions import load_enemies, load_items
import time

start_logo = r'''
 ▄▄▄▄▄▄▄ ▄▄   ▄▄ ▄▄▄▄▄▄ ▄▄▄▄▄▄  ▄▄▄▄▄▄▄ ▄     ▄ ▄▄▄▄▄▄▄    ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄    ▄▄▄▄▄▄▄ ▄▄▄     ▄▄▄▄▄▄  ▄▄▄▄▄▄▄ ▄▄▄▄▄▄   ▄▄▄ ▄▄▄▄▄▄ 
█       █  █ █  █      █      ██       █ █ ▄ █ █       █  █       █       █  █       █   █   █      ██       █   ▄  █ █   █      █
█  ▄▄▄▄▄█  █▄█  █  ▄   █  ▄    █   ▄   █ ██ ██ █  ▄▄▄▄▄█  █   ▄   █    ▄▄▄█  █    ▄▄▄█   █   █  ▄    █   ▄   █  █ █ █ █   █  ▄   █
█ █▄▄▄▄▄█       █ █▄█  █ █ █   █  █ █  █       █ █▄▄▄▄▄   █  █ █  █   █▄▄▄   █   █▄▄▄█   █   █ █ █   █  █ █  █   █▄▄█▄█   █ █▄█  █
█▄▄▄▄▄  █   ▄   █      █ █▄█   █  █▄█  █       █▄▄▄▄▄  █  █  █▄█  █    ▄▄▄█  █    ▄▄▄█   █▄▄▄█ █▄█   █  █▄█  █    ▄▄  █   █      █
 ▄▄▄▄▄█ █  █ █  █  ▄   █       █       █   ▄   █▄▄▄▄▄█ █  █       █   █      █   █▄▄▄█       █       █       █   █  █ █   █  ▄   █
█▄▄▄▄▄▄▄█▄▄█ █▄▄█▄█ █▄▄█▄▄▄▄▄▄██▄▄▄▄▄▄▄█▄▄█ █▄▄█▄▄▄▄▄▄▄█  █▄▄▄▄▄▄▄█▄▄▄█      █▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█▄▄▄▄▄▄██▄▄▄▄▄▄▄█▄▄▄█  █▄█▄▄▄█▄█ █▄▄█

'''
enemies = load_enemies("enemies.txt")
items = load_items("items.txt")

def start():
    
    clear_screen()
    print(start_logo)
    time.sleep(.5)
    typing("You find yourself in the mythical land of Eldoria, a realm shrouded in mystery and danger. \n")
    typing("The once peaceful kingdom is now threatened by the rise of an ancient evil force known as the Shadow Cult. \n")
    typing("As a skilled adventurer, you embark on a journey to unravel the secrets of Eldoria, facing perilous challenges and making crucial decisions that will shape the fate of the land. \n")
    speechbreak()
    fasttyping("You arive at Celestria's main gate, the biggest city in Eldoria. \n")
    fasttyping("You head towards the Adventurer's Guild in city center where you meet Oberon.\n")
    
    typing("Oberon: You look new here son! What bring you here? Looking for some sweet money? \n")
    typing("You: No, I'm just an Adventurer. \n")
    typing("Oberon: Ohhh... So you're one of those kind, huh? But you seem empty handed...... \n")
    typing("You: I was ambused on my way and lost my stuff. \n")
    typing("Oberon: Well I suppose I could hook you with some stuff. Follow me!\n")
    clear_screen()
    fasttyping("You follow Oberon to the guild's armory. \n")
    

    # begin character creation

start()