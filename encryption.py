from key_code import Key_code
from message import Message

class Encryption:
    message = Message('')
    key_code = Key_code()
    
    def __init__(self, message, key_code) -> None:
        self.message = message
        self.key_code = key_code

    def encrypt_message():
        pass

    def decipher_message():
        pass

    def __str_to_int(self):
        lenght = len(str(self.key_code.p))
        max = (lenght - 1)//2
        character_list = self.message.text
        integer_list = []
        count = 0
        group = '49'
        for index in range(len(character_list)):
            count += 1
            
