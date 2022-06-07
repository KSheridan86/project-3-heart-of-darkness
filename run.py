"""
Choose your own adventure game.
This is a choose your own adventure game, based loosely on the theme's of
the movie Apocalypse now and the inspiration for that movie, the book
The Heart of Darkness by Joseph Conrad.
You must navigate your way down the Congo river at the height of the
Belgian colonial conquest.
"""
import time
import random
import sys
import os
import colorama
from colorama import init
from colorama import Fore, Style
import narrative
import ascii_art
init()


# Games

def russian_roulette():
    '''
    Loads the russian roulette game
    '''
    barrel = [1, 2, 3, 4, 5, 6]
    clear_terminal()
    print(Fore.LIGHTBLUE_EX + ascii_art.GUN)
    print(Style.RESET_ALL)
    txt_effect('You pick up the revolver and hold it to your head.')
    kill_shot = random.randrange(1, 6)

    def pull_trigger():
        '''
        Asks you to pull the trigger of a six shot revolver.
        '''
        trigger = input('\nPress X and then Enter to fire.\n').lower()
        if trigger == 'x':
            take_shot()
        else:
            print('Wrong key, try again.')

    def take_shot():
        '''
        Checks if you're dead and continues accordingly.
        '''
        clear_terminal()
        print(Fore.LIGHTBLUE_EX + ascii_art.GUN)
        print(Style.RESET_ALL)
        shot = barrel[random.randrange(0, len(barrel))]
        barrel.remove(shot)
        if shot == kill_shot:
            txt_effect('Kill shot, You are dead!')
            game_over()
        else:
            txt_effect(narrative.SURVIVE)
            comp_shot()

    def comp_shot():
        '''
        Fires for the computer and checks whether to continue or not.
        '''
        shot = barrel[random.randrange(0, len(barrel))]
        barrel.remove(shot)
        txt_effect(narrative.MANS_TURN)
        if shot == kill_shot:
            time.sleep(2)
            survive_game_enter_office()
        else:
            txt_effect('Click, Empty, my turn...\n')
            pull_trigger()

    pull_trigger()
