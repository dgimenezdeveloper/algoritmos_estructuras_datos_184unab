"""
Escribir un programa, que tome como entrada un string del usuario, el cuál debe ser impreso por pantalla en orden reverso. El programa también debe imprimir la palabra "Bingo!", si el string ingresado es palíndromo. """

string = input("Ingrese un string: ")
reversed_string = string[::-1]
print(reversed_string)

if string == reversed_string:
    print("Bingo!")
