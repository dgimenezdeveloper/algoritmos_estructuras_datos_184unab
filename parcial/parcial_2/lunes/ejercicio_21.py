""" 2.1 - Agregar a la clase Comprador un método comprar_articulo que permita adquirir Artículos y agregarlos a una lista (privada) de artículos comprados. Al comprarlos, los puntos del artículo se suman a los puntos de Comprador. """
class Comprador:
    def __init__(self, nombre, direccion, telefono, fecha_nacimiento):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.fecha_nacimiento = fecha_nacimiento
        self.puntaje = 0
        self._articulos_comprados = []
    
    def sumar_puntos(self, puntos):
        self.puntaje += puntos
    
    def restar_puntos(self, puntos):
        self.puntaje -= puntos
    
    def comprar_articulos(self, articulo):
        self._articulos_comprados.append(articulo)
        self.sumar_puntos(articulo.puntos)