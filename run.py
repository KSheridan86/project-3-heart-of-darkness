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
# import colorama
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
            txt_effect('        Click, Empty, my turn...\n')
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
        act_two()
    elif option == '3':
        act_three()
    else:
        menu()


def txt_effect(text_to_print):
    '''
    This prints all of the text slowly.
    # '''
    for character in text_to_print:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    # print(text_to_print)


def clear_terminal():
    '''
    Call this function to clear
    the terminal of the last section.
    '''
    print(Style.RESET_ALL)
    os.system('cls' if os.name == 'nt' else 'clear')


def game_over():
    '''
    Prints a game over graphic
    '''
    time.sleep(2)
    clear_terminal()
    print(Fore.RED + ascii_art.GAME_OVER)
    choose_your_path('Would you like to play again? [Y/N]\n',
                     'y',
                     'n',
                     "This is not a valid selection....Try again.",
                     menu,
                     end_story
                     )


def game_over_alive():
    '''
    Prints a game over graphic
    '''
    clear_terminal()
    print(Fore.BLUE + ascii_art.GAME_OVER_ALIVE)
    choose_your_path('Would you like to play again? [Y/N]\n',
                     'y',
                     'n',
                     "This is not a valid selection....Try again.",
                     menu,
                     end_story
                     )


def end_story():
    '''
    Ends the game.
    '''
    print(Style.RESET_ALL)
    print('Thanks for playing, come back soon.')


def begin_game():
    '''
    Asks you to begin the game, prints the first
    paragraph and loads the first choice.
    '''

    print()
    answer = input(
        Fore.YELLOW + 'Would you like to start the story? (Y/N)\n').lower()
    if answer == 'y':
        clear_terminal()
        txt_effect(intro_text)
        choose_your_path('Volunteer or Stay with the boat? [V/S]\n',
                         'v',
                         's',
                         "This is not a valid selection....Try again.",
                         volunteer,
                         stay_with_boat
                         )
    elif answer == 'n':
        game_over()
    else:
        print("This is not a valid selection....Try again.")
        begin_game()


# Start story

print(Fore.LIGHTYELLOW_EX)
print(ascii_art.TITLE)
print(Fore.GREEN + Style.BRIGHT)
txt_effect(narrative.INTRO)
print(Style.RESET_ALL)
time.sleep(.5)
name = input('Please enter your name to continue....\n').capitalize()
while not name or len(name) > 50:
    name = input('''Ooops too long, Max of 50 characters...\n
Please enter your name to continue....\n''').capitalize()


intro_text = f"""
        Act 1\n
        The year was 1902 and the steamboat I was travelling on had
        blown an engine. Miles from the town we had left yesterday and
        half a world from home.\n
        This damn river was trying to kill me....\n
        {name} a voice called, it was the Captain.
        The radio is busted. We need 2 volunteers to go and alert
        the station master of what has happened...

        """


# Act 1
# Act 1 Fork 1


def volunteer():
    '''
    Runs the volunteer selection
    '''
    clear_terminal()
    print(Fore.GREEN + ascii_art.JUNGLE)
    print(Style.RESET_ALL)
    txt_effect(narrative.VOLUNTEER)
    choose_your_path('Do you get Angry or stay Calm? (A/C)\n',
                     'a',
                     'c',
                     'Invalid choice, please choose...',
                     pass_functions_into_choices,
                     dont_fight_sven,
                     narrative.FIGHT_SVEN,
                     game_over
                     )


def dont_fight_sven():
    '''
    placeholder
    '''
    clear_terminal()
    txt_effect(narrative.DONT_FIGHT)
    choose_your_path('Do you drink the Water or the Bourbon? (W/B)\n',
                     'w',
                     'b',
                     'Invalid choice, please choose a drink.',
                     pass_functions_into_choices,
                     drink_bourbon,
                     narrative.WATER,
                     game_over
                     )


# Act 1 Fork 1.1


def drink_bourbon():
    """
    Placeholder docstring to remove errors
    """
    clear_terminal()
    txt_effect(narrative.BOURBON)
    choose_your_path('Press Enter to start Act two.\n',
                     '',
                     '',
                     'Invalid choice, press Enter.',
                     act_two,
                     act_two
                     )

# Act 1 Fork 2


