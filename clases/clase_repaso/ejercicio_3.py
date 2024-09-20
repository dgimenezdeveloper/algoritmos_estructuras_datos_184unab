class Polinomio():
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c
    
    def evaluar(self, x):
        return self._a * x**2 + self._b * x + self._c
    
    def __str__(self):
        return f'{self._a}x^2 + {self._b}x + {self._c}'

# Bloque principal del programa
def main():
    polinomio = Polinomio(2, 3, 1)
    print(polinomio)
    print(polinomio.evaluar(2))
    print(polinomio.evaluar(3))
    print(polinomio.evaluar(5))

main()