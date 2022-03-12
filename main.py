from graphs import *
from keycode import KeyCode
from encryption import Encryption
# from graphs import Graph, Node
import os

gdict = {}

def clear_screen(func):
    def wrapper(*args, **kwargs):
        os.system('clear')
        return func(*args, **kwargs)

    return wrapper


@clear_screen
def encrypt_or_decrypt(message, key_code):
    print('You have a message and key')
    encryption = Encryption(message=message, key_code=key_code)

    def encrypt():
        encryption.encrypt_message()
        print('This is the message:')
        print(message.text)
        input()

    def decrypt():
        encryption.decipher_message()
        print('This is the message:')
        print(message.text)
        input()

    if message.encryption:
        print('The message is encrypted')
        print('... decrypting')
        return decrypt()
    else:
        print('The message is decrypted')
        print('... encrypting')
        return encrypt()


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
def key_screen(data):
    print('::: [K]ey_code :::')
    answer = str(input('Do you already have a key? [y/n] ')).upper()
    if answer == 'Y':
        print('Enter the values of k1, k2 and k3.')
        try:
            data[0].k1 = int(input('k1:? '))
            data[0].k2 = int(input('k2:? '))
            data[0].k3 = int(input('k3:? '))
        except ValueError:
            input('The values entered are wrong.')
            return key_screen()
        ans = str(input('Are the values correct?[Y] ')).upper()
        if ans == 'Y':
            return key_code
        else:
            return key_screen()

    elif answer == 'N':
        print('... generating key ...')
        key_code.generate_key()
        print(f'The values  of p, e and d are')
        print(f'k1: {key_code.k1}')
        print(f'k2: {key_code.k2}')
        print(f'k3: {key_code.k3}')
        input('Copy the values to a safe place.')
        return key_code
    else:
        input('Option not found, try again.')
        return key_screen()


@clear_screen
def main_screen(encryp : Encryption) -> str:
    print('''
    Greetings! The options are:

    Key Code    [K]
    Message     [M]
    Exit        [Any other key]''')
    answer = str(input('''
    Which option do you choose? ''')).upper()
    return answer , encryp


@clear_screen
def run():
    
    encryp = Encryption()
    
    # first screen
    fs = Node(main_screen, encryp) 
    
    # key screen
    ks = Node(key_screen)
    
    # message screen
    ms = Node(message_screen)
    
    # node for exit
    exit = Node(exit)
    
    fs.next = {'K': ks, 'M': ms, 'E': exit}
    ks.next = {'P': fs, 'M': ms}
    ks.next = {'P': fs, 'K': ks}

    answer = main_screen()
    
    if answer == 'K':
        key_code = key_screen()
        input('Now you need a message.')
        message = message_screen()
        encrypt_or_decrypt(message, key_code)
        run()

    elif answer == 'M':
        message = message_screen()
        input('Now you need a key_code.')
        key_code = key_screen()
        encrypt_or_decrypt(message, key_code)
        run()

    elif answer == 'E':
        exit()

    else:
        input('Option not found, try again.')
        run()
        
    exit()


if __name__ == '__main__':
    run()
