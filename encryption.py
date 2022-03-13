from keycode import KeyCode

KEYS = {'#': '35', 'Q': '61', '0': '66', ' ': '88', 'W': '81', 'k': '46',
        '=': '75', 'E': '80', '+': '74', 'd': '20', '1': '43', 'z': '71',
        'F': '94', ';': '10', 'I': '47', 'U': '16', 'M': '09', 'e': '26',
        'n': '92', 'T': '56', 'B': '13', '7': '82', ')': '01', '4': '93',
        'Ñ': '76', 'Z': '07', 'i': '44', 'y': '14', 'P': '68', '/': '79',
        'o': '62', 'S': '58', '3': '34', '2': '30', 'p': '52', 'ú': '03',
        '¿': '70', 'ñ': '63', 'j': '73', 'L': '78', 'G': '04', 'a': '18',
        'q': '89', 'Y': '85', '*': '54', 'R': '60', 's': '67', "'": '65',
        'x': '83', 'N': '02', 'X': '32', 'ó': '49', 'V': '37', ']': '45',
        'r': '84', 'D': '53', 'v': '28', 'f': '06', '(': '29', 'J': '91',
        ':': '77', 'H': '19', '[': '33', 'l': '24', 'í': '59', '}': '41',
        'A': '64', '-': '72', 'O': '42', 'w': '36', '9': '40', 'g': '08',
        'b': '57', 'é': '23', '¡': '51', '?': '25', 'c': '38', '5': '12',
        'á': '27', '&': '15', 'ẍ': '55', '8': '00', 'K': '21', '{': '69',
        '~': '48', 'C': '87', 'm': '22', 'h': '05', 'u': '11', 't': '31',
        '"': '90', '$': '50', '>': '97', '<': '96', '!': '86', '.': '95',
        '6': '17', ',': '98'}


class Encryption:
    
    def __init__(self, key_code : KeyCode = None, message : str = None) -> None:
        if message is None:
            self.message = '~'
        else:
            self.message = str(message)
        self.key_code = key_code
        
    def __str__(self) -> str:
        return self.message
    
    def _dig_to_str(self, text:str) -> str:
        lenght = len(text) // 2
        text_aux = ''
        dig = [text[index * 2: (index + 1) * 2]
                       for index in range(lenght)]
        for num in dig:
            for keys, values in KEYS.items():
                if values == num:
                    text_aux += keys
        return text_aux
    
    def _str_to_dig(self, text:str) -> str:
        text_aux = ''
        for chr in text:
            text_aux += KEYS[chr]
        return text_aux
    
    def _group_dig(self, text:str) -> list:
        lenght = len(str(self.key_code._k1))
        max_len = (lenght - 1) // 2
        rang = (len(text) // max_len) +1
        dig_lis = [text[max_len * idx: max_len * (idx + 1)] for idx in range(rang)]
        while len(dig_lis[-1]) < max_len:
            dig_lis[-1] += '55'
        return dig_lis
    
    def _dis_to_int(self, dig_lis:list) -> list:
        int_lis = [int(dig) for dig in dig_lis]
        return int_lis
    
    
        
                
    

    def _str_to_int(self) -> str:
        # Takes a string of characters and 
        # transforms them into a list of integers
        lenght = len(str(self.key_code._k1))
        max_lenght = (lenght - 1) // 2
        character_list = self.message
        integer_list = []
        count = 0
        group = '55'
        for index in range(len(character_list)):
            count += 1
            if count % max_lenght == 0:
                integer_list.append(group)
                group = KEYS[character_list[index]]
            else:
                group += KEYS[character_list[index]]
        integer_list.append(group)
        while len(integer_list[-1]) < 2 * max_lenght:
            integer_list[-1] += '55'
        input(f'{integer_list}')
        return integer_list

    def _int_to_str(self) -> str:
        # Takes a list of integers and 
        # transforms them into a string
        lenght = len(self.message) // 2
        text = ''
        letters_num = [self.message[index * 2: (index + 1) * 2]
                       for index in range(lenght)]
        for num in letters_num:
            for keys, values in KEYS.items():
                if values == num:
                    text += keys
        return text#.replace('ẍ','')

    def _powers_towers(self, p: int, e: int) -> int:
        # Function that calculates a tower of powers
        # to facilitate calculations.
        bin_e = list(bin(e))
        bin_e = bin_e[2:]
        bin_e = [int(num) for num in bin_e]
        powers = []
        for index in range(0, len(bin_e)):
            if index == 0:
                c = p % self.key_code._k1
                powers.insert(0, c)
            else:
                c = powers[0] ** 2 % self.key_code._k1
                powers.insert(0, c)
        result = 1
        for index in range(len(bin_e)):
            if bin_e[index] == 1:
                result *= powers[index]
                result = result % self.key_code._k1
        return result

    def _encrypt_message(self) -> str:
        # modular power calculation is applied
        integer_list = self._str_to_int()
        integers = [int(num) for num in integer_list]
        encrypted_integers = [self._powers_towers(num, self.key_code._k2)
                              for num in integers]
        encrypted_integers_list = [str(num) for num in encrypted_integers]
        ciphertext = ''
        for index in range(len(encrypted_integers_list)):
            while len(encrypted_integers_list[index]) < len(str(self.key_code._k1)):
                encrypted_integers_list[index] = '0' + encrypted_integers_list[index]
            ciphertext += encrypted_integers_list[index]
        return ciphertext

    def _decipher_message(self):
        length = len(str(self.key_code._k1))
        encrypted_integers_list = []
        group = ''
        for index in range(1, len(self.message)):
            if len(group) < length:
                group += self.message[index - 1]
            else:
                encrypted_integers_list.append(group)
                group = self.message[index - 1]
        group += self.message[-1]
        encrypted_integers_list.append(group)
        encrypted_integer = [int(num) for num in encrypted_integers_list]
        integers = [self._powers_towers(num, self.key_code._k3)\
                    for num in encrypted_integer]
        integers_list = [str(num) for num in integers]
        decrypted_text = ''
        for index in range(len(integers_list)):
            while len(integers_list[index]) < length - 1:
                integers_list[index] = '0' + integers_list[index]
            decrypted_text += integers_list[index]
        return decrypted_text

    def encrypt_message(self):
        if not self.key_code:
            print('Missing data in KeyCode')
        else:
            self.message = self._encrypt_message()
            input(f'{self.message}')
            # self.message = self._int_to_str() # Recent!

    def decipher_message(self):
        if not self.key_code:
            print('Missing data in KeyCode')
        else:
            # self.message = self._str_to_int() ## Recent!
            input(f'{self.message}')
            self.message = self._decipher_message()
            self.message = self._int_to_str()
