class Pila:
    """ Representa una pila con operaciones de apilar, desapilar y verificar si está vacía. """

    def __init__(self):
        """ Crea una pila vacía. """
        self.contenido = []  # La pila vacía se representa con una lista vacía

    def push(self, x):
        """ Agrega el elemento x a la pila. """
        self.contenido.append(x)  # Apilar es agregar al final de la lista.

    def pop(self):
        """ Devuelve el elemento tope y lo elimina de la pila.
            Si la pila está vacía levanta una excepción. """
        try:
            return self.contenido.pop()  # Desapilar es quitar el último elemento de la lista.
        except IndexError:
            raise ValueError("La pila está vacía.")

    def is_empty(self):
        """ Devuelve True si la lista está vacía, False si no. """
        return self.contenido == []  # La pila está vacía si la lista está vacía.

    def top(self):
        """ Devuelve el elemento tope sin eliminarlo de la pila.
            Si la pila está vacía levanta una excepción. """
        try:
            return self.contenido[-1]  # Devuelve el último elemento de la lista.
        except IndexError:
            raise ValueError("La pila está vacía.")

    def __str__(self):
        """ Devuelve una representación en forma de cadena de la pila. """
        elementos = ', '.join(str(x) for x in self.contenido)
        return f'Pila: [{elementos}]'  # Representación de la pila como una cadena.

# Ejemplo de uso y explicaciones

# Crear una pila vacía
pila = Pila()

# Agregar elementos a la pila (apilar)
pila.push(1)  # La pila ahora contiene: [1]
pila.push(2)  # La pila ahora contiene: [1, 2]
pila.push(3)  # La pila ahora contiene: [1, 2, 3]

# Mostrar la pila
print(pila)  # Debería imprimir "Pila: [1, 2, 3]"

# Ver el elemento en el tope de la pila sin eliminarlo
print("Tope de la pila:", pila.top())  # Debería imprimir "Tope de la pila: 3"

# Eliminar el elemento del tope de la pila (desapilar)
pila.pop()  # La pila ahora contiene: [1, 2]

# Mostrar la pila después de desapilar
print(pila)  # Debería imprimir "Pila: [1, 2]"

# Verificar si la pila está vacía
print("¿La pila está vacía?", pila.is_empty())  # Debería imprimir "¿La pila está vacía? False"

# Desapilar todos los elementos
pila.pop()  # La pila ahora contiene: [1]
pila.pop()  # La pila ahora está vacía: []

# Verificar nuevamente si la pila está vacía
print("¿La pila está vacía?", pila.is_empty())  # Debería imprimir "¿La pila está vacía? True"
