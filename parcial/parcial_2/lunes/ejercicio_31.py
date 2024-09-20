""" Crear seis instancias de compradores, y agregarles (mediante el método comprar_articulo) diferentes cantidades de artículos. Nota: crear las instancias necesarias de artículos diferentes.
"""

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

articulo_1 = Articulos(10, "Mouse", "Inalambrico", "Logitech", 100, 10)
articulo_2 = Articulos(20, "Teclado", "Mecanico", "Razer", 150, 15)
articulo_3 = Articulos(13, "Monitor", "Curvo", "Samsung", 200, 20)
articulo_4 = Articulos(42, "Parlantes", "Bluetooth", "JBL", 250, 20)
articulo_5 = Articulos(15, "Auriculares", "Inalambricos", "Sony", 300, 30)
articulo_6 = Articulos(60, "Webcam", "Full HD", "Logitech", 350, 15)

comprador1 = Comprador("Juan", "Calle 123", "123456", "01/01/2000")
comprador1.comprar_articulos(articulo_2)
comprador1.comprar_articulos(articulo_6)
comprador2 = Comprador("Pedro", "Calle 456", "654321", "02/02/2000")
comprador2.comprar_articulos(articulo_1)
comprador2.comprar_articulos(articulo_4)
comprador2.comprar_articulos(articulo_5)
comprador3 = Comprador("Maria", "Calle 789", "789123", "03/03/2000")
comprador3.comprar_articulos(articulo_6)
comprador4 = Comprador("Ana", "Calle 987", "987321", "04/04/2000")
comprador4.comprar_articulos(articulo_1)
comprador4.comprar_articulos(articulo_2)