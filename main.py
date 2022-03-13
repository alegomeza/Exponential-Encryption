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
    return 'exit' , data

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
def message_screen(encryp : Encryption):
    print('\t\t::: [M]essage :::')
    print('''
    New Message     [N]
    Decrypt Message [D]
    Encrypt Message [E]
    View Message    [V]''')
    answer = str(input('\tWhich option do you choose? ')).upper()
    if answer == 'N':
        text = str(input('What is your message? '))
        encryp.message = text
        print(encryp)
        return 'ms' , encryp
        
    # elif answer == 'N':
    #     text = str(input('What is your message? '))
    #     message.text = text
    #     return message
    else:
        input('\tOption not found, try again.')
        return message_screen()


@clear_screen
def key_screen(encryp : Encryption):
    print('\t\t::: [K]ey_code :::\n')
    answer = str(input('\tDo you have a KeyCode? [y/n] ')).upper()
    if answer == 'Y':
        print('\tEnter the values of k1, k2 and k3.\n')
        try:
            k1 = int(input('\tk1:?'))
            k2 = int(input('\tk2:?'))
            k3 = int(input('\tk3:?'))
            encryp.key_code = KeyCode(k1, k2, k3)
            input('\tKeyCode is load')
        except ValueError:
            input('\tValue entered is wrong')
            return 'ks' , encryp
        return 'fs' , encryp

    elif answer == 'N':
        print('... generating key')
        key_code = KeyCode()
        key_code.generate_key()
        encryp.key_code = key_code
        print('''
    The values  of k1, k2 and k3 are\n''')
        print(str(encryp.key_code).replace('k','\tk'))
        input('    Copy the values to a safe place.')
        return 'fs' , encryp
    else:
        input('Option not found, try again.')
        return 'ks' , encryp
    
    input('here2')

@clear_screen
def main_screen(encryp : Encryption) -> str:
    convert_answer = {'K':'ks', 'M':'ms', 'E':'exit'}
    print('''
    Greetings! The options are:

    Key Code    [K]
    Message     [M]
    Exit        [E]''')
    try:
        answer = str(input('\n\tWhich option do you choose? ')).upper()
        answer = convert_answer[answer]
    except KeyError:
        input('\tOption not found, try again.')
        return 'fs' , encryp
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
    ex.next = {'exit':ex}
    
    main_graphs = Graph(fs)
    
    while True:
        
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

# =============================================================================
# # %%
# =============================================================================

if __name__ == '__main__':
    main()
