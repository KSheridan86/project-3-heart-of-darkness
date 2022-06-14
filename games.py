'''
Games
Russian roulette and Fishing, these can be played depending
on the users choices.
'''
import random
import time
from colorama import init
from colorama import Fore, Style
import narrative
import functions
import ascii_art
init()


def russian_roulette():
    '''
    Loads the russian roulette game
    Generates a virtual 6 shot revolver randomly assigns the bullet
    to a chamber and spins the cylinder.
    User fires first, then a randomly generated computer shot,
    keeps taking shots back and forth until someone is dead.
    '''
    barrel = [1, 2, 3, 4, 5, 6]
    functions.clear_terminal()
    print(Fore.LIGHTBLUE_EX + ascii_art.GUN)
    print(Style.RESET_ALL)
    functions.txt_effect(
        '    You pick up the revolver and hold it to your head.')
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
        functions.clear_terminal()
        print(Fore.CYAN + ascii_art.CLICK)
        time.sleep(1.5)
        print(Style.RESET_ALL)
        shot = barrel[random.randrange(0, len(barrel))]
        barrel.remove(shot)
        if shot == kill_shot:
            functions.clear_terminal()
            print(Fore.RED + ascii_art.BANG)
            functions.game_over()
        else:
            functions.clear_terminal()
            print(Fore.CYAN + ascii_art.EMPTY)
            time.sleep(1.5)
            functions.clear_terminal()
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
        functions.txt_effect(narrative.MANS_TURN)
        time.sleep(1.5)
        functions.clear_terminal()
        print(Fore.CYAN + ascii_art.CLICK)
        if shot == kill_shot:
            time.sleep(1.5)
            functions.clear_terminal()
            print(Fore.RED + ascii_art.BANG)
            print(Style.RESET_ALL)
            time.sleep(1.5)
            functions.survive_game_enter_office()
        else:
            time.sleep(1.5)
            functions.clear_terminal()
            print(Fore.CYAN + ascii_art.EMPTY)
            time.sleep(1.5)
            functions.clear_terminal()
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
    functions.clear_terminal()
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
        functions.choose_your_path('\n    Keep Fishing? (Y/N)\n',
                                   'y',
                                   'n',
                                   '      Invalid choice, Keep Fishing?',
                                   fish_game,
                                   functions.sleep
                                   )
    else:
        print('     No luck, try again?\n')
        print(f"    You have caught {narrative.FISH_CAUGHT} fish.\n")
        functions.choose_your_path('      Keep trying? (Y/N)\n',
                                   'y',
                                   'n',
                                   '      Invalid choice, Keep trying?',
                                   fish_game,
                                   functions.sleep
                                   )
