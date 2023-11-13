from basic_functions import typing, clear_screen, speechbreak
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
start()