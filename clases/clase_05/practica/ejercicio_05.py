""" Implementar el tipo de dato lista circular. """
class ListaEnlazadaCircular:
    """Clase Lista enlazada Circular."""

#-------- Clase Anidada - NODO ------------#
    class _Node:
        """Clase Nodo."""
        __slots__ = '_element', '_next' # optimiza el uso de memoria

        def __init__(self, element, next):
            self._element = element # inicializar el contenido del Nodo
            self._next = next       # referencia al siguiente Nodo

    def __init__(self):
        """Crea una Lista Vacia."""
        self._head = None  #referencia a la "cabeza" de la lista
        self._size = 0     #cantidad de elementos

    def __len__(self):
        """Retorna el numero de elementos de la Lista."""
        return self._size

    def is_empty(self):
        """Retorna VERDADERO si la Lista esta Vacia."""
        return self._size == 0

    def append(self, x):
    ## Agrega un elemento al final de la lista. ##
    ## COMPLETAR ##
        if self.is_empty(): 
            nuevo_nodo = self._Node(x, None) 
            self._head = nuevo_nodo 
            self._head._next = self._head 
        else:
            nuevo_nodo = self._Node(x, self._head._next)
            self._head._next = nuevo_nodo
        self._size += 1

    def insert(self, i, x):
    ## Agrega el elemento 'x' en la posición 'i' ##
    # levanta una excepción / informa un erorr; si la posición 'i'es inválida. #
    ## COMPLETAR ##
        if i < 0 or i > self._size:
            raise IndexError('Posición inválida')
        if i == 0:
            self.append(x)
        else:
            nuevo_nodo = self._Node(x, None)
            actual = self._head
            for _ in range(i-1):
                actual = actual._next
            nuevo_nodo._next = actual._next
            actual._next = nuevo_nodo
            self._size += 1
    

    def remove(self, x):
    ## Eliminar la primera aparición de 'x' en la lista ##
    # levanta una excepción / informa error; si 'x' no está.
    ## COMPLETAR ##
        if self.is_empty():
            raise ValueError('Lista vacía')
        actual = self._head
        if actual._element == x:
            self._head = self._head._next
            self._size -= 1
            return
        while actual._next != self._head:
            if actual._next._element == x:
                actual._next = actual._next._next
                self._size -= 1
                return
            actual = actual._next
        raise ValueError('Elemento no encontrado')

    def pop(self, i = None):
    ## borra el elemento que está en la posición 'i' y devolver su valor. ##
    # Si no se especifica el valor de 'i' ver el método pop() debajo #
    ## COMPLETAR ##
        if i is None:
            i = self._size - 1
        if i < 0 or i >= self._size:
            raise IndexError('Posición inválida')
        if i == 0:
            valor = self._head._element
            self._head = self._head._next
            self._size -= 1
            return valor
        actual = self._head
        for _ in range(i-1):
            actual = actual._next
        valor = actual._next._element
        actual._next = actual._next._next
        self._size -= 1
        return valor
        
    def pop(self):
    ## elimina y devuelve el elemento que está en el último lugar de la lista ##
    # levanta una excepción / informa del error; si se hace  referencia a una posición no válida de la lista. #
    ## COMPLETAR ##
        if self.is_empty():
            raise ValueError('Lista vacía')
        valor = self._head._element
        if self._size == 1:
            self._head = None
        else:
            actual = self._head
            for _ in range(self._size-2):
                actual = actual._next
            valor = actual._next._element
            actual._next = self._head
        self._size -= 1
        return valor

    def index(self, x):
    ## devuelve la posición de la primera aparición de 'x' en la lista ##
    # levanta una excepción / informa error; si 'x' no está.
    ## COMPLETAR ##
        if self.is_empty():
            raise ValueError('Lista vacía')
        actual = self._head
        for i in range(self._size):
            if actual._element == x:
                return i
            actual = actual._next
        raise ValueError('Elemento no encontrado')
    
    def __str__(self):
        """Retorna una representación en string de la lista."""
        if self.is_empty():
            return '[]'
        actual = self._head
        s = '[' + str(actual._element)
        actual = actual._next
        while actual != self._head:
            s += ', ' + str(actual._element)
            actual = actual._next
        return s + ']'
    
    def __iter__(self):
        """Iterador de la lista."""
        actual = self._head
        for _ in range(self._size):
            yield actual._element
            actual = actual._next
    
    def __next__(self):
        """Iterador de la lista."""
        actual = self._head
        for _ in range(self._size):
            yield actual._element
            actual = actual._next

#-------- Fin de la Clase ListaEnlazadaCircular ------------#
