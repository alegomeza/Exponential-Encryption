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

k1=62569581079531
k2=35152792042126009
k3=29983486957339

max_len = len(str(k1))

text = 'Texto re equis de pruebaaaaaaaa jejeje re cosas escriras al azar jaja!'
text2 = 'ñ{Júo*0íóéEr]é]!NMN4Mb@¿<kúz$"F-oARYaEJ7d9m+%cíé3t~<p}adQñMM!Eñ|;&:[uOc!ñZ-,e'

def open_text_in(text:str, ran:int, dict_in:dict) -> int :
    l = len(text)
    num = 0
    for i in range(l):
        num += dict_in[text[i]] * ran**(int(i))
    return num

num = open_text_in(text, ran, dict_in)
num2 = open_text_in(text2, ran, dict_in)

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

int_lis = int_to_lis_int(num , max_len - 1)
int_lis2 = int_to_lis_int(num2 , max_len )

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

c_int_lis = exponential_cipher_lis(int_lis, k2, k1)
c_int_lis2 = exponential_cipher_lis(int_lis2, k3, k1)


def lis_int_to_int(int_lis:list, max_len:int) -> int:
    dig_lis = []
    for num in int_lis:
        dig = str(num)
        while len(dig) < max_len:
            dig = '0' + dig
        dig_lis.append(dig)
    dig = ''.join(dig_lis)
    return int(dig)

c_num = lis_int_to_int(c_int_lis, max_len)
c_num2 = lis_int_to_int(c_int_lis2, max_len - 1)

def open_text_out(num:int, ran:int, dict_out:dict) -> str :
    text = ''
    r , div = 1 , 1
    while div != 0:
        div = num // ran
        r = num % ran
        num = div
        text += dict_out[r]
    return text

c_text = open_text_out(c_num, ran, dict_out)
c_text2 = open_text_out(c_num2, ran, dict_out)
