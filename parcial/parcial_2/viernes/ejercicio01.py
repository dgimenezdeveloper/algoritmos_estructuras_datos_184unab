""" #EJERCICIO 1 Una nueva Sucursal del Banco ILBA tiene 3 nuevos clientes, los cuales pueden hacer depósitos y extracciones. También, esta
sucursal necesita que al final del día calcule la cantidad de dinero que hay depositado. Identificar las clases Cliente y la clase Banco. Definir los
atributos y los métodos de cada clase Realizar un menú de consultas para cada operació """

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

#ejemplo de uso ejer1
banco = Banco()
cliente1 = Cliente("Juan", 1000)
cliente2 = Cliente("Ana", 2000)
cliente3 = Cliente("Pedro", 3000)
banco.agregar_cliente(cliente1)
banco.agregar_cliente(cliente2)
banco.agregar_cliente(cliente3)
banco.mostrar_menu()

