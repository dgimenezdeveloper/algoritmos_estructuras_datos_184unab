""" Escribir un algoritmo que muestre por pantalla las tablas de multiplicacion, desde el 1 hasta el 9. """

for i in range(1, 10):
    print(f"Tabla de multiplicación del {i}:")
    for j in range(1, 11):
        resultado = i * j
        print(f"{i} x {j} = {resultado}")
    print()