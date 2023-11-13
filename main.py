from basic_functions import typing, fasttyping, clear_screen, speechbreak
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
    typing("Oberon: Ohhh... So you're one of those kind, huh? \n")
    typing("Oberon: Well to buy anything here at the guild you'd a guild emblem, you register there at the counter. \n")
    typing("Oberon: This old man sells a lot of things. \n")
    typing(' ')
    fasttyping("You head over to the counter to register.")
    clear_screen()
    # begin character creation

start()