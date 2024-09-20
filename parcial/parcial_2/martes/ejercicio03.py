""" Añadir un método a la clase Mercado que permita buscar un producto y removerlo (venderlo). Recordar que deben actualizar el stock. Si un producto se termina, el método debe lanzar una excepcion.

Importante:

Utilizar Iteradores de ser posible.
Pueden agregar más atributos y funciones/métodos, si lo consideran necesario. """
from ejercicio01 import Producto, datetime
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