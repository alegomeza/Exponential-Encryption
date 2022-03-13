from keycode import KeyCode

KEYS1 = {'ü': '83', ']': '73', ':': '17', 'S': '33', 's': '12', 'd': '57', 
         'L': '65', 'f': '01', '.': '67', 'ñ': '89', 'Y': '68', ',': '31',
         '_': '14', 'ó': '32', '>': '07', 'Q': '41', 'l': '56', 'n': '90',
         '6': '78', 'x': '71', 'U': '28', 'ú': '37', 'w': '44', ' ': '10',
         '{': '58', 'D': '70', '(': '51', 'h': '86', 'E': '34', '!': '09',
         '4': '22', 'X': '98', '¿': '26', 'F': '29', '°': '93', '-': '97',
         '*': '99', '8': '18', 'Ñ': '19', '$': '79', '?': '60', 'N': '45',
         'k': '35', 'b': '21', '[': '47', 'j': '04', 'é': '59', 'K': '36',
         'J': '42', '5': '74', 'u': '85', 'G': '63', 'i': '24', '}': '88',
         '/': '52', 'y': '96', ')': '55', 'v': '77', 'Z': '02', 'W': '54',
         '2': '50', 'B': '46', '¡': '39', 'á': '87', 'O': '43', 'm': '15',
         '3': '48', '%': '16', '<': '06', '1': '66', 'T': '92', 'z': '49',
         '"': '38', '~': '75', 'M': '72', '#': '20', 'C': '82', '0': '30',
         'q': '84', 'í': '27', '+': '95', 'V': '69', 'o': '40', '9': '61',
         '=': '13', 'a': '80', 'R': '11', ';': '08', 'I': '25', '&': '81',
         'A': '62', 'g': '53', '7': '64', 'H': '03', 'e': '94', 'c': '00',
         'r': '76', 'P': '23', 't': '05', 'p': '91'}

KEYS2 = {'83': 'ü', '73': ']', '17': ':', '33': 'S', '12': 's', '57': 'd',
         '65': 'L', '01': 'f', '67': '.', '89': 'ñ', '68': 'Y', '31': ',',
         '14': '_', '32': 'ó', '07': '>', '41': 'Q', '56': 'l', '90': 'n',
         '78': '6', '71': 'x', '28': 'U', '37': 'ú', '44': 'w', '10': ' ',
         '58': '{', '70': 'D', '51': '(', '86': 'h', '34': 'E', '09': '!',
         '22': '4', '98': 'X', '26': '¿', '29': 'F', '93': '°', '97': '-',
         '99': '*', '18': '8', '19': 'Ñ', '79': '$', '60': '?', '45': 'N',
         '35': 'k', '21': 'b', '47': '[', '04': 'j', '59': 'é', '36': 'K',
         '42': 'J', '74': '5', '85': 'u', '63': 'G', '24': 'i', '88': '}',
         '52': '/', '96': 'y', '55': ')', '77': 'v', '02': 'Z', '54': 'W',
         '50': '2', '46': 'B', '39': '¡', '87': 'á', '43': 'O', '15': 'm',
         '48': '3', '16': '%', '06': '<', '66': '1', '92': 'T', '49': 'z',
         '38': '"', '75': '~', '72': 'M', '20': '#', '82': 'C', '30': '0',
         '84': 'q', '27': 'í', '95': '+', '69': 'V', '40': 'o', '61': '9',
         '13': '=', '80': 'a', '11': 'R', '08': ';', '25': 'I', '81': '&',
         '62': 'A', '53': 'g', '64': '7', '03': 'H', '94': 'e', '00': 'c',
         '76': 'r', '23': 'P', '05': 't', '91': 'p'}


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


def chr_to_dig(text:str) -> str:
    text_aux = ''
    for chr in text:
        text_aux += KEYS[chr]
    return text_aux
    
def group_dig(text:str, max_len:int) -> list:
    if len(text) % max_len == 0:
        rang = len(text) // max_len
    else:
        rang = (len(text) // max_len) + 1
    dig_lis = [text[max_len * idx: max_len * (idx + 1)] for idx in range(rang)]
    while len(dig_lis[-1]) < max_len:
        dig_lis[-1] += '75'
    return dig_lis
    
def dig_to_int(dig_lis:list) -> list:
    int_lis = [int(dig) for dig in dig_lis]
    return int_lis

def power_tower(P, mod, ran):
    powers = [P % mod]
    for _ in range(1, ran):
        power = powers[0] ** 2 % mod
        powers.insert(0, power)
    return powers



class Encryption:
    
    def __init__(self, key_code : KeyCode = None, message : str = None) -> None:
        if message is None:
            self.message = '~'
        else:
            self.message = str(message)
        self.key_code = key_code
        
    def __str__(self) -> str:
        return self.message
    
    def _dig_to_chr(self, text:str) -> str:
        lenght = len(text) // 2
        text_aux = ''
        dig = [text[index * 2: (index + 1) * 2] for index in range(lenght)]
        for num in dig:
            for keys, values in KEYS.items():
                if values == num:
                    text_aux += keys
        return text_aux
    
    
    
    
        
                
    

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
