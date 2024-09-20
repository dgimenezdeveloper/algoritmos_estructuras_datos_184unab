""" Diseñar un algoritmo que calcule la media de una serie de números positivos entrados por teclado. El ingreso de un valor igual a cero indicará el final del ingreso de datos. """
numbers = []
while True:
    num = float(input("Ingrese un número positivo (0 para terminar): "))
    if num == 0:
        break
    elif num < 0:
        print("Error: el número ingresado no es positivo.")
    else:
        numbers.append(num)

if len(numbers) > 0:
    average = sum(numbers) / len(numbers)
    print("La media de los números ingresados es:", average)
else:
    print("No se ingresaron números positivos.")