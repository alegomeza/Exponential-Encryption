from keycode import KeyCode

Kc = 'ẍ\
abcdefghijklmnñopqrstuvwxyz\
ABCDEFGHIJKLMNÑOPQRSTUVWXYZ\
0123456789áéíóú (),.!?;:"\
|¿¡°#$%&/=+-*-_@~\
[]{}<>'

ran = len(Kc)

dict_in = {Kc[idx]:int(idx) for idx in range(ran)}

dict_out = {int(idx):Kc[idx] for idx in range(ran)}

def open_text_in(text:str, ran:int, dict_in:dict) -> int :
    l = len(text)
    num = 0
    for i in range(l):
        num += dict_in[text[i]] * ran**(int(i))
    return num


def int_to_lis_int(num:int, max_len:int) -> list:
    dig = str(num)
    rang = ((len(dig) - 1) // max_len) + 1
    res = len(dig) % max_len
    if res == 0:
        dig_lis = [dig[max_len*idx:max_len*(idx + 1)] for idx in range(rang)]
    else:
        dig_lis = [dig[:res]] + [dig[res + max_len*idx:res + max_len*(idx + 1)] \
                               for idx in range(rang - 1)]
    input(f'{dig_lis}')
    return [int(dig) for dig in dig_lis]

# =============================================================================
# def exponential_cipher_lis(int_lis:list, exp:int, mod:int) -> list:
#     return [power_mod(num, exp, mod) for num in int_lis]
# =============================================================================

def lis_int_to_int(int_lis:list, max_len:int) -> int:
    dig_lis = []
    for num in int_lis:
        dig = str(num)
        while len(dig) < max_len:
            dig = '0' + dig
        dig_lis.append(dig)
    dig = ''.join(dig_lis)
    return int(dig)
    

def open_text_out(num:int, ran:int, dict_out:dict) -> str :
    text = ''
    r , div = 1 , 1
    while div != 0:
        div = num // ran
        r = num % ran
        num = div
        text += dict_out[r]
    return text




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


def tex_to_dig(text:str, KEYS:dict) -> str:
    dig_text = ''
    for chr in text:
        try:
            dig_text += KEYS[chr]
        except KeyError:
            dig_text += KEYS['?']
    return dig_text

    
def dig_group(dig_text:str, max_len:int) -> list:
    if len(dig_text) % max_len == 0:
        rang = len(dig_text) // max_len
    else:
        rang = (len(dig_text) // max_len) + 1
        
    dig_lis = [dig_text[max_len * idx: max_len * (idx + 1)] for idx in range(rang)]
    
    while len(dig_lis[-1]) < max_len:
        dig_lis[-1] += '83'
    return dig_lis

    
def diglis_to_intlis(dig_lis:list) -> list:
    return [int(dig) for dig in dig_lis]


def power_tower(num:int, mod:int, max_power:int) -> list:
    pow_tow = [num % mod]
    for _ in range(1, max_power):
        power = pow_tow[0] ** 2 % mod
        pow_tow.insert(0, power)
    return pow_tow


def power_mod(num:int, exp:int, mod:int) -> int:
    
    bin_exp = bin(exp)
    bin_exp = bin_exp[2:]
    max_power = len(bin_exp)
    
    pow_tow = power_tower(num, mod, max_power)
    
    result = 1
    for idx in range(max_power):
        if bin_exp[idx] == '1':
            result *= pow_tow[idx]
            result %= mod
    return result


def exponential_cipher_lis(int_lis:list, exp:int, mod:int) -> list:
    return [power_mod(num, exp, mod) for num in int_lis]


def intlis_to_diglis(int_lis:list, max_len:int) -> list:
    dig_lis = []
    for num in int_lis:
        dig = str(num)
        while len(dig) < max_len:
            dig = '0' + dig
        dig_lis.append(dig)
    return dig_lis


def diglis_to_tex(dig_lis:list, KEYS:dict):
    dig_text = ''.join(dig_lis)
    return ''.join([KEYS2[dig_text[2*idx:2*(idx + 1)]]\
                  for idx in range(len(dig_text) // 2) ])



class Encryption:
    
    def __init__(self, key_code : KeyCode = None, message : str = None) -> None:
        if message is None:
            self.message = '~'
        else:
            self.message = str(message)
        self.key_code = key_code
        
    def __str__(self) -> str:
        return self.message
    
    def encrypt_message(self):
        
        if not self.key_code:
            pass
        else:
            try:
                mod = self.key_code._k1
                exp = self.key_code._k2
                max_len = len(str(mod)) - 2
                dig_tex = tex_to_dig(self.message, KEYS1)
                dig_lis = dig_group(dig_tex, max_len)
                int_lis = diglis_to_intlis(dig_lis)
                c_int_lis = exponential_cipher_lis(int_lis, exp, mod)
                c_dig_lis = intlis_to_diglis(c_int_lis, max_len + 2)
                self.message = diglis_to_tex(c_dig_lis, KEYS2)
            except:
                input('\n\tSomething is wrong!\n')
        
        

    def decipher_message(self):
        if not self.key_code:
            pass
        else:
            try:
                mod = self.key_code._k1
                exp = self.key_code._k3
                max_len = len(str(mod))
                c_dig_tex = tex_to_dig(self.message, KEYS1)
                c_dig_lis = dig_group(c_dig_tex, max_len)
                c_int_lis = diglis_to_intlis(c_dig_lis)
                int_lis = exponential_cipher_lis(c_int_lis, exp, mod)
                dig_lis = intlis_to_diglis(int_lis, max_len - 2)
                text = diglis_to_tex(dig_lis, KEYS2)
                self.message = text.replace('ü','')
            except:
                input('\n\tSomething is wrong!\n')
            
            
def run():
            
    k = KeyCode(12,33,45)
    k = KeyCode()
    k()
    # input(k)
    enc = Encryption(k, 'Message forẍtest this!!')
    
    enc.encrypt_message()
    input('1')
    print(enc)
    enc.decipher_message()
    input('2')
    print(enc)


if __name__ == '__main__':
    run()

