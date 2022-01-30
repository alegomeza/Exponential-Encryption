from youtube_dl import main
from message import Message
from key_code import Key_code
from encryption import Encryption
import os

def main_screen() -> str:
    print('''
    Greetings! The options are:

    [K]ey_code
    [M]essage    
    [E]xit
    ''')
    answer = str(input('Which option do you choose?')).upper()
    return answer

def run():
    answer = main_screen()
    if answer == 'K':
        pass
    
    elif answer == 'M':
        pass

    elif answer == 'E':
        pass

    else:
        print('Option not found, try again.')
        run()

if __name__ == '__main__':
    run()