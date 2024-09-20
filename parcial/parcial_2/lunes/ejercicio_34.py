""" Crear una lista enlazada de todos los artículos creados en el punto 3.1, y escribir una función que pueda procesar esta lista y determinar (devolviendo un valor booleano) si existen dos artículos con la misma cantidad de puntos.
 """

class Nodo:
    def __init__(self, articulo):
        self.articulo = articulo
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, articulo):
        nodo = Nodo(articulo)
        if self.cabeza is None:
            self.cabeza = nodo
        else:
            nodo.siguiente = self.cabeza
            self.cabeza = nodo
    
    def articulos_mismos_puntos(self):
        puntos = []
        nodo = self.cabeza
        while nodo is not None:
            if nodo.articulo.puntos in puntos:
                return True
            puntos.append(nodo.articulo.puntos)
            nodo = nodo.siguiente
        return False