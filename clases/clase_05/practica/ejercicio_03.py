""" Sobrecargar los métodos __str__ y __add__ para la pila enlazada. """

class ListaSimpleEnlazada:
    """Clase Lista 'Simplemente' Enlazada."""

#-------- Clase Anidada - NODO ------------#
    class _Node:
        """Clase Nodo."""
        __slots__ = '_element', '_next' # optimiza el uso de memoria

        def __init__(self, element, next):
            self._element = element # inicializar el contenido del Nodo
            self._next = next       #referencia al siguiente Nodo

    def __init__(self):
        """Crea una Pila Vacia."""
        self._head = None  #referencia a la "cabeza" de la lista
        self._size = 0     #cantidad de elementos


    def __len__(self):
        """Retorna el numero de elementos de la Pila."""
        return self._size

    def is_empty(self):
        """Retorna VERDADERO si la Pila esta Vacia."""
        return self._size == 0
    
    # ----------- Sobrecarga de Operadores Añadidos ----------- #
    def __iter__(self):
        """Iterador de la Pila."""
        self._actual = self._head
        return self
    
    def __next__(self):
        """Retorna el siguiente elemento de la Pila."""
        if self._actual is not None:
            nodo = self._actual._element
            self._actual = self._actual._next
            return nodo
        else:
            raise StopIteration
    
    #----------- Métodos de la Pila ----------- #

    def push(self, elem):  # COMPLETAR #
        nuevo = self._Node(elem, None)
        if self.is_empty():
            self._head = nuevo
        else:
            nuevo._next = self._head
            self._head = nuevo
        self._size += 1
        
    def pop(self):# COMPLETAR #
        if self.is_empty():
            raise ValueError("Pila vacía")
        valor = self._head._element
        self._head = self._head._next
        self._size -= 1
        return valor
    
    def top(self):   # COMPLETAR #
        if self.is_empty():
            raise ValueError("Pila vacía")
        return self._head._element           
    
    # RESOLUCION EJERCICIO 3    
    def __str__(self):
        """Retorna una representación en cadena de la Pila."""
        cadena = "["
        for elemento in self:
            cadena += str(elemento) + ", "
        return cadena.rstrip(", ") + "]"
    
    def __add__(self, otro):
        nueva_pila = ListaSimpleEnlazada()
        for elemento in self: 
            nueva_pila.push(elemento) 
        for elemento in otro:
            nueva_pila.push(elemento) 
        return nueva_pila
    
def main():
    

    pila = ListaSimpleEnlazada()
    pila.push(21)
    pila.push(9)
    pila.push(1985)
    print("Pila:", pila)
    pila2 = ListaSimpleEnlazada()
    pila2.push(10)
    pila2.push(20)
    print("Pila 2:", pila2)
    nueva_pila = pila + pila2
    print("Nueva Pila:", nueva_pila)
main()