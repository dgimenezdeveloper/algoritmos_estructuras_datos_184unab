""" Escribir una función, llamada grep que reciba una expresión y un archivo, e imprima las líneas del archivo que contienen la expresión recibida. """

def grep(expresion, archivo):
    with open(archivo, 'r') as file:
        for linea in file:
            if expresion in linea:
                print(linea, end='')