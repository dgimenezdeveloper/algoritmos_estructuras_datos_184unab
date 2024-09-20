"""Confeccionar un programa que contenga las siguientes funciones:
1) Carga de una lista y retorno al bloque principal.
2) Fijar en cero todos los elementos de la lista que tengan un valor menor a 10.
3) Imprimir la lista"""

def cargar_lista():
    lista = []
    for x in range(5):
        valor = int(input('Ingrese un valor: '))
        lista.append(valor)
    return lista

def cargar_lista():
    lista = []
    cantidad = int(input('Ingrese la cantidad de elementos a ingresar: '))
    for x in range(cantidad):
        valor = int(input('Ingrese un valor: '))
        lista.append(valor)
    return lista

def fijar_cero_menores_10(lista):
    for x in range(len(lista)):
        if lista[x] < 10:
            lista[x] = 0

def imprimir_lista(lista):
    print(lista)

# Bloque principal del programa
def main():
    lista = cargar_lista()
    fijar_cero_menores_10(lista)
    imprimir_lista(lista)

main()

