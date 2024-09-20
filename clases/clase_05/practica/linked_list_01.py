class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class LinkedList:
    def __init__(self):
        self.cabeza = None
        self.len = 0

    def insertar(self, nuevo_nodo):
        # cabeza => John => None
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            # cabeza => John => Ben => None
            temporal = self.cabeza
            while temporal.siguiente is not None:
                temporal = temporal.siguiente
            temporal.siguiente = nuevo_nodo
            self.len += 1
            print(f"Se ha agregado el nodo {nuevo_nodo} al final de la lista. Y el siguiente apunta a {nuevo_nodo.siguiente}")
    
    def imprimir_lista(self):
        print("Imprimiendo lista enlazada:")
        nodos = []
        actual = self.cabeza
        while actual is not None:
            nodos.append(str(actual.dato))
            actual = actual.siguiente
        print("--> ".join(nodos))

# Node => data, next
# fist_node.dato => "John", first_node.siguiente => None
first_node = Nodo("John")
lista_enlazada = LinkedList()
lista_enlazada.insertar(first_node)
second_node = Nodo("Ben")
lista_enlazada.insertar(second_node)
third_node = Nodo("Matthew")