"""
This is a choose your own adventure game, based loosely on the theme's of
the book The Heart of Darkness by Joseph Conrad.
You must navigate your way up the Congo river at the height of the
Belgian colonial conquest.
"""
import time
import random
import sys
import os
from colorama import init
from colorama import Fore, Style
import narrative
import ascii_art
import menu
init()


# Games
# Russian roulette and Fishing, these can be played depending
# on the users choices.
##############################################################################

def russian_roulette():
    '''
    Loads the russian roulette game
    Generates a virtual 6 shot revolver randomly assigns the bullet
    to a chamber and spins the cylinder.
    User fires first, then a randomly generated computer shot,
    keeps taking shots until someone is dead.
    '''
    barrel = [1, 2, 3, 4, 5, 6]
    clear_terminal()
    print(Fore.LIGHTBLUE_EX + ascii_art.GUN)
    print(Style.RESET_ALL)
    txt_effect('    You pick up the revolver and hold it to your head.')
    kill_shot = random.randrange(1, 6)

    def pull_trigger():
        '''
        Asks you to pull the trigger of a six shot revolver.
        '''
        trigger = input('\n Press X and then Enter to fire.\n').lower()
        if trigger == 'x':
            take_shot()
        else:
            print('     Wrong key, try again.')

    def take_shot():
        '''
        Checks if you're dead and continues accordingly.
        '''
        clear_terminal()
        print(Fore.CYAN + ascii_art.CLICK)
        time.sleep(1.5)
        print(Style.RESET_ALL)
        shot = barrel[random.randrange(0, len(barrel))]
        barrel.remove(shot)
        if shot == kill_shot:
            clear_terminal()
            print(Fore.RED + ascii_art.BANG)
            game_over()
        else:
            clear_terminal()
            print(Fore.CYAN + ascii_art.EMPTY)
            time.sleep(1.5)
            clear_terminal()
            print(Fore.CYAN + ascii_art.SURVIVE)
            print(Style.RESET_ALL)
            time.sleep(1.5)
            comp_shot()

    def comp_shot():
        '''
        Fires for the computer and checks whether to continue or not.
        '''
        shot = barrel[random.randrange(0, len(barrel))]
        barrel.remove(shot)
        txt_effect(narrative.MANS_TURN)
        time.sleep(1.5)
        clear_terminal()
        print(Fore.CYAN + ascii_art.CLICK)
        if shot == kill_shot:
            time.sleep(1.5)
            clear_terminal()
            print(Fore.RED + ascii_art.BANG)
            print(Style.RESET_ALL)
            time.sleep(1.5)
            survive_game_enter_office()
        else:
            time.sleep(1.5)
            clear_terminal()
            print(Fore.CYAN + ascii_art.EMPTY)
            time.sleep(1.5)
            clear_terminal()
            print(Fore.CYAN + ascii_art.YOUR_TURN)
            print(Style.RESET_ALL)
            time.sleep(1.5)
            pull_trigger()

    pull_trigger()


def fish_game():
    """
    Randomly generates a number between 1 and 100 then checks
    to see if that number is prime.
    1 in 4 chance it is
    A prime number = a caught fish.
    """
    clear_terminal()
    print(Fore.BLUE + ascii_art.FISH)
    narrative.GO_FISHING = True
    print(Style.RESET_ALL)

    num = random.randrange(1, 100)

    def cast_line(num):
        if num == 1:
            return True
        else:
            for i in range(2, num):
                if num % i == 0:
                    return False
        return True

    answer = cast_line(num)

    if answer:
        narrative.FISH_CAUGHT += 1
        print('     You caught a Fish!!\n')
        print(f"    You now have {narrative.FISH_CAUGHT} fish in your bucket.")
        choose_your_path('\n    Keep Fishing? (Y/N)\n',
                         'y',
                         'n',
                         '      Invalid choice, Keep Fishing?',
                         fish_game,
                         sleep
                         )
    else:
        print('     No luck, try again?\n')
        print(f"    You have caught {narrative.FISH_CAUGHT} fish.\n")
        choose_your_path('      Keep trying? (Y/N)\n',
                         'y',
                         'n',
                         '      Invalid choice, Keep trying?',
                         fish_game,
                         sleep
                         )


