""" Te piden desarrollar un sistema de gestión de contactos para una empresa. Cada contacto tiene un nombre, un número de
teléfono y una dirección de correo. Necesitas implementar una estructura de datos que te permita almacenar y manipular eficientemente esta
información. Tu tarea es escribir un programa que utilice una lista enlazada para implementar las siguientes funcionalidades: Agregar un nuevo
contacto a la lista. Buscar un contacto por su nombre. Eliminar un contacto de la lista. Mostrar todos los contactos en la lista. """

class Nodo:
    def __init__(self, nombre, telefono, correo):
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar_contacto(self, nombre, telefono, correo):
        nuevo_contacto = Nodo(nombre, telefono, correo)
        if not self.cabeza:
            self.cabeza = nuevo_contacto
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_contacto

    def buscar_contacto(self, nombre):
        actual = self.cabeza
        while actual:
            if actual.nombre == nombre:
                return actual
            actual = actual.siguiente
        return None

    def eliminar_contacto(self, nombre):
        actual = self.cabeza
        anterior = None
        while actual:
            if actual.nombre == nombre:
                if anterior:
                    anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
                return True
            anterior = actual
            actual = actual.siguiente
        return False

    def mostrar_contactos(self):
        actual = self.cabeza
        while actual:
            print(f"Nombre: {actual.nombre}, Teléfono: {actual.telefono}, Correo: {actual.correo}")
            actual = actual.siguiente

#Ejemplo de uso ejer4

lista_contactos = ListaEnlazada()
lista_contactos.agregar_contacto("Juan Pérez", "123456789", "juan@example.com")
lista_contactos.agregar_contacto("Ana López", "987654321", "ana@example.com")
lista_contactos.mostrar_contactos()