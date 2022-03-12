from graphs import Node, Graph
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


def exit_(data = None):
    exit()
    return ' ' , data

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

input('yy')
@clear_screen
# %%
def key_screen(encryp : Encryption):
    print('''
    ::: [K]ey_code :::''')
    answer = str(input('''
    Do you have a KeyCode? [y/n] ''')).upper()
    if answer == 'Y':
        print('Enter the values of k1, k2 and k3.')
        try:
            k1 = int(input('k1:? '))
            k2 = int(input('k2:? '))
            k3 = int(input('k3:? '))
            encryp.key_code = KeyCode(k1, k2, k3)
            input(f'{encryp.key_code}')
            input('KeyCode is load')
        except ValueError:
            input('Value entered is wrong')
            return 'ks' , encryp
        return 'fs' , encryp

    elif answer == 'N':
        print('... generating key ...')
        key_code = KeyCode()
        encryp.key_code = key_code.generate_key()
        print('''
    The values  of k1, k2 and k3 are''')
        print(f'    {encryp.key_code}')
        input('    Copy the values to a safe place.')
        return 'fs' , encryp
    else:
        input('Option not found, try again.')
        return 'ks' , encryp
    
    input('here2')
# %%

@clear_screen
def main_screen(encryp : Encryption) -> str:
    convert_answer = {'K':'ks', 'M':'ms', 'E':'exit'}
    print('''
    Greetings! The options are:

    Key Code    [K]
    Message     [M]
    Exit        [E]''')
    answer = str(input('''
    Which option do you choose? ''')).upper()
    answer = convert_answer[answer]
    return answer , encryp


@clear_screen
def main():
    
    encryp = Encryption()
    
    # first screen
    fs = Node(main_screen, encryp) 
    
    # key screen
    ks = Node(key_screen)
    
    # message screen
    ms = Node(message_screen)
    
    # node for exit
    ex = Node(exit_)
    
    # raise ValueError('MEsaje re x')
    
    fs.next = {'fs': fs, 'ks': ks, 'ms': ms, 'exit': ex}
    ks.next = {'fs': fs, 'ks': ks, 'ms': ms}
    ms.next = {'fs': fs, 'ks': ks, 'ms': ms}
    
    main_graphs = Graph(fs)
    
    while True:
        
        input(f'{main_graphs.current_node}')
        main_graphs.run()

# =============================================================================
#     answer = main_screen()
#     
#     if answer == 'K':
#         key_code = key_screen()
#         input('Now you need a message.')
#         message = message_screen()
#         encrypt_or_decrypt(message, key_code)
#         run()
# 
#     elif answer == 'M':
#         message = message_screen()
#         input('Now you need a key_code.')
#         key_code = key_screen()
#         encrypt_or_decrypt(message, key_code)
#         run()
# 
#     elif answer == 'E':
#         exit()
# 
#     else:
#         input('Option not found, try again.')
#         run()
#         
#     exit()
# =============================================================================


if __name__ == '__main__':
    main()
