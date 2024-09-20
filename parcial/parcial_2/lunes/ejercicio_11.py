""" 1.1 - Crear una clase Comprador que contenga los datos básicos de una persona: nombre, dirección, teléfono, fecha de nacimiento y un campo puntaje que dependerá de las compras que realice. En el constructor, se deben inicializar todos los campos, y por defecto, el valor de puntaje será 0 (cero). Implementar los métodos para sumar o restar puntos del puntaje del comprador. """
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