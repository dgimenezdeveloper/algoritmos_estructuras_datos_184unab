""" Diseñar un algoritmo que calcula e imprime la suma de los números pares comprendidos entre 2 y 100. """
suma = 0
for num in range(2, 101, 2):
    suma += num
print("La suma de los números pares entre 2 y 100 es:", suma)