def stay_with_boat():
    """
    Placeholder docstring to remove errors
    """
    clear_terminal()
    txt_effect(narrative.STAY)
    choose_your_path('Stay and help or take what you can and Escape? (S/E)\n',
                     's',
                     'e',
                     'Invalid choice, please choose a path.',
                     pass_functions_into_choices,
                     escape_boat,
                     narrative.STAY_ON_BOAT,
                     game_over
                     )

# Act 1 Fork 2.1


def escape_boat():
    """
    Placeholder docstring to remove errors
    """
    clear_terminal()
    txt_effect(narrative.ESCAPE_BOAT)
    choose_your_path('Press Enter to start Act two.\n',
                     '',
                     '',
                     'Invalid choice, press Enter.',
                     act_two,
                     act_two
                     )


##############################################################################
# Act 2


def act_two():
    """
    Placeholder docstring to remove errors
    """
    clear_terminal()
    txt_effect(narrative.ACT_TWO)
    choose_your_path('Do you go to the Bar? or the port Offices? (O/B)\n',
                     'o',
                     'b',
                     'Invalid choice, please choose a destination.',
                     enter_office,
                     visit_bar
                     )

#  Chapter 2 Fork 1


def visit_office():
    """
    Placeholder docstring to remove errors
    """
    clear_terminal()
    txt_effect(narrative.LEAVE_BAR_AFTER_DRINK)
    txt_effect(narrative.PORT_OFFICE)
    choose_your_path('Press Enter to talk to the girl.\n',
                     '',
                     '',
                     'Invalid choice, please report what has happened.',
                     make_report,
                     make_report
                     )


def make_report():
    '''
    placeholder docstring
    '''
    clear_terminal()
    txt_effect(narrative.TALK_TO_GIRL_1)
    print(Fore.RED)
    txt_effect(narrative.TALK_TO_GIRL_2)
    print(Style.RESET_ALL)
    txt_effect(narrative.TALK_TO_GIRL_3)
    print(Fore.RED)
    txt_effect(narrative.TALK_TO_GIRL_4)
    choose_your_path('Press Enter to start Act 3.\n',
                     '',
                     '',
                     'Invalid choice, press Enter.',
                     act_three,
                     act_three
                     )


def enter_office():
    '''
    directly enter the office
    '''
    clear_terminal()
    txt_effect(narrative.PORT_OFFICE)
    choose_your_path('Press Enter to talk to the girl.\n',
                     '',
                     '',
                     'Invalid choice, please report what has happened.',
                     make_report,
                     make_report
                     )


#  Act 2 Fork 2


def visit_bar():
    """
    Placeholder docstring to remove errors
    """
    clear_terminal()
    print(Fore.LIGHTWHITE_EX + ascii_art.SALOON)
    txt_effect(narrative.VISIT_BAR)
    choose_your_path('Do you Gamble or go get a Drink? (G/D)\n',
                     'g',
                     'd',
                     'Invalid choice, please choose your next move.',
                     enter_room,
                     drink
                     )


def refuse_drink_visit_office():
    """
    Placeholder docstring to remove errors
    """
    clear_terminal()
    txt_effect(narrative.CUT_OFF)
    txt_effect(narrative.PORT_OFFICE)
    choose_your_path('Press Enter to talk to the girl.\n',
                     '',
                     '',
                     'Invalid choice, please report what has happened.',
                     make_report,
                     make_report
                     )

# Act 2 Fork 2.1 (Russian roulette)


def enter_room():
    '''
    creepy room
    '''
    clear_terminal()
    txt_effect(narrative.ENTER_ROOM)
    choose_your_path('Do you Stay or go back to the Bar? (S/B)\n',
                     's',
                     'b',
                     'Invalid choice, please choose your next move.',
                     gamble_room,
                     drink
                     )


def gamble_room():
    '''
    get ready to play
    '''
    clear_terminal()
    txt_effect(narrative.GAMBLE)
    choose_your_path('Do you Run or Play? (R/P)\n',
                     'r',
                     'p',
                     'Invalid choice, please choose your next move.',
                     pass_functions_into_choices,
                     russian_roulette,
                     narrative.RUN_FROM_GAME,
                     game_over
                     )


def survive_game_enter_office():
    '''
    directly enter the office after russian roulette
    '''
    clear_terminal()
    txt_effect(narrative.ROULETTE_VICTORY + narrative.PORT_OFFICE)
    choose_your_path('Press Enter to talk to the girl.\n',
                     '',
                     '',
                     'Invalid choice, please report what has happened.',
                     make_report,
                     make_report
                     )

# Act 2 Fork 2.2


