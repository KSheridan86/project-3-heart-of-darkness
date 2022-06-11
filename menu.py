'''
placeholder
'''
import time
from colorama import init
from colorama import Fore, Style
import narrative
import functions
import ascii_art


init()


def menu():
    '''
    Calls the main menu lets the user play the game from any point forward.
    '''
    functions.clear_terminal()
    print(Fore.LIGHTYELLOW_EX + ascii_art.MENU)
    print(Style.RESET_ALL)
    print(narrative.MENU)
    option = input('')
    str(option)
    if option == '1':
        functions.clear_terminal()
        print(Fore.LIGHTYELLOW_EX + ascii_art.MENU)
        print(Style.RESET_ALL)
        print(narrative.ACT_1)
        option = input('')
        str(option)
        if option == '1':
            functions.clear_terminal()
            functions.txt_effect(functions.intro_text)
            functions.choose_your_path(
                '      Volunteer or Stay with the boat? [V/S]\n',
                'v',
                's',
                "This is not a valid selection....Try again.",
                functions.volunteer,
                functions.stay_with_boat
                )
        elif option == '2':
            functions.stay_with_boat()
        elif option == '3':
            functions.volunteer()
        elif option == '4':
            functions.dont_fight_sven()
        else:
            menu()
    elif option == '2':
        functions.clear_terminal()
        print(Fore.LIGHTYELLOW_EX + ascii_art.MENU)
        print(Style.RESET_ALL)
        print(narrative.ACT_2)
        option = input('')
        str(option)
        if option == '1':
            functions.act_two()
        elif option == '2':
            functions.visit_bar()
        elif option == '3':
            functions.make_report()
        else:
            menu()
    elif option == '3':
        functions.clear_terminal()
        print(Fore.LIGHTYELLOW_EX + ascii_art.MENU)
        print(Style.RESET_ALL)
        print(narrative.ACT_3)
        option = input('')
        str(option)
        if option == '1':
            functions.act_three()
        elif option == '2':
            functions.river_discovery()
        elif option == '3':
            functions.go_with_men()
        elif option == '4':
            functions.board_boat()
        else:
            menu()
    elif option == 'q':
        functions.game_over_alive()
    else:
        print('This is an invalid selection....Please try again...')
        time.sleep(2)
        menu()
