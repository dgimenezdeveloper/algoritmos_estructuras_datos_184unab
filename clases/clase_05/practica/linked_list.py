class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
    
    def __str__(self):
        return str(self.dato)

class LinkedList:
    def __init__(self):
        self.cabeza = None
        self.len = 0
    
    def __len__(self):
        len = 0
        if self.cabeza is None:
            return len
        else:
            temporal = self.cabeza
            while temporal is not None:
                len += 1
                temporal = temporal.siguiente
        return len
    
    def __str__(self):
        print("Imprimiendo lista enlazada:")
        nodos = []
        actual = self.cabeza
        while actual is not None:
            nodos.append(str(actual.dato))
            actual = actual.siguiente
        return "--> ".join(nodos)
    
    def agregar_al_inicio(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo
        self.len += 1
        print(f"Se ha agregado el nodo {nuevo_nodo} al inicio de la lista. Y el siguiente apunta a {nuevo_nodo.siguiente}")
    
    def agregar_en_posicion(self, dato):
        self.posicion = 0
        self.dato = dato
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            temporal = self.cabeza
            while temporal.siguiente:
                temporal = temporal.siguiente
                self.posicion += 1
            temporal.siguiente = nuevo_nodo
            self.len += 1
            print(f"Se ha agregado el nodo {nuevo_nodo} en la posición {self.posicion} de la lista. Y el siguiente apunta a {nuevo_nodo.siguiente}")
    
    def agregar_al_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            temporal = self.cabeza
            while temporal.siguiente is not None:
                temporal = temporal.siguiente
            temporal.siguiente = nuevo_nodo
            self.len += 1
            print(f"Se ha agregado el nodo {nuevo_nodo} al final de la lista. Y el siguiente apunta a {nuevo_nodo.siguiente}")
    
    def obtener_cabeza(self):
        return self.cabeza
    
    def obtener_cola(self):
        temporal = self.cabeza
        while temporal.siguiente:
            temporal = temporal.siguiente
        return temporal

    def existe(self, dato):
        temporal = self.cabeza
        while temporal:
            if temporal.dato == dato:
                return True
            temporal = temporal.siguiente
        return False
    
    def invertir(self):
        previo = None
        actual = self.cabeza
        while actual:
            proximo = actual.siguiente
            actual.siguiente = previo
            previo = actual
            actual = proximo
        self.cabeza = previo
    
    def eliminar_duplicados(self):
        temporal = self.cabeza
        while temporal:
            actual = temporal
            while actual.siguiente:
                if temporal.dato == actual.siguiente.dato:
                    actual.siguiente = actual.siguiente.siguiente
                else:
                    actual = actual.siguiente
            temporal = temporal.siguiente

my_list = LinkedList()
my_list.agregar_al_inicio(21)
my_list.agregar_al_inicio(22)
my_list.agregar_al_final(1)
print(len(my_list)) # 3
print(my_list) # 22 --> 21 --> 1
print(my_list.obtener_cabeaza()) # 22
print(my_list.obtener_cola()) # 1
print(my_list.existe(21))   # True
print(my_list.existe(20))     # False
dicc = {"nombre": "Juan", "edad": 30, "ciudad": "Bogotá"}
my_list.agregar_al_inicio(dicc)
print(my_list) # {'nombre': 'Juan', 'edad': 30, 'ciudad': 'Bogotá'} --> 22 --> 21 --> 1