def drink():
    """
    Placeholder docstring to remove errors
    """
    clear_terminal()
    txt_effect(narrative.DRINK_AT_BAR)
    choose_your_path('Do you want another Drink? (Y/N)\n',
                     'n',
                     'y',
                     'Invalid choice, Another drink?',
                     pass_functions_into_choices,
                     another_drink,
                     narrative.LEAVE_BAR_AFTER_DRINK,
                     visit_office
                     )


def another_drink():
    """
    Placeholder docstring to remove errors
    """
    clear_terminal()
    print(Style.RESET_ALL)
    if narrative.TOTAL_DRINKS > 3:
        refuse_drink_visit_office()
    else:
        narrative.TOTAL_DRINKS += 1
        txt_effect(f'''
        "Can i have another?"

        "Sure, number {narrative.TOTAL_DRINKS} coming right up."
        ''')
        choose_your_path('Do you want another Drink? (Y/N)\n',
                         'n',
                         'y',
                         'Invalid choice, Another drink?',
                         pass_functions_into_choices,
                         another_drink,
                         narrative.LEAVE_BAR_AFTER_DRINK,
                         visit_office
                         )


##############################################################################
# Act 3


def act_three():
    """
    Placeholder docstring to remove errors
    """
    clear_terminal()
    txt_effect(narrative.ACT_THREE)
    choose_your_path('Press Enter to talk to Ishmel.\n',
                     '',
                     '',
                     'Invalid choice, You must talk to Ishmel.',
                     join_ishmel,
                     join_ishmel
                     )


def join_ishmel():
    """
    Placeholder docstring to remove errors
    """
    clear_terminal()
    print(Fore.LIGHTRED_EX + ascii_art.BOAT)
    print(Style.RESET_ALL)
    txt_effect(narrative.TALK_TO_ISHMEL)
    choose_your_path('Do you Fish? (Y/N)\n',
                     'y',
                     'n',
                     'Invalid choice, Do you Fish?',
                     go_fish,
                     sleep
                     )


# Act three
# Fork 1

def go_fish():
    """
    Placeholder docstring to remove errors
    """
    clear_terminal()
    print(Fore.BLUE + ascii_art.FISH)
    print(Style.RESET_ALL)
    txt_effect(narrative.GO_FISH)
    choose_your_path('Press Enter to begin fishing.\n',
                     '',
                     '',
                     'Invalid choice, Press Enter to Fish.',
                     fish_game,
                     fish_game
                     )


# Act 3
# Fork 2


def sleep():
    """
    Placeholder docstring to remove errors
    """
    clear_terminal()
    txt_effect(narrative.REFUSE_FISHING)
    choose_your_path('Press Enter to go speak with the men.\n',
                     '',
                     '',
                     'Invalid choice, You must speak to these men.',
                     river_discovery,
                     river_discovery
                     )


# Act three
# Fork 1 & 2 lead here so from here out i will refer to
# the forks as 1 or 2 and disregard the first fork


def river_discovery():
    '''
    placeholder docstring
    '''
    clear_terminal()
    txt_effect('       Standing on the deck are two men dressed in overalls.')
    print(Fore.RED)
    txt_effect(narrative.PLANTATION_MECHANICS_1)
    print(Style.RESET_ALL)
    txt_effect(narrative.PLANTATION_MECHANICS_2)
    print(Fore.RED)
    txt_effect(narrative.PLANTATION_MECHANICS_3)
    print(Style.RESET_ALL)
    choose_your_path('Go with the men? or Stay with Ishmel? (G/S)\n',
                     'g',
                     's',
                     'Invalid choice, Please choose.',
                     go_with_men,
                     stay_with_ishmel
                     )

# Fork 1


def stay_with_ishmel():
    '''
    placeholder docstring
    '''
    clear_terminal()
    txt_effect(narrative.PLANTATION_WITH_ISHMEL)
    choose_your_path('Press Enter to tie off the boat.\n',
                     '',
                     '',
                     'Invalid choice, Press Enter.',
                     arrive_plantation,
                     arrive_plantation
                     )


# Fork 2


