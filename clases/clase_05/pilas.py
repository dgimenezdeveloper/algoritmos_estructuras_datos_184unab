""" 
El comportamiento de una Pila se puede describir mediante la frase “Lo último que se apiló es lo primero que se usa”. Este método se llama LIFO (Last In First Out).
Formalmente un Pila es un TAD que tiene las siguientes operaciones:
__init__ : Inicializa una pila vacía.
push (apilar): Agrega un nuevo elemento a la Pila
pop (desapilar): Remueve el tope de la Pila y lo devuelve. Este es el último elemento que se agregó.
is_empty (está_vacía): Retorna True o False según si la pila está vacía o no.
Opcionles:
top : Retorna el tope de la Pila (sin removerlo).
"""
# Implementacion de Pilas utilizando Listas
class Pila:
    def __init__(self):
        self.contenido = [] #La pila vacía se representa con una lista vacia
    
    def push(self, elemento):
        self.contenido.append(elemento)
    
    def pop(self):
        try:
            return self.contenido.pop()
        except IndexError:
            raise ValueError("La pila está vacía.")
    
    def is_empty(self):
        return self.contenido == []
    
    def top(self):
        try:
            return self.contenido[-1]
        except IndexError:
            raise ValueError("La pila está vacia.")
    
    def __str__(self):
        """ Devuelve una representación en forma de cadena de la pila. """
        elementos = []
        for i in self.contenido:
            elementos.append(str(i))
        return f'Pila: {elementos}'

p = Pila()
print(p.is_empty())
p.push(1)
print(p.is_empty())
p.push(5)
p.push("+")
p.push(23)
print(p.pop())
p.push(21)
print(p.top())
print(p)