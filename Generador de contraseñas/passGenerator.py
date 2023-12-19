# Author: CabaCrD
#ESTE PROGRAMA ES SIMPLEMENTE UN GENERADOR DE CONTRASEÑAS QUE FUNCIONA MEDIANTE LA CONSOLA DE COMANDOS

import random #IMPORTANOS RANDOM

# VARIABLES QUE USAREMOS
caracteresMinus = "abcdefghijqlmnopqrstuvwxyz"
caracteresMayus = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
caracteresNum = "0123456789"
caracteresSimbol = "!@#$%^&*_-+="
contrasena = ""
longitud = 0
minusculas = ""
numeros = ""
mayusculas = ""
simbolos = ""

print("Bienvenido al generador de contraseñas")

while True: #BUCLE WHILE

    try: #MANEJO DE EXCEPCIONES

        longitud = int(input("Introduzca la longitud de la contraseña (8/2048): ")) #LONGITUD

        if 8 <= longitud <= 2048: #SI SE CUMPLE LA CONDICION

            minusculas = input("¿Quiere que contenga minúsculas (S/N) ").upper() #MINUSCULAS

            if minusculas == "N" or minusculas == "S": #SI SE CUMPLE LA CONDICION

                numeros = input("¿Quiere que contenga números (S/N) ").upper() #NUMEROS

                if numeros == "N" or numeros == "S": #SI SE CUMPLE LA CONDICION

                    mayusculas = input("¿Quiere que contenga mayúsculas (S/N) ").upper() #MAYUSCULAS

                    if mayusculas == "N" or mayusculas == "S": #SI SE CUMPLE LA CONDICION

                        simbolos = input("¿Quiere que contenga símbolos (S/N) ").upper() #SIMBOLOS

                        if simbolos == "N" or simbolos == "S": #SI SE CUMPLE LA CONDICION

                            break 

                        else:

                            print("Por favor, elija una opcion válida") #SI NO SE CUMPLE LA CONDICION

                    else:

                        print("Por favor, elija una opcion válida") #SI NO SE CUMPLE LA CONDICION

                else:

                    print("Por favor, elija una opcion válida") #SI NO SE CUMPLE LA CONDICION

            else:

                print("Por favor, elija una opcion válida") #SI NO SE CUMPLE LA CONDICION

        else:

            print("Por favor, elija una longitud válida") #SI NO SE CUMPLE LA CONDICION

    except ValueError:

        print("Por favor, elija una opcion válida.") #MENSAJE DE MANEJO DE EXCEPCIONES

cadena = "" #CADENA CON LAS OPCIOPNES SELECCIONADAS

if minusculas == "S": #SI SE SELECCIONARON LAS MINUSCULAS

    cadena += caracteresMinus

if mayusculas == "S": # SI SE SELECCIONARON LAS MAYUSCULAS

    cadena += caracteresMayus

if numeros == "S": # SI SE SELECCIONARON LAS NUMEROS

    cadena += caracteresNum

if simbolos == "S": # SI SE SELECCIONARON LAS SIMBOLOS

    cadena += caracteresSimbol

if not cadena: # SI NO SELECCIONAMOPS NINGUNA OPCIÓN

    print("Ninguna opción seleccionada, no se generará la contraseña")#IMPRIMIMOS EL MENSAJE

else: # SI SELECCIONAMOS ALGUNA OPCION

    contrasena = ''.join(random.choice(cadena) for _ in range(longitud))# A LA CADENA SE LE SUMARA UNOS CARACTERES ALEATORIOS DE LA CADENA JUNTO A UN BUCLE FOR CON LA LONGITUD SELECCIONADA
    print("Contraseña: ", contrasena)# IMPRIMIMOS LA CONTRASEÑA