def go_with_men():
    '''
    placeholder docstring
    '''
    clear_terminal()
    if narrative.GO_FISHING:
        if narrative.FISH_CAUGHT >= 1:
            txt_effect(f"""
        'Of course, I'm very curious to find out what happened on that boat.'

        You jump across onto the mens boat and Ishmel tosses a small parcel
        over to you, it contains {narrative.FISH_CAUGHT} fish.

        'Your catch, you boys will need to eat, see you around {name}.
        And be careful, it's a jungle out there.'

        he then proceeds to laugh hysterically.
        """)
            txt_effect(narrative.FIND_BOAT)
            choose_your_path('Board the boat or Wait here? (B/W)\n',
                             'b',
                             'w',
                             'Invalid choice, Please choose.',
                             board_boat,
                             wait_on_mechanics
                             )
        else:
            txt_effect(narrative.OLD_BOAT)
            txt_effect(narrative.FIND_BOAT)
            choose_your_path('Board the boat or Wait here? (B/W)\n',
                             'b',
                             'w',
                             'Invalid choice, Please choose.',
                             board_boat,
                             wait_on_mechanics
                             )
    else:
        txt_effect(narrative.OLD_BOAT)
        txt_effect(narrative.FIND_BOAT)
        choose_your_path('Board the boat or Wait here? (B/W)\n',
                         'b',
                         'w',
                         'Invalid choice, Please choose.',
                         board_boat,
                         wait_on_mechanics
                         )


def board_boat():
    '''
    placeholder docstring
    '''
    clear_terminal()
    txt_effect(narrative.BOARD_BOAT)
    print(Fore.RED)
    txt_effect(narrative.BOARD_BOAT_2)
    print(Style.RESET_ALL)
    txt_effect(narrative.BOARD_BOAT_3)
    choose_your_path('Leave Africa and go home or Continue? (L/C)\n',
                     'l',
                     'c',
                     'Invalid choice, Please choose.',
                     leave_africa,
                     arrive_plantation
                     )


def wait_on_mechanics():
    '''
    placeholder docstring
    '''
    clear_terminal()
    txt_effect(narrative.WAIT_ON_MECHANICS_1)
    print(Fore.RED)
    txt_effect(narrative.WAIT_ON_MECHANICS_2)
    print(Style.RESET_ALL)
    txt_effect(narrative.BOARD_BOAT_3)
    choose_your_path('Leave Africa and go home or Continue? (L/C)\n',
                     'l',
                     'c',
                     'Invalid choice, Please choose.',
                     decide_to_leave,
                     arrive_plantation_mechanics
                     )


# Fork  2.1


def decide_to_leave():
    '''
    placeholder docstring
    '''
    txt_effect(narrative.DECIDE_TO_LEAVE_1)
    print(Fore.RED)
    txt_effect(narrative.DECIDE_TO_LEAVE_2)
    print(Style.RESET_ALL)
    txt_effect(narrative.DECIDE_TO_LEAVE_2)
    choose_your_path('Press Enter to go to the town.\n',
                     '',
                     '',
                     'Invalid choice, Press Enter.',
                     leave_africa,
                     leave_africa
                     )


def leave_africa():
    '''
    placeholder docstring
    '''
    clear_terminal()
    txt_effect(narrative.LEAVE_AFRICA)
    print(Fore.GREEN)
    txt_effect(narrative.OUTRO_QUOTE)
    print(Style.RESET_ALL)
    txt_effect(narrative.END)
    choose_your_path('View the Menu or quit game? (M/Q)\n',
                     'm',
                     'q',
                     'Invalid choice, Please choose.',
                     menu,
                     game_over_alive
                     )

# Fork 1.2 & Fork 2.2


def arrive_plantation():
    '''
    placeholder docstring
    '''
    clear_terminal()
    txt_effect(narrative.ARRIVE_PLANTATION)
    print(Fore.GREEN)
    txt_effect(narrative.OUTRO_QUOTE)
    print(Style.RESET_ALL)
    txt_effect(narrative.END)
    choose_your_path('View the Menu or quit game? (M/Q)\n',
                     'm',
                     'q',
                     'Invalid choice, Please choose.',
                     menu,
                     game_over_alive
                     )


def arrive_plantation_mechanics():
    '''
    placeholder docstring
    '''
    clear_terminal()
    txt_effect(narrative.ARRIVE_PLANTATION_MECHANICS)
    print(Fore.GREEN)
    txt_effect(narrative.OUTRO_QUOTE)
    print(Style.RESET_ALL)
    txt_effect(narrative.END)
    choose_your_path('View the Menu or quit game? (M/Q)\n',
                     'm',
                     'q',
                     'Invalid choice, Please choose.',
                     menu,
                     game_over_alive
                     )


pass_functions_into_choices(narrative.TITLE_TEXT, begin_game)
