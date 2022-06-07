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


def fish_game():
    """
    Placeholder docstring to remove errors
    """
    clear_terminal()
    print(Fore.BLUE + ascii_art.FISH)
    narrative.GO_FISHING = True
    print(Style.RESET_ALL)
    num = random.randrange(1, 100)

    def start_fish(num):
        if num == 1:
            return True
        else:
            for i in range(2, num):
                if num % i == 0:
                    return False
        return True

    answer = start_fish(num)

    if answer:
        narrative.FISH_CAUGHT += 1
        print('You caught a Fish!!\n')
        print(f"You now have {narrative.FISH_CAUGHT} fish in your bucket.\n")
        choose_your_path('Keep Fishing? (Y/N)\n',
                         'y',
                         'n',
                         'Invalid choice, Keep Fishing?',
                         fish_game,
                         sleep
                         )
    else:
        print('No luck, try again?\n')
        print(f"You have caught {narrative.FISH_CAUGHT} fish.\n")
        choose_your_path('Keep trying? (Y/N)\n',
                         'y',
                         'n',
                         'Invalid choice, Keep trying?',
                         fish_game,
                         sleep
                         )


# Function used throughout the story


def choose_your_path(choice,
                     option_1,
                     option_2,
                     error,
                     function_1,
                     function_2,
                     *args
                     ):
    '''
    Function used throughout the game to
    direct the story depending on your choice.
    '''
    choice = input(Fore.YELLOW + choice).lower()
    if choice == option_1:
        function_1(*args)
    elif choice == option_2:
        function_2()
    else:
        print(Fore.YELLOW + error)
        choose_your_path(choice,
                         option_1,
                         option_2,
                         error,
                         function_1,
                         function_2,
                         *args)
    print(Style.RESET_ALL)


def pass_functions_into_choices(text, function):
    '''
    Starts the game.
    Streamlines the process of calling the choose_your_path
    function, you can pass arguments instead of having to write
    individual functions to pass in for every fork in the path.
    '''
    clear_terminal()
    txt_effect(f"{text}")
    function()


def menu():
    '''
    Calls the main menu after you have died once during the game.
    lets the user play the game from any point forward.
    '''
    clear_terminal()
    print(Style.RESET_ALL)
    print(narrative.MENU)
    option = input('')
    str(option)
    if option == '1':
        clear_terminal()
        txt_effect(intro_text)
        choose_your_path('Volunteer or Stay with the boat? [V/S]\n',
                         'v',
                         's',
                         "This is not a valid selection....Try again.",
                         volunteer,
                         stay_with_boat
                         )
    elif option == '2':
        chapter_two()
    elif option == '3':
        chapter_three()
    else:
        menu()


def txt_effect(text_to_print):
    '''
    This prints all of the text slowly.
    # '''
    # for character in text_to_print:
    #     sys.stdout.write(character)
    #     sys.stdout.flush()
    #     time.sleep(0.001)
    print(text_to_print)


def clear_terminal():
    '''
    Call this function to clear
    the terminal of the last section.
    '''
    print(Style.RESET_ALL)
    os.system('cls' if os.name == 'nt' else 'clear')