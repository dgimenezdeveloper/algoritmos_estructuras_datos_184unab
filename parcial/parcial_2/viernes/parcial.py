""" 'EXAMEN COMISIÓN 7 UNAB SOBRE ALGORITMOS Y ESTRUCTURAS DE DATOS
MODALIDAD: Tienen 1 (un) solo intento para resolver la actividad, el tiempo máximo es de 4 (cuatro) horas. El tiempo cuenta desde el
momento en que acepten realizar la tarea en Github Classroom y cualquier "commit" realizado luego de 4 (cuatro) horas, no será aceptado
como parte del intento de resolución.
#EJERCICIO 1 Una nueva Sucursal del Banco ILBA tiene 3 nuevos clientes, los cuales pueden hacer depósitos y extracciones. También, esta
sucursal necesita que al final del día calcule la cantidad de dinero que hay depositado. Identificar las clases Cliente y la clase Banco. Definir los
atributos y los métodos de cada clase Realizar un menú de consultas para cada operación
#EJERCICIO 2 Debes desarrollar una aplicación para administrar el inventario de una cadena de tiendas de electrónica. Cada local tiene su
propio inventario de productos, identificados por un código único. Cuando un cliente solicita un producto, se debe buscar su código en el
inventario de la tienda correspondiente para verificar si está disponible. Hay que implementar un algoritmo de búsqueda lineal para encontrar
un código de producto específico en el inventario de cada tienda. El programa debe: Permitir al usuario ingresar el código del producto que
está buscando. Permitir al usuario seleccionar la tienda en la que desea buscar el producto. Recorrer el inventario de la tienda seleccionada de
forma secuencial hasta encontrar el código solicitado. Informar al usuario si el producto está disponible o no en el inventario de la tienda.
#EJERCICIO 3 Crear y cargar en un lista los nombres de 5 países y en otra lista paralela la cantidad de habitantes del mismo. Ordenar
alfabéticamente e imprimir los resultados. Por último ordenar con respecto a la cantidad de habitantes (de mayor a menor) e imprimir
nuevamente.Importante: Utilizar algoritmo de ordenamiento no funciónes de Python
#EJERCICIO 4 Te piden desarrollar un sistema de gestión de contactos para una empresa. Cada contacto tiene un nombre, un número de
teléfono y una dirección de correo. Necesitas implementar una estructura de datos que te permita almacenar y manipular eficientemente esta
información. Tu tarea es escribir un programa que utilice una lista enlazada para implementar las siguientes funcionalidades: Agregar un nuevo
contacto a la lista. Buscar un contacto por su nombre. Eliminar un contacto de la lista. Mostrar todos los contactos en la lista.
"""
class Cliente:
    def __init__(self, nombre, saldo=0):
        self.nombre = nombre
        self.saldo = saldo

    def depositar(self, cantidad):
        self.saldo += cantidad

    def extraer(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
        else:
            print("Fondos insuficientes")

    def obtener_saldo(self):
        return self.saldo

class Banco:
    def __init__(self):
        self.clientes = []

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)

    def calcular_total_depositado(self):
        total = sum(cliente.obtener_saldo() for cliente in self.clientes)
        return total

    def mostrar_menu(self):
        while True:
            print("\n1. Depositar\n2. Extraer\n3. Ver total depositado\n4. Salir")
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                nombre = input("Nombre del cliente: ")
                cantidad = float(input("Cantidad a depositar: "))
                encontrado = False
                for cliente in self.clientes:
                    if cliente.nombre == nombre:
                        cliente.depositar(cantidad)
                        encontrado = True
                        print(f"Depósito realizado. Saldo actual: {cliente.obtener_saldo()}")
                if not encontrado:
                    print("Cliente no encontrado.")
            elif opcion == "2":
                nombre = input("Nombre del cliente: ")
                cantidad = float(input("Cantidad a extraer: "))
                encontrado = False
                for cliente in self.clientes:
                    if cliente.nombre == nombre:
                        cliente.extraer(cantidad)
                        encontrado = True
                        print(f"Extracción realizada. Saldo actual: {cliente.obtener_saldo()}")
                if not encontrado:
                    print("Cliente no encontrado.")
            elif opcion == "3":
                print(f"Total depositado en el banco: {self.calcular_total_depositado()}")
            elif opcion == "4":
                break
            else:
                print("Opción no válida.")

def administrar_inventario(inventario):

    
    def buscar_producto(codigo, productos):
        for producto in productos:
            if producto == codigo:
                return True
        return False

    codigo_producto = input("Ingrese el código del producto que está buscando: ")


    print("Seleccione la tienda en la que desea buscar el producto:")
    for tienda in inventario.keys():
        print(tienda)
    tienda_seleccionada = input()

    if tienda_seleccionada in inventario:
        producto_encontrado = buscar_producto(codigo_producto, inventario[tienda_seleccionada])
        if producto_encontrado:
            print("El producto está disponible en el inventario de la tienda.")
        else:
            print("El producto no está disponible en el inventario de la tienda.")
    else:
        print("La tienda seleccionada no existe.")



inventario_sucursal = {
    "sucursal1": ["producto1", "producto2", "producto3"],
    "sucursal2": ["producto4", "producto5", "producto6"],
    "sucursal3": ["producto7", "producto8", "producto9"]
}

administrar_inventario(inventario_sucursal)


def ordenar_paises_habitantes(paises, habitantes):

    for i in range(len(paises)-1):
        for j in range(0, len(paises)-i-1):
            if paises[j] > paises[j+1]:

                paises[j], paises[j+1] = paises[j+1], paises[j]

                habitantes[j], habitantes[j+1] = habitantes[j+1], habitantes[j]


    print("Orden alfabético:")
    for i in range(len(paises)):
        print(f"{paises[i]}: {habitantes[i]}")


    for i in range(len(habitantes)-1):
        for j in range(0, len(habitantes)-i-1):
            if habitantes[j] < habitantes[j+1]:

                habitantes[j], habitantes[j+1] = habitantes[j+1], habitantes[j]
                paises[j], paises[j+1] = paises[j+1], paises[j]


    print("\nOrden por cantidad de habitantes (de mayor a menor):")
    for i in range(len(paises)):
        print(f"{paises[i]}: {habitantes[i]}")


paises_ejemplo = ["Argentina", "Brasil", "Chile", "Perú", "Colombia"]
habitantes_ejemplo = [45195777, 212559417, 19116201, 32971854, 50882891]
ordenar_paises_habitantes(paises_ejemplo, habitantes_ejemplo)


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


lista_contactos = ListaEnlazada()
lista_contactos.agregar_contacto("Juan Pérez", "123456789", "juan@example.com")
lista_contactos.agregar_contacto("Ana López", "987654321", "ana@example.com")
lista_contactos.mostrar_contactos()