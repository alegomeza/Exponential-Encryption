# -*- coding: utf-8 -*-

KEYS1 = {'ü': '83', ']': '73', ':': '17', 'S': '33', 's': '12', 'd': '57', 
         'L': '65', 'f': '01', '.': '67', 'ñ': '89', 'Y': '68', ',': '31',
         '_': '14', 'ó': '32', '>': '07', 'Q': '41', 'l': '56', 'n': '90',
         '6': '78', 'x': '71', 'U': '28', 'ú': '37', 'w': '44', ' ': '10',
         '{': '58', 'D': '70', '(': '51', 'h': '86', 'E': '34', '!': '09',
         '4': '22', 'X': '98', '¿': '26', 'F': '29', '@': '93', '-': '97',
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
         '22': '4', '98': 'X', '26': '¿', '29': 'F', '93': '@', '97': '-',
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

# =============================================================================
# k1=1054008758443
# k2=352957235
# k3=16787875721
# =============================================================================
k1=140364644941
k2=775080661
k3=75355938421


# Mensaje inicial
text = 'Meseajoo dea proobia'


# Tranformamos a digitos
text_dig = ''
for char in text:
    text_dig += KEYS1[char]


# Generamos grupos de digitos de acuerdo a
# la longitud de k1    
max_len = len(str(k1)) - 2
if len(text_dig) % max_len == 0:
    rang = len(text_dig) // max_len
else:
    rang = (len(text_dig) // max_len) + 1
dig_lis = [text_dig[max_len * idx: max_len * (idx + 1)] for idx in range(rang)]
# Completamos el grupo
while len(dig_lis[-1]) < max_len:
    dig_lis[-1] += '55'
    
int_lis = [int(dig) for dig in dig_lis]


# Torre de potencias

# Calculamos el número binario de la potencia
bin_k2 = str(bin(k2))
bin_k2 = bin_k2[2:]


# #2**0 = 1
# powers = [int_lis[0] % k1]
# # Resto de potencias
# for _ in range(len(bin_k2) - 1):
#     power = powers[0] ** 2 % k1
#     print(power)
#     powers.insert(0, power)

# Para calcular la torre de potencias de un número
def power_tower(num, mod, max_power):
    pow_tow = [num % mod]
    for _ in range(1, max_power):
        power = pow_tow[0] ** 2 % mod
        pow_tow.insert(0, power)
    return pow_tow

ci_mess = ''

for index in range(len(int_lis)):
    # Calculamos la torre de potencia para cada int en int_lis    
    powers = power_tower(int_lis[index], k1, len(bin_k2))
    
    # Calculamos num ** k2 con ayuda de la torre de potencias 
    # y la expresión en bin del exponente
    result = 1
    for idx in range(1 ,len(bin_k2)):
        if bin_k2[idx] == '1':
            result *= powers[idx]
            result = result % k1
    
    # int a str
    result = str(result)
    cip = result
    
    
    # Completamos la longitud del str a la de k1 (mod) con ceros al inicio 
    # para que no altere el valor implicito del int
    while len(cip) < max_len + 2:
        cip = '0' + cip
    # Concatenamos para entregar un una sola línea de dígitos
    ci_mess += cip

text_cip = ''
lenght = len(ci_mess) // 2

# Agrupamos los dígitos en pares (dos números) para dig -> chr
ci_mess_idx = [ci_mess[2*idx:2*(idx+1)] for idx in range(lenght)]

# De dígitos a caracteres
for idx in ci_mess_idx:
    text_cip += KEYS2[idx]

    
# =============================================================================
# AHORA A DECIFRAR EL MSJE
# =============================================================================

text_dig_2 = ''
for char in text_cip:
    text_dig_2 += KEYS1[char]
    
max_len_2 = len(str(k1))
rang_2 = len(text_dig_2) // max_len_2

dig_lis_2 = [text_dig_2[max_len_2 * idx: max_len_2 * (idx + 1)]\
             for idx in range(rang_2)]
    











