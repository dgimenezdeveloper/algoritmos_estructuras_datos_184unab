""" Implementar el tipo de dato *Cola* utilizando listas enlazadas. Completar la siguiente definición de la clase *Cola Enlazada*. """

from queue import Empty


class ColaEnlazada:
    """FIFO queue implementation using a singly linked list for storage."""

#-------- Clase Anidada - NODO ------------#
    class _Node:
        """Clase Nodo."""
        __slots__ = '_element', '_next' # optimiza el uso de memoria

        def __init__(self, element, next):
            self._element = element # inicializar el contenido del Nodo
            self._next = next       #referencia al siguiente Nodo

#----------- Métodos de la Cola ----------- #

    def __init__(self):
        """Crea una Cola Vacia."""
        self._head = None
        self._tail = None
        self._size = 0  # Numero de elementos en la Cola

    def __len__(self):
        """Retorna el numero de elementos de la Cola."""
        return self._size

    def is_empty(self):
        """True si la Cola esta vacia."""
        return self._size == 0

    def first(self):
        """Retornar (sin remover) el primer elemento de la Cola.
        

        Raise Empty exception if the queue is empty. """
        # COMPLETAR #
        if self.is_empty():
            raise Empty("La Cola esta vacia")
        else:
            return self._head._element

    def dequeue(self):
        """Remove and return the first element of the queue (i.e., FIFO).

        Raise Empty exception if the queue is empty."""
            # Ejemplo:   ## if self.is empty():
            #            ##    raise Empty( Queue is empty )
        if self.is_empty():
            raise Empty("La Cola esta vacia")
        else:
            eliminado = self.first() # Guardo el primer elemento
            self._head = self._head._next # Actualizo la cabeza
            self._size -= 1
            if self.is_empty(): # Si la cola esta vacia, actualizo la cola
                self._tail = None
            return eliminado

    def enqueue(self, e):
        """Add an element to the back of queue."""
        # COMPLETAR #
        nuevo = self._Node(e, None)
        if self.is_empty():
            self._head = nuevo
        else:
            self._tail._next = nuevo
        self._tail = nuevo
        self._size += 1

    def __iter__(self):
        """Iterador de la Cola."""
        self._actual = self._head
        return self
    
    def __next__(self):
        """Retorna el siguiente elemento de la Cola."""
        if self._actual is not None:
            nodo = self._actual._element
            self._actual = self._actual._next
            return nodo
        else:
            raise StopIteration

    def __str__(self):
        """Retorna una representación en cadena de la Cola."""
        cadena = "["
        for elemento in self:
            cadena += str(elemento) + ", "
        return cadena.rstrip(", ") + "]"
    
def main():
    cola = ColaEnlazada()
    cola.enqueue(1)
    cola.enqueue(2)
    cola.enqueue(3)
    cola.enqueue(4)
    cola.enqueue(5)
    print("Cola original:", cola)

main()
