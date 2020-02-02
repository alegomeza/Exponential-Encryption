# -*- coding: utf-8 -*-

from codigo import KEYS, Clave, Mensaje

def run():
    #imprimimos pantalla principal y esperamos valor,
    #para proceder a una proxima pantalla
    valor = pantalla_principal()
    if valor == 'G':
        print('::: [G]enerando Clave ... ::: ')
        generar_clave_exponencial()
    elif valor == 'C':
        print('::: [C]ifrar Mensaje :::')
        print()
        try:
            p = int(input('Ingrese p: '))
            e = int(input('Ingrese e: '))
        except ValueError:
            print('Valores ingresados no son correctos!')
            run()
        menu_cifrar_mensaje(p,e)
    elif valor == 'D':
        print('::: [D]ecifrar Mensaje :::')
        print()
        try:
            p = int(input('Ingrese p: '))
            d = int(input('Ingrese d: '))
        except ValueError:
            print('Valores ingresados no son correctos!')
            run()
        menu_decifrar_mensaje(p,d)
    elif valor == 'S':
        print('::: [S] A L I R :::')
        print()
        quit()
    else:
        print('Comando no encontrado, intente de nuevo')
        print()
        run()

def pantalla_principal():
    #Pantalla principal
    print('''
    ¡Saludos! Las opciones disponibles son:

    [G]enerar clave
    [C]ifrar mensaje
    [D]ecifrar mensaje
    [S]salir
        ''')
    valor = str(input('¿Que desea realizar?: ')).upper()
    return valor

def generar_clave_exponencial():
    #Pantalla para generar clave
    clave = Clave()
    print('Su clave es: ')
    print('''
    p: %s
    e: %s
    d: %s
    '''%(str(clave.p),str(clave.e),str(clave.d)))
    run()

def menu_cifrar_mensaje(p,e):
    #Imprimimos pantalla para cifrar,y eesperamos valor
    valor = pantalla_cifrar()
    if valor == 'E':
        print('::: [E]scribir Mensaje :::')
        print()
        cifrar_mensaje(p,e)
    elif valor == 'I':
        print('::: [I]mportar Mensaje :::')
        print('El mensaje importado es: ')
        print()
        importar_mensaje(p, e, cifrado = False)
    elif valor == 'A':
        print('::: [A]tras :::')
        print()
        run()
    elif valor == 'S':
        print('::: [S] A L I R :::')
        quit()
    else:
        print('Comando no encontrado, intente de nuevo')
        print()
        menu_cifrar_mensaje(p,e)

def menu_decifrar_mensaje(p,d):
    #Imprimimos pantalla para cifrar,y esperamos valor
    valor = pantalla_cifrar()
    if valor == 'E':
        print('::: [E]scribir Mensaje :::')
        print()
        decifrar_mensaje(p,d)
    elif valor == 'I':
        print('Importar')
        print()
        importar_mensaje(p, d, cifrado =  True)
    elif valor == 'A':
        print('::: [A]tras :::')
        print()
        run()
    elif valor == 'S':
        print('::: [S] A L I R :::')
        quit()
    else:
        print('Comando no encontrado, intente de nuevo')
        print()
        menu_decifrar_mensaje(p,d)

def pantalla_cifrar():
    #Pantalla para cifrar
    print('''
    Las opciones disponibles son:

    [E]scribir mensaje
    [I]mportar mensaje (.txt)
    [A]tras
    [S]alir
        ''')
    valor = str(input('¿Que desea realizar?: ')).upper()
    return valor

def cifrar_mensaje(p,e):
    #Ciframos el mensaje almacenado en base a los parametros p,e
    texto = input('¿Cuál es el mensaje a cifrar?\n')
    mensaje = Mensaje(texto,p)
    mensaje_cifrado = Mensaje(mensaje.cifrar_mensaje(e),p)
    print()
    print('Su mensaje cifrado es:')
    print(mensaje_cifrado.texto)
    exportar_mensaje(mensaje_cifrado.texto, True)

def decifrar_mensaje(p,d):
    #Deciframos el mensaje almacenado en base a los parametros p,d
    texto = input('¿Cuál es el mensaje a decifrar?\n')
    mensaje_cifrado = Mensaje(texto,p)
    mensaje = Mensaje(mensaje_cifrado.decifrar_texto(d),p)             #Creamos la clase
    print()
    print('El mensaje decifrado es: ')
    print(mensaje.texto)
    exportar_mensaje(mensaje.texto,False)

def exportar_mensaje(texto, cifrado = True):
    #Pantalla para exportar mensaje
    print('''
    ¿Desea exportar el mensaje (.txt)?
    [S]i
    [N]o
    ''')
    respuesta = input('? ').upper()
    if respuesta == 'S':
        if cifrado:
            with open('mensaje_cifrado.txt','w') as f:
                f.write('Su mensaje cifrado es:\n')
                f.write(texto)
        else:
            with open('mensaje_decifrado.txt','w') as f:
                f.write('Su mensaje decifrado es:\n')
                f.write(texto)
        print('El archivo a sido exportado')
        run()
    elif respuesta == 'N':
        run()
    else:
        print('Comando no encontrado, intente de nuevo')
        print()
        exportar_mensaje(texto, cifrado)

def importar_mensaje(p, key, cifrado = True):
    #Pantalla para importar mensaje
    if cifrado:
        with open('mensaje_cifrado.txt') as f:
            lista_mensaje = f.readlines()
    else:
        with open('mensaje_decifrado.txt') as f:
            lista_mensaje = f.readlines()
    lista = lista_mensaje[1:]
    texto = ''
    for msje in lista:
        texto += msje
    print(texto)
    if cifrado:
        mensaje_cifrado = Mensaje(texto,p)
        mensaje = Mensaje(mensaje_cifrado.decifrar_texto(key),p)             #Creamos la clase
        print()
        print('El mensaje decifrado es: ')
        print(mensaje.texto)
        exportar_mensaje(mensaje.texto,False)
    else:
        mensaje = Mensaje(texto,p)
        mensaje_cifrado = Mensaje(mensaje.cifrar_mensaje(key),p)
        print()
        print('Su mensaje cifrado es:')
        print(mensaje_cifrado.texto)
        exportar_mensaje(mensaje_cifrado.texto, True)
    run()

if __name__ == '__main__':
    print('''
    *** S I S T E M A   D E   E N C R I P T A C I Ó N  E X P O N E N C I A L ***
    by: Alejoock
    ''')
    run()
