""" Añadir a la clase Mercado un atributo clientes implementando una clase ColaPrioridad utilizando el siguiente modelo de definición,  Una Cola de Prioridades es similar a una cola pero sus elementos tienen una prioridad asignada. Los elementos de mayor prioridad serán desencolados primero

"""
"""
class _Node:

    __slot_s_ = '_element', '_next', '_priory' # optimiza el uso de memoria
    def _init__(self, element, prev, next):
        self._element = element #inicializar contenido del Nodo
        self._next = next # referencia al siguiente Nodo
        self._priory = priory # prioridad del elemento
        
class ColaPrioridad:

def __init__(self):
    
    self._head = None
    self._tail = None
    self._size = 0 # Numero de elementos en la Cola

"""
from ejercicio02 import ListaEnlazada, Nodo
class Mercado:
    def __init__(self):
        self.pasillos = {}

    def agregar_producto(self, pasillo, producto):
        if pasillo not in self.pasillos:
            self.pasillos[pasillo] = ListaEnlazada()
        self.pasillos[pasillo].agregar(producto)

    def remover_producto(self, pasillo, ID):
        if pasillo in self.pasillos:
            self.pasillos[pasillo].remover(ID)

    def productos_a_expirar_24hs(self):
        expirados = {}
        for pasillo, lista in self.pasillos.items():
            expirados[pasillo] = lista.productos_a_expirar()
        return expirados

    def vender_producto(self, ID):
        producto_encontrado = False
        for pasillo, lista in self.pasillos.items():
            for producto in lista:
                if producto.ID == ID:
                    lista.remover(ID)
                    producto_encontrado = True
                    break
            if producto_encontrado:
                break
        if not producto_encontrado:
            raise Exception("Producto no encontrado o ya vendido.")

class _Node:
    """Clase Nodo."""
    __slots__ = '_element', '_next', '_priority'  # optimiza el uso de memoria

    def __init__(self, element, next, priority):
        self._element = element  # inicializar el contenido del Nodo
        self._next = next  # referencia al siguiente Nodo
        self._priority = priority  # prioridad del elemento
    
class ColaPrioridad:
    """Clase Cola de Prioridades"""

    def __init__(self):
        """Crea una Cola Vacia."""
        self._head = None
        self._tail = None
        self._size = 0
    
    def __len__(self):
        return self._size == 0
    
    def is_empty(self):
        try:
            return self._size == 0
        except Exception as e:
            raise e
    
    def first(self):
        try:
            return self._head._element
        except Exception as e:
            raise e
    
    def dequeue(self):
        try:
            answer = self._head._element
            self._head = self._head._next
            self._size -= 1
            if self.is_empty():
                self._tail = None
            return answer
        except Exception as e:
            raise e
    
    def enqueue(self, e, priority):
        try:
            new_node = _Node(e, None, priority)
            if self.is_empty() or priority > self._head._priority:
                new_node._next = self._head
                self._head = new_node
            else:
                current = self._head
                while current._next and current._next._priority >= priority:
                    current = current._next
                new_node._next = current._next
                current._next = new_node
            self._size += 1
        except Exception as e:
            raise e
    
    def __iter__(self):
        self.actual = self._head
        return self
    
    def __next__(self):
        if self.actual:
            producto = self.actual._element
            self.actual = self.actual._next
            return producto
        else:
            raise StopIteration