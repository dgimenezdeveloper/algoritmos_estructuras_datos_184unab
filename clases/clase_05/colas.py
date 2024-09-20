class Cola:
    """ Representa una cola con operaciones de encolar, desencolar y verificar si está vacía. """

    def __init__(self):
        """ Crea una cola vacía. """
        self.contenido = []  # La cola vacía se representa con una lista vacía

    def encolar(self, x):
        """ Agrega el elemento x a la cola. """
        self.contenido.append(x)  # Encolar es agregar al final de la lista.

    def desencolar(self):
        """ Devuelve el primer elemento y lo elimina de la cola.
            Si la cola está vacía levanta una excepción. """
        try:
            return self.contenido.pop(0)  # Desencolar es quitar el primer elemento de la lista.
        except IndexError:
            raise ValueError("La cola está vacía.")

    def is_empty(self):
        """ Devuelve True si la lista está vacía, False si no. """
        return self.contenido == []  # La cola está vacía si la lista está vacía.

    def front(self):
        """ Devuelve el primer elemento sin eliminarlo de la cola.
            Si la cola está vacía levanta una excepción. """
        try:
            return self.contenido[0]  # Devuelve el primer elemento de la lista.
        except IndexError:
            raise ValueError("La cola está vacía.")

    def __str__(self):
        """ Devuelve una representación en forma de cadena de la cola. """
        elementos = ', '.join(str(x) for x in self.contenido)
        return f'Cola: [{elementos}]'  # Representación de la cola como una cadena.

# Ejemplo de uso y explicaciones

# Crear una cola vacía
cola = Cola()

# Agregar elementos a la cola (encolar)
cola.encolar(1)  # La cola ahora contiene: [1]
cola.encolar(2)  # La cola ahora contiene: [1, 2]
cola.encolar(3)  # La cola ahora contiene: [1, 2, 3]

# Mostrar la cola
print(cola)  # Debería imprimir "Cola: [1, 2, 3]"

# Ver el primer elemento de la cola sin eliminarlo
print("Primer elemento de la cola:", cola.front())  # Debería imprimir "Primer elemento de la cola: 1"

# Eliminar el primer elemento de la cola (desencolar)
cola.desencolar()  # La cola ahora contiene: [2, 3]

# Mostrar la cola después de desencolar
print(cola)  # Debería imprimir "Cola: [2, 3]"

# Verificar si la cola está vacía
print("¿La cola está vacía?", cola.is_empty())  # Debería imprimir "¿La cola está vacía? False"

# Desencolar todos los elementos
cola.desencolar()  # La cola ahora contiene: [2]
cola.desencolar()  # La cola ahora está vacía: []

# Verificar nuevamente si la cola está vacía
print("¿La cola está vacía?", cola.is_empty())  # Debería imprimir "¿La cola está vacía? True"
