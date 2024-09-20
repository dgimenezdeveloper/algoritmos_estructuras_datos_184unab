""" Implementar una funcion iterativa que calcule la suma de una lista de numeros enteros """
def sumatoria(lista):
    suma = 0
    for i in lista:
        suma += i
    return suma

""" Implementar una funcion recursiva que calcule la suma de una lista de numeros enteros """
def sumatoria_recursiva(lista):
    if len(lista) == 0:
        return 0
    return lista[0] + sumatoria_recursiva(lista[1:])

""" Definir una clase Circulo. La clase debe contener los siguientes metodos:
- Calcular el peri­metro del circulo
- Calcular el area del circulo
- Dado un punto, calcular si este pertenece al circulo.
Importante: 
- Pueden agregar más atributos y metodos, si lo consideran necesario.

Sobrecargar el método __eq__ es decir, dados dos circulos, comparar si son iguales

Sobrecargar los metodos __lt__ y __gt__ para comparar dos circulos por su radio

Agregar a la clase circulo un método que permita calcular lo siguiente:
- Dados dos puntos calcular si la recta que pasa por ellos es tangente o secante al circulo
- Si la recta no intersecta al circulo, el metodo retorna un error
"""
import math
class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def perimetro(self):
        return 2 * math.pi * self.radio

    def area(self):
        return math.pi * self.radio ** 2

    def punto_pertenece(self, x, y):
        return x ** 2 + y ** 2 <= self.radio ** 2
    
    def __eq__(self, otro):
        return self.radio == otro.radio
    
    def __lt__(self, otro):
        return self.radio < otro.radio
    
    def __gt__(self, otro):
        return self.radio > otro.radio
    
    def tangente_o_secante(self, x1, y1, x2, y2):
        if x1 == x2:
            if x1 == 0:
                return "Tangente"
            return "Secante"
        m = (y2 - y1) / (x2 - x1)
        c = y1 - m * x1
        a = m ** 2 + 1
        b = 2 * m * c
        c = c ** 2 - self.radio ** 2
        discriminante = b ** 2 - 4 * a * c
        if discriminante < 0:
            raise ValueError("La recta no intersecta al circulo")
        if discriminante == 0:
            return "Tangente"
        return "Secante"
    
    

""" Sobrecargar el método __eq__ es decir, dados dos circulos, comparar si son iguales """

