from graphs import Node, Graph
from keycode import KeyCode
from encryption import Encryption
from time import sleep
import os

gdict = {}


def clear_screen(func):
    def wrapper(*args, **kwargs):
        os.system('cls')
        print(
            'By: Alejoock - GitHub: https://github.com/alejogomeza/Exponential-Encryption')
        return func(*args, **kwargs)

    return wrapper


def time_sleep(seconds: int):
    for second in range(seconds):
        second_rest = seconds - second
        print(f'\t{second_rest} seconds')
        sleep(1)


@clear_screen
def exit_(data=None):
    input('\n\t\t::: Bye! :::')
    os.system('cls')
    exit()
    return 'exit', data


@clear_screen
def message_screen(encryp: Encryption):
    if encryp.key_code:
        there_is_key_code = '(There are keys)'
    else:
        there_is_key_code = '(There are not keys)'
    print('\n\t\t::: [M]essage :::')
    print(f'''
\t[I]nput Message
\t[E]ncrypt Message \t{there_is_key_code}
\t[D]ecrypt Message
\t[V]iew Message
\t[R]eturn''')
    answer = str(input('\n\tWhich option do you choose? ')).upper()
    if answer == 'I':
        text = str(input('\n\tWhat is your message?\n\n\t'))
        encryp.message = text
        sure = False
        while not sure:
            print('\n\tYour message is:')
            print(f'\n\t{encryp}')
            ans = str(input('\n\tAre you sure?[Y] ')).upper()
            if ans == 'Y' or ans == '':
                sure = True
            else:
                text = str(input('\n\tWhat is your message?\n\n\t'))
        input('\n\tThe message is load')
        return 'ms', encryp

    elif answer == 'E':
        if encryp.key_code:
            print(f'\n\t{encryp}')
            print('\n\tEncrypting message')
            encryp.encrypt_message()
            input(f'\n\t{encryp}')
            return 'ms', encryp
        else:
            print('\n\tThere are currently no keys')
            ans = str(input('\n\tDo you input keys?[Y]/N ')).upper()
            if ans == 'Y' or ans == '':
                return 'ks', encryp
            elif ans == 'N':
                return 'ms', encryp
            else:
                input('\n\tOption not found')
                return 'fs', encryp

    elif answer == 'D':
        if encryp.key_code:
            print(f'\n\t{encryp}')
            print('\n\tDecrypting message')
            encryp.decipher_message()
            input(f'\n\t{encryp}')
            return 'ms', encryp
        else:
            print('\n\tThere are currently no keys')
            ans = str(input('\n\tDo you input keys?[Y]/N ')).upper()
            if ans == 'Y' or ans == '':
                return 'ks', encryp
            elif ans == 'N':
                return 'ms', encryp
            else:
                input('\tOption not found')
                return 'fs', encryp

    elif answer == 'V':
        print('\n\tThis is the current message:')
        input(f'\n\t{encryp}')
        return 'ms', encryp

    elif answer == 'R':
        return 'fs', encryp

    else:
        input('\n\tOption not found, try again!')
        return 'ms', encryp


@clear_screen
def key_screen(encryp: Encryption):
    if encryp.key_code:
        there_is_key_code = '(There are keys)'
    else:
        there_is_key_code = '(There are not keys)'
    print('\n\t\t::: [K]ey_code :::')
    print(f'''
\t[G]enerate keys     
\t[I]nput keys
\t[V]iew keys   \t{there_is_key_code}
\tRe[s]et
\t[R]eturn''')
    answer = str(input('\n\tWhich option do you choose? ')).upper()
    if answer == 'G':
        print('\n\t... generating keys')
        key_code = KeyCode()
        key_code()
        encryp.key_code = key_code
        print('\n\tThe values  of k1, k2 and k3 are\n')
        print(str(encryp.key_code).replace('k', '\tk'))
        input('\n\tCopy the values to a safe place.')
        return 'ks', encryp

    elif answer == 'I':
        print('\n\tEnter the values of k1, k2 and k3')
        try:
            sure = False
            while not sure:
                k1 = int(input('\n\tk1:? '))
                k2 = int(input('\tk2:? '))
                k3 = int(input('\tk3:? '))
                print(
                    f'\n\tYour code keys:\n\n\tk1: {k1}\n\tk2: {k2}\n\tk3: {k3}')
                ans = str(input('\n\tAre you sure?[Y] ')).upper()
                if ans == 'Y' or ans == '':
                    sure = True
                else:
                    input('\n\tEnter the values of k1, k2 and k3')
            encryp.key_code = KeyCode(k1, k2, k3)
            input('\n\tKeyCode is load')
        except ValueError:
            input('\tValue entered is wrong')
            return 'ks', encryp
        return 'ks', encryp

    elif answer == 'V':
        if encryp.key_code:
            print('\n\tThe keys are currently:\n')
            print(str(encryp.key_code).replace('k', '\tk'))
            print(' ')
            time_sleep(5)
            return 'ks', encryp
        else:
            input('\n\tThere are currently no keys')
            return 'ks', encryp

    elif answer == 'S':
        encryp.key_code = None
        return 'ks', encryp

    elif answer == 'R':
        return 'fs', encryp

    else:
        input('\n\tOption not found, try again!')
        return 'ks', encryp


@clear_screen
def main_screen(encryp: Encryption) -> str:
    if encryp.key_code:
        there_is_key_code = '(There are keys)'
    else:
        there_is_key_code = '(There are not keys)'
    convert_answer = {'K': 'ks', 'M': 'ms', 'E': 'exit'}
    print(f'''\n\t\t::: MAIN SCREEN :::
          
\tThe options are:

\t[K]ey Code    \t{there_is_key_code}
\t[M]essage           
\t[E]xit''')
    try:
        answer = str(input('\n\tWhich option do you choose? ')).upper()
        answer = convert_answer[answer]
    except KeyError:
        input('\n\tOption not found, try again.')
        return 'fs', encryp
    return answer, encryp


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
    ex.next = {'exit': ex}

    main_graphs = Graph(fs)

    while True:

        main_graphs.run()


if __name__ == '__main__':
    try:
        print('\n\tGreetings! ')
        main()

    except KeyboardInterrupt:
        os.system('cls')
        input('\n\n\t\tWhat happened!?')
        os.system('cls')
        quit()
