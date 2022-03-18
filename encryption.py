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
        try:
            num += dict_in[text[i]] * ran**(int(i))
        except KeyError:
            num += dict_in['?'] * ran**(int(i))
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
                max_len = len(str(mod))
                num = open_text_in(self.message, ran, dict_in)
                int_lis = int_to_lis_int(num , max_len - 1)
                c_int_lis = exponential_cipher_lis(int_lis, exp, mod)
                c_num = lis_int_to_int(c_int_lis, max_len)
                self.message = open_text_out(c_num, ran, dict_out)
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
                num = open_text_in(self.message, ran, dict_in)
                int_lis = int_to_lis_int(num , max_len)
                c_int_lis = exponential_cipher_lis(int_lis, exp, mod)
                c_num = lis_int_to_int(c_int_lis, max_len - 1)
                self.message = open_text_out(c_num, ran, dict_out)
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

