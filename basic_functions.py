import os
import sys
import time
import random
import msvcrt

def clear_screen():
    '''Clears The Screen'''
    os.system('cls')

def typing(message):
    '''Typing Mech'''
    for letter in message:
        time.sleep(random.choice([0.3, 0.11, 0.08, 0.07,0.07, 0.07, 0.06, 0.06, 0.05, 0.01]))
        sys.stdout.write(letter)
        sys.stdout.flush()
    time.sleep(.1)
    return ""

def fasttyping(message):
    for letter in message:
        time.sleep(random.choice([0.11, 0.01, 0.08, 0.01,0.01, 0.07, 0.06, 0.06, 0.05, 0.01]))
        sys.stdout.write(letter)
        sys.stdout.flush()
    time.sleep(.1)
    return ''

def speechbreak():
    print("Press any key to continue....", end='')
    msvcrt.getch()

def createcharacter():
    pass


def newline():
    print()
