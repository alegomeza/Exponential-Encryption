from cgitb import text
from email import message
from youtube_dl import main
from message import Message
from key_code import Key_code
from encryption import Encryption
import os

def clear_screen(func):
    def wrapper(*args,**kwargs):
        os.system('clear')
        return func(*args, **kwargs)
    return wrapper

@clear_screen
def message_screen():
    message = Message(text='')
    print('::: [M]essage :::')
    answer = str(input('Is the message encrypted?[y/n] ')).upper()
    if answer == 'Y':
        try:
            text = str(int(input('What is your message? ')))
            message.text = text
            message.encryption = True
            return message
        except ValueError:
            input('The values entered are wrong')
            return message_screen()
    elif answer == 'N':
        text = str(input('What is your message? '))
        message.text = text
        return message
    else:
        input('Option not found, try again.')
        return message_screen()

@clear_screen
def key_screen():
    print('::: [K]ey_code :::')
    key_code = Key_code()
    answer = str(input('Do you already have a key? [y/n] ')).upper()
    if answer == 'Y':
        print('Enter the values of p,e and d.')
        try:
            key_code.p = int(input('p:? '))
            key_code.e = int(input('e:? '))
            key_code.d = int(input('d:? '))
        except ValueError:
            input('The values entered are wrong.')
            return key_screen()
        ans = str(input('Are the values correct?[Y] ')).upper()
        if ans == 'Y':
            import key_code
        else:
            return key_screen()
        
        return key_code
    elif  answer == 'N':
        print('... generating key ...')
        key_code.generate_key()
        print(f'The values  of p, e and d are')
        print(f'p: {key_code.p}')
        print(f'e: {key_code.e}')
        print(f'd: {key_code.d}')
        input('Copy the values to a safe place.')
        return key_code
    else:
        input('Option not found, try again.')
        return key_screen()

@clear_screen
def main_screen() -> str:
    print('''
    Greetings! The options are:

    [K]ey_code
    [M]essage    
    [E]xit
    ''')
    answer = str(input('Which option do you choose? ')).upper()
    return answer

@clear_screen
def run():
    answer = main_screen()
    if answer == 'K':
        key_code = key_screen()
        input('Now you need a message.')
        message = message_screen()
        input('[Press enter]')
    
    elif answer == 'M':
        message = message_screen()
        input('Now you need a key_code.')
        key_code = key_screen()
        input('[Press enter]')

    elif answer == 'E':
        exit()

    else:
        input('Option not found, try again.')
        run()

if __name__ == '__main__':
    run()