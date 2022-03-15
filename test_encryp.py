# -*- coding: utf-8 -*-

KEYS1 = {'ẍ': '83', ']': '73', ':': '17', 'S': '33', 's': '12', 'd': '57', 
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

KEYS2 = {'83': 'ẍ', '73': ']', '17': ':', '33': 'S', '12': 's', '57': 'd',
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
text = 'Otra prueba de una tantas'


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
lis_dig = [text_dig[max_len * idx: max_len * (idx + 1)] for idx in range(rang)]


# Completamos el grupo
while len(lis_dig[-1]) < max_len:
    lis_dig[-1] += '83'

# De dig a int    
lis_int = [int(dig) for dig in lis_dig]

# Para calcular la torre de potencias de un número
def power_tower(num, mod, max_power):
    pow_tow = [num % mod]
    for _ in range(1, max_power):
        power = pow_tow[0] ** 2 % mod
        pow_tow.insert(0, power)
    return pow_tow

# Para calcular (num**exp) %mod
def power_mod(num, exp, mod):
    
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


# Los enteros en la lista son modificados por la operación (num**exp) %mod
# (Aquí es cuando se encripta el mensake)
lis_int_c = [power_mod(num, k2, k1) for num in lis_int]

lis_dig_c = []

# De enteros se pasan a dígitos a la vez que se le agrega un cero para 
# lograr una longotud equivalente a la del mod
for num in lis_int_c:
    dig = str(num)
    while len(dig) < max_len + 2:
        dig = '0' + dig
    lis_dig_c.append(dig)

# Se unen los dígitos en una sola línea
text_dig_c = ''.join(lis_dig_c)

# Se dig se pasan a caracteres
text_c = ''.join([KEYS2[text_dig_c[2*idx:2*(idx + 1)]]\
                  for idx in range(len(text_dig_c) // 2) ])
    
    
# =============================================================================
# AHORA A DECIFRAR EL MSJE
# =============================================================================












