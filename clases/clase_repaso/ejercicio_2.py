"""Desarrollar una clase que represente un punto en el plano y tenga 
los siguientes métodos: inicializar los valores de x e y que llegan como parámetros,
imprimir en que cuadrante se encuentra dicho punto (concepto matemático, 
primer cuadrante si x e y son positivas, si x<0 e y>0 segundo cuadrante, etc.)"""

class Plano():
    def __init__(self,x,y):
        self._x = x
        self._y = y
    
    def cuadrante(self):
        if self._x > 0 and self._y > 0:
            print('Primer cuadrante')
        elif self._x < 0 and self._y > 0:
            print('Segundo cuadrante')
        elif self._x < 0 and self._y < 0:
            print('Tercer cuadrante')
        elif self._x > 0 and self._y < 0:
            print('Cuarto cuadrante')
        else:
            print('Origen')

    def __str__(self):
        return f'Punto: ({str(self._x)},{str(self._y)})'

# Bloque principal del programa
def main():
    punto = Plano(2,3)
    print(punto)
    punto.cuadrante()
    punto = Plano(-2,3)
    print(punto)
    punto.cuadrante()
    punto = Plano(-2,-3)
    print(punto)
    punto.cuadrante()
    punto = Plano(2,-3)
    print(punto)
    punto.cuadrante()
    punto = Plano(0,0)
    print(punto)
    punto.cuadrante()

main()