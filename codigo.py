# -*- coding: utf-8 -*-

import random
import math

#Se le asigna un valor entero a los caracteres que deseamos codificar

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
        'á': '27', '&': '15', '\n': '55', '8': '00', 'K': '21', '{': '69',
        '~': '48', 'C': '87', 'm': '22', 'h': '05', 'u': '11', 't': '31',
        '"': '90', '$': '50', '>': '97', '<': '96', '!': '86', '.': '95',
        '6': '17'}

KEYS2 = {'a': '00', 'b': '01', 'c': '02', 'd': '03', 'e': '04', 'f': '05',
         'g': '06', 'h': '07', 'i': '08', 'j': '09', 'k': '10', 'l': '11',
         'm': '12', 'n': '13', 'o': '14', 'p': '15', 'q': '16', 'r': '17',
         's': '18', 't': '19', 'u': '20', 'v': '21', 'w': '22', 'x': '23',
         'y': '24', 'z': '25', 'A': '26', 'B': '27', 'C': '28', 'D': '29',
         'E': '30', 'F': '31', 'G': '32', 'H': '33', 'I': '34', 'J': '35',
         'K': '36', 'L': '37', 'M': '38', 'N': '39', 'O': '40', 'P': '41',
         'Q': '42', 'R': '43', 'S': '44', 'T': '45', 'U': '46', 'V': '47',
         'W': '48', 'X': '49', 'Y': '50', 'Z': '51', '0': '52', '1': '53',
         '2': '54', '3': '55', '4': '56', '5': '57', '6': '58', '7': '59',
         '8': '60', '9': '61', '.': '62', ',': '63', '?': '64', '!': '65',
         ' ': '66', '\n': '67' }

'''
Clase encargada de generar una clave de acuerdo a los parametros 
iniciales, los cuales le daran la complejidad a la clave
'''
class Clave:
    def __init__(self):
        #Valores iniciales que determinan la complejidad de la clave
        self.p = self._primo_long_impar(40)
        self.e = self._primo_relativo(30)
        self.d = self._modulo_inverso(self.e)

    def _algoritmo_de_Euclides(self, a, b):
        #input: a=Número entero , b=Número entero
        #output: mcd entre a y b  , 1 = a*u0 + b*v0
        if b == 0:
            return 0,1,0
        u0 = 1
        u1 = 0
        v0 = 0
        v1 = 1
        while b != 0:
            q = a//b
            r = a - b * q
            u = u0 - q * u1
            v = v0 - q * v1
            #Update a,b
            a = b
            b = r
            #Update for next iteration
            u0 = u1
            u1 = u
            v0 = v1
            v1 = v
        return  a, u0, v0

    def _modulo_inverso(self, num):
        #Hallamos el inverso mod(self.p-1) del parametro
        mod = self.p - 1
        mcd,u,v = self._algoritmo_de_Euclides(mod,num)
        if mcd != 1:
            print('No existe inverso')
            return 0
        return v % mod

    def _primo_relativo(self, bits):
        #Hallamos un primo relativo con respecto a self.p -1, de acuerdo al parametro
        busqueda = True
        while busqueda:
            e = random.getrandbits(bits)
            phi_p = self.p - 1
            mcd, u, v = self._algoritmo_de_Euclides(phi_p, e)
            if mcd == 1:
                busqueda = False
                return e

    def _primo_long_impar(self,bits):
        #Generamos un número primo de acuerdo al parametro, 
        #con una cantidad impar de digitos
        p = 'UD'
        while len(str(p)) % 2 == 0:
            p = self._generar_primo(bits)
        return p

    def _generar_primo(self,bits):
        #Generamos un número primo de acuerdo al parametro
        busqueda = True
        while busqueda:
            es_primo = True
            p = random.getrandbits(bits)
            for i in range(2, int(math.sqrt(p)) + 1):
                if p % i == 0:
                    es_primo = False
                    break
            if es_primo:
                return p

