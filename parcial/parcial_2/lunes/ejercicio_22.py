""" Agregar a la clase Comprador un método encontrar_articulo que reciba el identificador del artículo y devuelva True o False de acuerdo a si el artículo está o no en la lista del comprador. Utilizar el método de búsqueda lineal. """

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