# Functions used throughout the story.
###############################################################################


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
    elif choice == 'menu':
        menu.menu()
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


def pass_args_in(text, function):
    '''
    Starts the game.
    Streamlines the process of calling the choose_your_path
    function (above), arguments are passed to one of the functions inside the
    choose_your_path function instead of having to write
    individual functions to pass in for every fork in the path.
    '''
    clear_terminal()
    txt_effect(f"{text}")
    function()


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
    It resets colorama colors also.
    '''
    print(Style.RESET_ALL)
    os.system('cls' if os.name == 'nt' else 'clear')


def game_over():
    '''
    Prints a game over graphic and offers options to start again.
    '''
    time.sleep(2)
    clear_terminal()
    print(Fore.RED + ascii_art.GAME_OVER)
    choose_your_path('      Would you like to play again? [Y/N]\n',
                     'y',
                     'n',
                     "      This is not a valid selection....Try again.",
                     menu.menu,
                     end_story
                     )


def game_over_alive():
    '''
    Prints a game over graphic and offers options to start again.
    '''
    clear_terminal()
    print(Fore.BLUE + ascii_art.GAME_OVER_ALIVE)
    choose_your_path('      Would you like to play again? [Y/N]\n',
                     'y',
                     'n',
                     "      This is not a valid selection....Try again.",
                     menu.menu,
                     end_story
                     )


def end_story():
    '''
    Ends the game.
    '''
    print(Style.RESET_ALL)
    print('     Thanks for playing, come back soon.')


def sleep_animation():
    '''
    Recreates a basic animation by looping over ascii art characters
    printing them and after a time delay clearing the console and
    printing the next character
    '''
    for wake in ascii_art.w_list:
        for i in range(2):
            for zzz in ascii_art.z_list:
                for j in range(2):
                    # num = 2
                    # while num > 0:
                    clear_terminal()
                    print(Fore.LIGHTGREEN_EX + Style.DIM)
                    print(zzz)
                    # num -= 1
                    time.sleep(.5)
        clear_terminal()
        print(Fore.LIGHTGREEN_EX + Style.DIM)
        print(wake)
        time.sleep(.25)


def begin_game():
    '''
    Asks you to begin the game, prints the first
    paragraph and loads the first choice.
    '''
    print()
    answer = input(
        Fore.YELLOW + '    Would you like to start the story? (Y/N)\n').lower()
    if answer == 'y':
        clear_terminal()
        print(Fore.LIGHTYELLOW_EX)
        print(ascii_art.ACT_1)
        print(Style.RESET_ALL)
        txt_effect(intro_text)
        choose_your_path('      Volunteer or Stay with the boat? [V/S]\n',
                         'v',
                         's',
                         "      This is not a valid selection....Try again.",
                         volunteer,
                         stay_with_boat
                         )
    elif answer == 'n':
        game_over_alive()
    elif answer == 'menu':
        menu.menu()
    else:
        print("This is not a valid selection....Try again.")
        begin_game()


# Start of the story.
# Name is required to continue, must be less than 50 characters.
# All characters are accepted.
###############################################################################

print(Fore.LIGHTYELLOW_EX)
print(ascii_art.TITLE)
print(Fore.GREEN + Style.BRIGHT)
txt_effect(narrative.INTRO)
print(Style.RESET_ALL)
time.sleep(.5)
name = input('  Please enter your name to continue.......').capitalize()
while not name or len(name) > 50:
    name = input(narrative.NAME_VALIDATION_ERROR).capitalize()


intro_text = f"""
        The year was 1902 and the steamboat I was travelling on had
        blown an engine. Miles from the town we had left yesterday and
        half a world from home.\n
        This damn river was trying to kill me....\n
        {name} a voice called, it was the Captain.
        The radio is busted. We need 2 volunteers to go and alert
        the station master of what has happened...

        """

# Below are the functions that dictate the path of the game.
# They have been laid out in the order they appear in the game.
###############################################################################
# Act 1
# Fork 1


def volunteer():
    '''
    Runs if the user chooses to volunteer, this is the first
    fork of the game, both options have a valid path through
    to act 2.
    '''
    clear_terminal()
    print(Fore.GREEN + ascii_art.JUNGLE)
    print(Style.RESET_ALL)
    txt_effect(narrative.VOLUNTEER)
    choose_your_path('      Do you get Angry or stay Calm? (A/C)\n',
                     'a',
                     'c',
                     '      Invalid choice, please choose...',
                     pass_args_in,
                     dont_fight_sven,
                     narrative.FIGHT_SVEN,
                     game_over
                     )


def dont_fight_sven():
    '''
    Runs if the user chooses to stay calm, it's the correct choice,
    the user survives to make another choice.
    Prints text, loads question.
    '''
    clear_terminal()
    txt_effect(narrative.DONT_FIGHT)
    choose_your_path('      Do you drink the Water or the Bourbon? (W/B)\n',
                     'w',
                     'b',
                     '      Invalid choice, please choose a drink.',
                     pass_args_in,
                     drink_bourbon,
                     narrative.WATER,
                     game_over
                     )


# Act 1
# Fork 1.1


def drink_bourbon():
    """
    Runs if the user chooses bourbon, it's the correct choice,
    user survives and is prompted to press enter to begin act 2.
    """
    clear_terminal()
    txt_effect(narrative.BOURBON)
    choose_your_path('      Press Enter to start Act two.\n',
                     '',
                     '',
                     '      Invalid choice, press Enter.',
                     act_two,
                     act_two
                     )

# Act 1
# Fork 2


def stay_with_boat():
    """
    Runs if the user chooses to stay with the boat.
    This is the wrong path, user is killed.
    """
    clear_terminal()
    txt_effect(narrative.STAY)
    choose_your_path(
                '      Stay and help or take what you can and Escape? (S/E)\n',
                's',
                'e',
                '       Invalid choice, please choose a path.',
                pass_args_in,
                escape_boat,
                narrative.STAY_ON_BOAT,
                game_over
                )

# Act 1 Fork 2.1


def escape_boat():
    """
    Runs if the user chooses to escape into the jungle.
    For this particular fork it's the path to survival.
    """
    clear_terminal()
    txt_effect(narrative.ESCAPE_BOAT)
    choose_your_path('      Press Enter to start Act two.\n',
                     '',
                     '',
                     '      Invalid choice, press Enter.',
                     act_two,
                     act_two
                     )


##############################################################################
# Act 2


def act_two():
    """
    Begins act two and asks you to choose
    your next move.
    """
    clear_terminal()
    print(Fore.LIGHTYELLOW_EX)
    print(ascii_art.ACT_2)
    print(Style.RESET_ALL)
    txt_effect(narrative.ACT_TWO)
    choose_your_path('     Do you go to the Bar? or the port Offices? (O/B)\n',
                     'o',
                     'b',
                     '      Invalid choice, please choose a destination.',
                     enter_office,
                     visit_bar
                     )

# Act 2
# Fork 1


def visit_office():
    """
    Runs when you visit the office, leads you to talk to the girl
    and begin act 3.
    """
    clear_terminal()
    txt_effect(narrative.LEAVE_BAR_AFTER_DRINK)
    txt_effect(narrative.PORT_OFFICE)
    choose_your_path('      Press Enter to talk to the girl.\n',
                     '',
                     '',
                     '      Invalid choice, please report what has happened.',
                     make_report,
                     make_report
                     )


def make_report():
    '''
    Prints the conversation between you and the girl
    in different colors and asks you to press Enter
    to begin act three.
    '''
    clear_terminal()
    txt_effect(narrative.TALK_TO_GIRL_1)
    print(Fore.LIGHTCYAN_EX)
    txt_effect(narrative.TALK_TO_GIRL_2)
    print(Style.RESET_ALL)
    txt_effect(narrative.TALK_TO_GIRL_3)
    print(Fore.LIGHTCYAN_EX)
    txt_effect(narrative.TALK_TO_GIRL_4)
    choose_your_path('      Press Enter to start Act 3.\n',
                     '',
                     '',
                     '      Invalid choice, press Enter.',
                     act_three,
                     act_three
                     )


def enter_office():
    '''
    Prints the text to directly enter the office and prompts the user
    to press Enter to speak to the girl.
    '''
    clear_terminal()
    txt_effect(narrative.PORT_OFFICE)
    choose_your_path('      Press Enter to talk to the girl.\n',
                     '',
                     '',
                     '      Invalid choice, please report what has happened.',
                     make_report,
                     make_report
                     )


# Act 2
# Fork 2


def visit_bar():
    """
    Prints the text for entering the bar and asks you to choose
    your next move.
    """
    clear_terminal()
    print(Fore.LIGHTWHITE_EX + ascii_art.SALOON)
    txt_effect(narrative.VISIT_BAR)
    choose_your_path('      Do you Gamble or go get a Drink? (G/D)\n',
                     'g',
                     'd',
                     '      Invalid choice, please choose your next move.',
                     enter_room,
                     drink
                     )


def refuse_drink_visit_office():
    """
    Cut off from the bar you must go and speak to the girl in the offices.
    """
    clear_terminal()
    txt_effect(narrative.CUT_OFF)
    txt_effect(narrative.PORT_OFFICE)
    choose_your_path('      Press Enter to talk to the girl.\n',
                     '',
                     '',
                     '      Invalid choice, please report what has happened.',
                     make_report,
                     make_report
                     )

# Act 2 Fork 2.1 (Russian roulette)


def enter_room():
    '''
    If you choose to gamble this function gives you the opportunity
    to change your mind.
    '''
    clear_terminal()
    txt_effect(narrative.ENTER_ROOM)
    choose_your_path('      Do you Stay or go back to the Bar? (S/B)\n',
                     's',
                     'b',
                     '      Invalid choice, please choose your next move.',
                     gamble_room,
                     drink
                     )


def gamble_room():
    '''
    If you choose to gamble this function gives you the opportunity
    to change your mind. But unlike the function above 'enter_room()'
    this is a trick question, if you change your mind you die.
    '''
    clear_terminal()
    print(Fore.LIGHTRED_EX + ascii_art.SNAP)
    print(Style.RESET_ALL)
    txt_effect(narrative.GAMBLE)
    choose_your_path('      Do you Run or Play? (R/P)\n',
                     'r',
                     'p',
                     '      Invalid choice, please choose your next move.',
                     pass_args_in,
                     russian_roulette,
                     narrative.RUN_FROM_GAME,
                     game_over
                     )


def survive_game_enter_office():
    '''
    This function runs if you survive the russian roulette game.
    Your challenger is dead and you go straight to the offices
    to speak to the girl.
    '''
    clear_terminal()
    txt_effect(narrative.ROULETTE_VICTORY + narrative.PORT_OFFICE)
    choose_your_path('      Press Enter to talk to the girl.\n',
                     '',
                     '',
                     '      Invalid choice, please report what has happened.',
                     make_report,
                     make_report
                     )

# Act 2 Fork 2.2


def drink():
    """
    This runs if you enter the bar and go straight for a drink.
    printing the text and loading the next choice.
    """
    clear_terminal()
    txt_effect(narrative.DRINK_AT_BAR)
    choose_your_path('\n        Do you want another Drink? (Y/N)\n',
                     'n',
                     'y',
                     '      Invalid choice, Another drink?',
                     pass_args_in,
                     another_drink,
                     narrative.LEAVE_BAR_AFTER_DRINK,
                     visit_office
                     )


def another_drink():
    """
    This runs if the user requests another drink.
    It checks if they have had more than 3 drinks already, if not
    you get another, if so you are refused and sent to the office.
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
        choose_your_path('\n        Do you want another Drink? (Y/N)\n',
                         'n',
                         'y',
                         '      Invalid choice, Another drink?',
                         pass_args_in,
                         another_drink,
                         narrative.LEAVE_BAR_AFTER_DRINK,
                         visit_office
                         )


##############################################################################
# Act 3
# First section of act 3 contains the fishing game.


def act_three():
    """
    Begins act three, user meets Ishmel and is prompted to press
    Enter to speak to him.
    """
    clear_terminal()
    print(Fore.LIGHTYELLOW_EX)
    print(ascii_art.ACT_3)
    print(Style.RESET_ALL)
    txt_effect(narrative.ACT_THREE)
    choose_your_path('      Press Enter to talk to Ishmel.\n',
                     '',
                     '',
                     '      Invalid choice, You must talk to Ishmel.',
                     join_ishmel,
                     join_ishmel
                     )


def join_ishmel():
    """
    The natural progression of act three is to board Ishmels boat
    but here the user is introduced to him and offered the chance to
    play the fishing game.
    """
    clear_terminal()
    print(Fore.LIGHTRED_EX + ascii_art.BOAT)
    print(Style.RESET_ALL)
    txt_effect(narrative.TALK_TO_ISHMEL)
    choose_your_path('      Do you Fish? (Y/N)\n',
                     'y',
                     'n',
                     '      Invalid choice, Do you Fish?',
                     go_fish,
                     sleep
                     )


def go_fish():
    """
    Runs if the user chooses to play the fish game.
    prints an acceptance message and starts the game.
    """
    clear_terminal()
    print(Fore.BLUE + ascii_art.FISH)
    print(Style.RESET_ALL)
    txt_effect(narrative.GO_FISH)
    choose_your_path('      Press Enter to begin fishing.\n',
                     '',
                     '',
                     '      Invalid choice, Press Enter to Fish.',
                     fish_game,
                     fish_game
                     )


def sleep():
    """
    Runs if the user refuses to play the fishing game.
    User goes to sleep, a small sleep animation runs
    and then they are awoken by Ishmel with news.
    """
    clear_terminal()
    txt_effect(narrative.REFUSE_FISHING)
    time.sleep(1)
    sleep_animation()
    print(Style.RESET_ALL)
    txt_effect(narrative.AWAKE)
    choose_your_path('      Press Enter to speak with the men.\n',
                     '',
                     '',
                     '      Invalid choice, You must speak to these men.',
                     river_discovery,
                     river_discovery
                     )

###############################################################################
# Act three
# The first section of act 3 leads here whatever choice is made,
# So the forks begin here and ultimately lead to 1 of 2 possible endings.
###############################################################################


def river_discovery():
    '''
    Following the natural progression you will always meet the
    mechanics from the plantation.
    Here the user meets them and is asked to join them.
    '''
    clear_terminal()
    txt_effect(
        '\n           Standing on the deck are two men dressed in overalls.')
    print(Fore.LIGHTCYAN_EX)
    txt_effect(narrative.PLANTATION_MECHANICS_1)
    print(Style.RESET_ALL)
    txt_effect(narrative.PLANTATION_MECHANICS_2)
    print(Fore.LIGHTCYAN_EX)
    txt_effect(narrative.PLANTATION_MECHANICS_3)
    print(Style.RESET_ALL)
    choose_your_path('      Go with the men? or Stay with Ishmel? (G/S)\n',
                     'g',
                     's',
                     '      Invalid choice, Please choose.',
                     go_with_men,
                     stay_with_ishmel
                     )

# Fork 1


def stay_with_ishmel():
    '''
    Runs if the user chooses to stay with Ishmel.
    It's a short cut to the end of the story.
    Bypassing an arm of narrative with the mechanics and heading
    straight to the plantation for a happy ending.
    '''
    clear_terminal()
    txt_effect(narrative.PLANTATION_WITH_ISHMEL)
    choose_your_path('      Press Enter to tie off the boat.\n',
                     '',
                     '',
                     '      Invalid choice, Press Enter.',
                     arrive_plantation,
                     arrive_plantation
                     )


# Fork 2


def go_with_men():
    '''
    This runs if the user leaves Ishmel and goes in search of
    the original boat and crew.
    '''
    clear_terminal()
    if narrative.GO_FISHING:
        if narrative.FISH_CAUGHT >= 1:
            txt_effect(f"""
        'Of course, I'm very curious to find out what happened on that boat.'

        You jump across onto the mens boat and Ishmel tosses a small parcel
        over to you, it contains {narrative.FISH_CAUGHT} fish.

        'Your catch, you will all need to eat, see you around {name}.
        And be careful... it's a jungle out there.'

        he then proceeds to laugh hysterically.
        """)
            txt_effect(narrative.FIND_BOAT)
            choose_your_path('      Board the boat or Wait here? (B/W)\n',
                             'b',
                             'w',
                             '      Invalid choice, Please choose.',
                             board_boat,
                             wait_on_mechanics
                             )
        else:
            txt_effect(narrative.OLD_BOAT)
            txt_effect(narrative.FIND_BOAT)
            choose_your_path('      Board the boat or Wait here? (B/W)\n',
                             'b',
                             'w',
                             '      Invalid choice, Please choose.',
                             board_boat,
                             wait_on_mechanics
                             )
    else:
        txt_effect(narrative.OLD_BOAT)
        txt_effect(narrative.FIND_BOAT)
        choose_your_path('      Board the boat or Wait here? (B/W)\n',
                         'b',
                         'w',
                         '      Invalid choice, Please choose.',
                         board_boat,
                         wait_on_mechanics
                         )


def board_boat():
    '''
    Runs when the user comes across the original boat
    and boards it to find out what happened.
    '''
    clear_terminal()
    txt_effect(narrative.BOARD_BOAT)
    print(Fore.LIGHTCYAN_EX)
    txt_effect(narrative.BOARD_BOAT_2)
    print(Style.RESET_ALL)
    txt_effect(narrative.BOARD_BOAT_3)
    choose_your_path('      Leave Africa and go home or Continue? (L/C)\n',
                     'l',
                     'c',
                     '      Invalid choice, Please choose.',
                     leave_africa,
                     arrive_plantation_mechanics
                     )


def wait_on_mechanics():
    '''
    Runs when the user comes across the original boat
    and refuses to board, just waits for the mechanics.
    '''
    clear_terminal()
    txt_effect(narrative.WAIT_ON_MECHANICS_1)
    print(Fore.LIGHTCYAN_EX)
    txt_effect(narrative.WAIT_ON_MECHANICS_2)
    print(Style.RESET_ALL)
    txt_effect(narrative.BOARD_BOAT_3)
    choose_your_path('      Leave Africa and go home or Continue? (L/C)\n',
                     'l',
                     'c',
                     '      Invalid choice, Please choose.',
                     decide_to_leave,
                     arrive_plantation_mechanics
                     )


# Fork  2.1


def decide_to_leave():
    '''
    Runs if the user chooses to leave Ishmel and visit the old boat.
    User will be given an option to give up their plans and go
    home to europe.
    '''
    txt_effect(narrative.DECIDE_TO_LEAVE_1)
    print(Fore.LIGHTCYAN_EX)
    txt_effect(narrative.DECIDE_TO_LEAVE_2)
    print(Style.RESET_ALL)
    txt_effect(narrative.DECIDE_TO_LEAVE_2)
    choose_your_path('      Press Enter to go to the town.\n',
                     '',
                     '',
                     '      Invalid choice, Press Enter.',
                     leave_africa,
                     leave_africa
                     )


def leave_africa():
    '''
    Runs if the user chooses to give up and go home.
    Prints the final chapter and offers the user the choice
    to visit the main menu or quit.
    '''
    clear_terminal()
    txt_effect(narrative.LEAVE_AFRICA)
    print(Fore.GREEN)
    txt_effect(narrative.OUTRO_QUOTE)
    print(Style.RESET_ALL)
    txt_effect(narrative.END)
    choose_your_path('      View the Menu or quit game? (M/Q)\n',
                     'm',
                     'q',
                     '      Invalid choice, Please choose.',
                     menu,
                     game_over_alive
                     )

# Fork 1.2 & Fork 2.2


def arrive_plantation():
    '''
    This runs if the user stays with Ishmel and arrives in the
    plantation for a happy ending.
    '''
    clear_terminal()
    txt_effect(narrative.ARRIVE_PLANTATION)
    print(Fore.GREEN)
    txt_effect(narrative.OUTRO_QUOTE)
    print(Style.RESET_ALL)
    txt_effect(narrative.END)
    choose_your_path('      View the Menu or quit game? (M/Q)\n',
                     'm',
                     'q',
                     '      Invalid choice, Please choose.',
                     menu,
                     game_over_alive
                     )


def arrive_plantation_mechanics():
    '''
    This runs after the user journeys with the mechanics and
    arrives at the plantation.
    Prints the end of game message, it's a little more neutral
    than the happy ending.
    '''
    clear_terminal()
    txt_effect(narrative.ARRIVE_PLANTATION_MECHANICS)
    print(Fore.GREEN)
    txt_effect(narrative.OUTRO_QUOTE)
    print(Style.RESET_ALL)
    txt_effect(narrative.END)
    choose_your_path('      View the Menu or quit game? (M/Q)\n',
                     'm',
                     'q',
                     '      Invalid choice, Please choose.',
                     menu,
                     game_over_alive
                     )
