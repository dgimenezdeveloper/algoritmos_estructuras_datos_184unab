""" Escribir una función, llamada head que reciba como parámetros un archivo y un número N e imprima las primeras N líneas del archivo. """

def head(archivo, N):
    with open(archivo, 'r') as file:
        for i in range(N):
            print(file.readline(), end='')