'''
Esta clase e encarga de almacenar el texto y las funciones necesarias 
para cifrar o decifrar el texto almacenado, en base a KEYS2
'''     
class Mensaje:
    #Valores iniciales, los cuales constan de un texto y de un entero p
    def __init__(self,texto,p):
        self.texto = texto
        self.p = p

    def cifrar_mensaje(self,e):
        #Recibe el parametro e, con esto se prodece a pasar la cadena de caracteres a una cadena de enteros
        #y son codificados por el parametro e
        lista_enteros = self._str_a_int()
        enteros = [int(num) for num in lista_enteros if True]
        enteros_cifrados = [self._calcular_Pe_mod_p(num, e, self.p) for num in enteros if True]
        lista_enteros_cifrados = [str(num) for num in enteros_cifrados if True]
        texto_cifrado = ''
        for idx in range(len(lista_enteros_cifrados)):
            while len(lista_enteros_cifrados[idx]) < len(str(self.p)):
                lista_enteros_cifrados[idx] = '0' + lista_enteros_cifrados[idx]
            texto_cifrado += lista_enteros_cifrados[idx]
        return texto_cifrado

    def _calcular_Pe_mod_p(self, P, e, p):
        #calculo de torres de potencia en base a los parametros
        bin_e = list(bin(e))
        bin_e = bin_e[2:]
        bin_e = [int(num) for num in bin_e if True]
        potencias_P = []
        for n in range(0, len(bin_e)):
            if n == 0:
                C = P % p
                potencias_P.insert(0,C)
            else:
                C = potencias_P[0]**2 % p
                potencias_P.insert(0,C)
        resultado = 1
        for i in range(len(bin_e)):
            if bin_e[i] == 1:
                resultado *= potencias_P[i]
                resultado = resultado % p
        return resultado

    def decifrar_texto(self, d):
        #Se encarga de descifrar self.texto a partir del parametro d
        longitud = len(str(self.p))
        lista_enteros_cifrados = []
        grupo = ''
        for id in range(1,len(self.texto)):
            if len(grupo) < longitud :
                grupo += self.texto[id - 1]
            else:
                lista_enteros_cifrados.append(grupo)
                grupo = self.texto[id - 1]
        grupo += self.texto[-1]
        lista_enteros_cifrados.append(grupo)
        try:
            enteros_cifrados = [int(num) for num in lista_enteros_cifrados if True]
        except ValueError:
            print('Valores ingresados no son correctos!')
            run()
        enteros = [self._calcular_Pe_mod_p(num, d, self.p) for num in enteros_cifrados if True]
        lista_enteros = [str(num) for num in enteros if True]
        texto_decifrado = ''
        for idx in range(len(lista_enteros)):
            while len(lista_enteros[idx]) < longitud - 1:
                lista_enteros[idx] = '0' + lista_enteros[idx]
            texto_decifrado += lista_enteros[idx]
        texto_final = self._int_a_str(texto_decifrado)
        return texto_final

    def _str_a_int(self):
        #Cambia self.texto a cadena de enteros
        longitud = len(str(self.p))  # 21
        max = (longitud - 1)//2      # 10
        lista_chr = list(self.texto)
        lista_enteros = []
        cuenta = 0
        grupo = '49'
        for idx in range(len(lista_chr)):
            cuenta += 1
            if cuenta % max == 0:
                lista_enteros.append(grupo)
                grupo = KEYS[lista_chr[idx]]
            else:
                grupo += KEYS[lista_chr[idx]]
        lista_enteros.append(grupo)
        while len(lista_enteros[-1]) < 2 * max:
            lista_enteros[-1] += '49'
        return lista_enteros

    def _int_a_str(self, texto_decifrado):
        #Apartir de una cadena de enteros, retorna una cadena de caracteres
        longitud = len(texto_decifrado)//2
        texto_final = ''
        letras_num = [texto_decifrado[i*2 : (i + 1)*2] for i in range(longitud) if True]
        for num in letras_num:
            for k , v in KEYS.items():
                if v == num:
                    texto_final += k
        return texto_final
