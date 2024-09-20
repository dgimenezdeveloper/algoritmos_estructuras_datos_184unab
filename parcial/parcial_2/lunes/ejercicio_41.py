""" Agregar a la clase Comprador un método lista_a_string que devuelva una lista de strings con los atributos de los artículos comprados [identificador, nombre, marca, precio, puntos] separador por puntos y comas (ej: [1;”computadora”;”del”; 100.00;30,5;”mouse”;”logitech”;200.00;15]) """
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
    
    # Se agrega el método lista_a_string
    def lista_a_string(self):
        articulos_str = []
        for articulo in self._articulos_comprados:
            articulos_str.append(f"{articulo.identificador};{articulo.nombre};{articulo.marca};{articulo.precio};{articulo.puntos}") #Hago uso de f-string por cuestiones de legibilidad
        return ",".join(articulos_str)

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

compradores = [comprador1, comprador2, comprador3, comprador4]

def ordenar_compradores(compradores):
    n = len(compradores)
    for i in range(n):
        for j in range(0, n-i-1):
            if compradores[j].puntaje < compradores[j+1].puntaje:
                compradores[j], compradores[j+1] = compradores[j+1], compradores[j]

ordenar_compradores(compradores)

