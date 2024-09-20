""" Crear una clase Mercado, el cual estara representado mediante una o varias Listas Enlazadas cuyos nodos contengan como dato objetos del tipo Producto. Cada lista enlazada corresponde a un pasillo (o sección del mercado).

La clase debe contener métodos para facilitar:

Controlar el stock de productos (añadir y remover, etc).
Calcular en cuantos productos expiran en las proximas 24hs y removerlos.
Importante:

Pueden agregar más atributos y métodos, si lo consideran necesario. """

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
        if self.cabeza.producto.ID == ID:
            self.cabeza = self.cabeza.siguiente
        else:
            actual = self.cabeza
            while actual.siguiente:
                if actual.siguiente.producto.ID == ID:
                    actual.siguiente = actual.siguiente.siguiente
                    break
                actual = actual.siguiente
    
    def productos_a_expirar(self):
        expirados = []
        for producto in self:
            try:
                dias, horas = producto.calcularexpirados()
                if dias == 0 and horas < 24:
                    expirados.append(producto)
            except Exception as e:
                raise e
        for producto in expirados:
            self.remover(producto.ID)
        return expirados
    
    def __str__(self):
        productos = []
        for producto in self:
            productos.append(str(producto))
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
    
    