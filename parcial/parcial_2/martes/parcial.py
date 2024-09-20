""" 
Definir una clase Producto, el cual contiene los siguientes datos:
descripcion : 'string' 
ID : 'integer' 
FechaExp : date, ## importar datetime 
INFO : 'de cualquier tipo' 
La clase debe contener los siguinetes métodos:
Cambiar uno o varios datos del Producto.
calcularexpirados()Calcular en cuantos dias/horas expira un producto. Si el método detecta que el producto ha expirado, debera lanzar una excepción.
Sobrecarga de métodos:
__str__
__eq__
Importante:Pueden agregar más atributos y métodos, si lo consideran necesario.

Crear una clase Mercado, el cual estara representado mediante una o varias Listas Enlazadas cuyos nodos contengan como dato objetos del tipo Producto. Cada lista enlazada corresponde a un pasillo (o sección del mercado).
La clase debe contener métodos para facilitar:
Controlar el stock de productos (añadir y remover, etc).
Calcular en cuantos productos expiran en las proximas 24hs y removerlos.
Importante:Pueden agregar más atributos y métodos, si lo consideran necesario.

Añadir un método a la clase Mercado que permita buscar un producto y removerlo (venderlo). Recordar que deben actualizar el stock. Si un producto se termina, el método debe lanzar una excepcion.
Importante:Utilizar Iteradores de ser posible.
Pueden agregar más atributos y funciones/métodos, si lo consideran necesario. 

Añadir a la clase Mercado un atributo clientes implementando una clase ColaPrioridad utilizando el siguiente modelo de definición,  Una Cola de Prioridades es similar a una cola pero sus elementos tienen una prioridad asignada. Los elementos de mayor prioridad serán desencolados primero

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

Implementar un Iterador para la clase ColaPrioridad.

Escribir una función, llamada head que reciba como parámetros un archivo y un número N e imprima las primeras N líneas del archivo. 

Escribir una función, llamada grep que reciba una expresión y un archivo, e imprima las líneas del archivo que contienen la expresión recibida. 
"""

import datetime
from datetime import date

class Producto:
    def __init__(self, descripcion, ID, FechaExp, INFO):
        self.descripcion = descripcion
        self.ID = ID
        self.FechaExp = FechaExp
        self.INFO = INFO
    
    def cambiar_datos(self, descripcion=None, ID=None, FechaExp=None, INFO=None):
        if descripcion:
            self.descripcion = descripcion
        if ID:
            self.ID = ID
        if FechaExp:
            self.FechaExp = FechaExp
        if INFO:
            self.INFO = INFO
    
    def calcularexpirados(self):
        hoy = datetime.datetime.now().date()
        if self.FechaExp <= hoy:
            return 0  # Expired today or before
        else:
            diferencia = self.FechaExp - hoy
            return diferencia.days
    
    def __str__(self):
        return f"Producto(ID={self.ID}, Descripción='{self.descripcion}', Fecha de Expiración={self.FechaExp}, INFO={self.INFO})"
    
    def __eq__(self, otro):
        return self.ID == otro.ID

class Nodo:
    def __init__(self, producto=None, siguiente=None):
        self.producto = producto
        self.siguiente = siguiente

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def __iter__(self):
        self.actual = self.cabeza
        return self

    def __next__(self):
        if self.actual:
            producto = self.actual.producto
            self.actual = self.actual.siguiente
            return producto
        else:
            raise StopIteration

    def agregar(self, producto):
        if not self.cabeza:
            self.cabeza = Nodo(producto)
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = Nodo(producto)

    def remover(self, ID):
        if not self.cabeza:
            return
        if self.cabeza.producto.ID == ID:
            self.cabeza = self.cabeza.siguiente
        else:
            actual = self.cabeza
            while actual.siguiente:
                if actual.siguiente.producto.ID == ID:
                    actual.siguiente = actual.siguiente.siguiente
                    return
                actual = actual.siguiente
    
    def productos_a_expirar(self):
        expirados = []
        actual = self.cabeza
        anterior = None
        while actual:
            try:
                dias = actual.producto.calcularexpirados()
                if dias == 0:  # Expira hoy o ya expirado
                    expirados.append(actual.producto)
                    if anterior:
                        anterior.siguiente = actual.siguiente
                    else:
                        self.cabeza = actual.siguiente
            except Exception as e:
                print(e)
            anterior = actual
            actual = actual.siguiente
        
        return expirados
    
    def __str__(self):
        productos = []
        actual = self.cabeza
        while actual:
            productos.append(str(actual.producto))
            actual = actual.siguiente
        return "\n".join(productos)

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
    __slots__ = '_element', '_next', '_priority'

    def __init__(self, element, next, priority):
        self._element = element
        self._next = next
        self._priority = priority

class ColaPrioridad:
    def __init__(self):
        self._head = None
        self._size = 0
    
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def first(self):
        if self.is_empty():
            raise Exception("Cola vacía.")
        return self._head._element
    
    def dequeue(self):
        if self.is_empty():
            raise Exception("Cola vacía.")
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer
    
    def enqueue(self, e, priority):
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
    
    def __iter__(self):
        self.actual = self._head
        return self
    
    def __next__(self):
        if self.actual:
            element = self.actual._element
            self.actual = self.actual._next
            return element
        else:
            raise StopIteration

def head(archivo, N):
    with open(archivo, 'r') as file:
        for i in range(N):
            print(file.readline(), end='')

def grep(expresion, archivo):
    with open(archivo, 'r') as file:
        for linea in file:
            if expresion in linea:
                print(linea, end='')

def main():
    # Crear algunos productos
    prod1 = Producto("Manzanas", 1, date(2024, 7, 1), "Frutas")
    prod2 = Producto("Leche", 2, date(2024, 6, 26), "Lácteos")
    prod3 = Producto("Pan", 3, date(2024, 6, 25), "Panadería")

    # Crear un mercado y agregar productos a diferentes pasillos
    mercado = Mercado()
    mercado.agregar_producto("Frutas", prod1)
    mercado.agregar_producto("Lácteos", prod2)
    mercado.agregar_producto("Panadería", prod3)

    # Mostrar productos antes de remover expirados
    print("Productos antes de remover expirados:")
    for pasillo, lista in mercado.pasillos.items():
        print(f"Pasillo: {pasillo}")
        print(lista)

    # Remover productos que expiran en las próximas 24 horas
    expirados = mercado.productos_a_expirar_24hs()
    print("\nProductos removidos (expirados en 24 horas):")
    for pasillo, productos in expirados.items():
        for producto in productos:
            print(producto)

    # Mostrar productos después de remover expirados
    print("\nProductos después de remover expirados:")
    for pasillo, lista in mercado.pasillos.items():
        print(f"Pasillo: {pasillo}")
        print(lista)

if __name__ == "__main__":
    main()
