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


""" Crear una lista con estos compradores """
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

compradores = [comprador1, comprador2, comprador3, comprador4]


""" Utilizar el método de ordenamiento burbuja para ordenarlos de forma DESCENDENTE (de mayor valor a menor valor) de acuerdo al puntaje de cada uno. """

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

compradores = [comprador1, comprador2, comprador3, comprador4]

def ordenar_compradores(compradores):
    n = len(compradores)
    for i in range(n):
        for j in range(0, n-i-1):
            if compradores[j].puntaje < compradores[j+1].puntaje:
                compradores[j], compradores[j+1] = compradores[j+1], compradores[j]

ordenar_compradores(compradores)


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

""" Escribir una función que reciba la lista de compradores creada en el punto 3.2 y genere archivos de texto con extensión .csv cuyo (usar los metodos de la libreria pathlib y os para verificar y crear directorios de ser necesario) nombre sea el nombre del comprador y que contenga la lista de artículos correspondientes, un artículo en cada línea.
 """
import os, pathlib
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


def generar_archivos_compradores(compradores, dir="compradores_csv"):
    pathlib.Path(dir).mkdir(parents=True, exist_ok=True)
    
    for comprador in compradores:
        ruta = os.path.join(dir, f"{comprador.nombre}.csv")
        with open(ruta, "w") as archivo:
            for articulo_str in comprador.lista_a_string().split(','):
                archivo.write(f"{articulo_str}\n")

generar_archivos_compradores(compradores)