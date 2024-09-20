""" Agregar a la clase Comprador un método eliminar_articulo que reciba el identificador del artículo y elimine TODAS las instancias del artículo en la lista del comprador. En cada ocasión, deben eliminarse los puntos correspondientes al artículo del puntaje del Comprador. """
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
    
    def encontrar_articulo(self, identificador):
        for articulo in self._articulos_comprados:
            if articulo.identificador == identificador:
                return True
        return False
    
    def eliminar_articulo(self, identificador):
        articulos_a_eliminar = [articulo for articulo in self._articulos_comprados if articulo.identificador == identificador]
        for articulo in articulos_a_eliminar:
            self._articulos_comprados.remove(articulo)
            self.restar_puntos(articulo.puntos)
