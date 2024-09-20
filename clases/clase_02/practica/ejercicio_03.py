""" Dado un número de 2n + 1 cifras, chequear si el mismo es palíndromo (capicúa). """

def es_palindromo(numero):
    numero_str = str(numero)
    return numero_str == numero_str[::-1]

numero = int(input("Ingrese un número de 2n + 1 cifras: "))
if es_palindromo(numero):
    print("El número es un palíndromo.")
else:
    print("El número no es un palíndromo.")