""" Diseñar un algoritmo que dado tres números, determinar si la suma de cualquier pareja de ellos es igual al tercer número. Si se cumple esta condición deberá imprimir la palabra ''iguales'', sino ''distintos''. """
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

if num1 + num2 == num3 or num1 + num3 == num2 or num2 + num3 == num1:
    print("iguales")
else:
    print("distintos")