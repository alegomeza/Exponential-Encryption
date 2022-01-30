from encryption import Encryption
from message import Message
from key_code import Key_code

def run():
    clave = Key_code()
    clave.generate_key()

    print('Ya generamos la clave')

    mensaje = Message(text='Esto en un mensaje de prueba')

    encriptacion = Encryption(message=mensaje, key_code=clave)

    print('Vamos a aplicar la función')

    text = encriptacion.a__encrypt_message()
    print(text)


if __name__ == '__main__':
    run()