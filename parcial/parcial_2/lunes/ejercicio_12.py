""" 1.2 - Crear una clase Artículos que contenga los campos identificador (tipo entero positivo), nombre, descripción, marca, precio (float) y puntos. En el constructor se deben establecer todos estos datos. Crear los métodos necesarios para modificar estos valores. IMPORTANTE: los puntos no pueden ser negativos.
"""
class Articulos:
    def __init__(self, identificador, nombre, descripcion, marca, precio, puntos):
        self.identificador = identificador
        self.nombre = nombre
        self.descripcion = descripcion
        self.marca = marca
        self.precio = precio
        self.puntos = puntos if puntos >= 0 else 0
    
    def modificar_nombre(self, nombre):
        self.nombre = nombre
    
    def modificar_descripcion(self, descripcion):
        self.descripcion = descripcion

    def modificar_marca(self, marca):
        self.marca = marca
    
    def modificar_precio(self, nuevo_precio):
        self.precio = nuevo_precio
    
    def modificar_puntos(self, nuevos_puntos):
        self.puntos = nuevos_puntos if nuevos_puntos >= 0 else 0