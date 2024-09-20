class Nodo:
    def __init__(self, valor=None):  # Creación de Nodo
        self.valor = valor
        self.siguiente = None
    
    def __str__(self):  # Método para imprimir el valor del nodo
        return str(self.valor)

class LinkedList:  # Creación de la clase LinkedList
    def __init__(self):
        self.cabeza = None  # Se inicializa la lista con la cabeza vacía
        self.len = 0  # Se inicializa la lista con longitud 0
    
    def append(self, valor):  # Método para agregar un nodo al final de la lista
        nuevo_nodo = Nodo(valor)  # Se crea un nuevo nodo
        if self.cabeza is None:
            self.cabeza = nuevo_nodo  # Si la lista está vacía, el nuevo nodo será la cabeza
        else:
            ultimo = self.cabeza  # Si la lista no está vacía, se recorre hasta el último nodo
            while ultimo.siguiente:  # Se recorre la lista hasta llegar al último nodo
                ultimo = ultimo.siguiente  # Se recorre la lista hasta llegar al último nodo
            ultimo.siguiente = nuevo_nodo  # Se agrega el nuevo nodo al final de la lista
        self.len += 1  # Se incrementa la longitud de la lista
    
    def pop(self, indice=None):  # Método para eliminar un nodo de la lista
        if indice is None:  # Si no se especifica el índice, se elimina el último nodo
            indice = self.len - 1
        if indice < 0 or indice >= self.len:
            raise IndexError("Índice fuera de rango")
        if indice == 0:  # Si el índice es 0, se elimina el primer nodo
            eliminado = self.cabeza
            self.cabeza = self.cabeza.siguiente
        else:  # Si el índice no es 0, se recorre la lista hasta llegar al nodo anterior al que se quiere eliminar
            nodo_anterior = self.cabeza  # Se inicializa el nodo anterior en la cabeza
            nodo_actual = self.cabeza.siguiente  # Se inicializa el nodo actual en el siguiente de la cabeza
            for i in range(1, indice): 
                nodo_anterior = nodo_anterior.siguiente  # nodo_anterior se mueve al siguiente nodo
                nodo_actual = nodo_actual.siguiente  # nodo_actual se mueve al siguiente nodo
            eliminado = nodo_actual  # Se guarda el nodo a eliminar
            nodo_anterior.siguiente = nodo_actual.siguiente  # Se elimina el nodo actual
        self.len -= 1  # Se reduce la longitud de la lista
        return eliminado  # Se retorna el nodo eliminado
    
    def remove(self, valor):
        if self.len == 0:  # Si la lista está vacía, se levanta un error
            raise ValueError("Lista vacía")
        if self.cabeza.valor == valor:  # Si el valor a eliminar es el primero, se elimina
            self.cabeza = self.cabeza.siguiente
            self.len -= 1
            return
        nodo_anterior = self.cabeza
        nodo_actual = self.cabeza.siguiente
        while nodo_actual is not None and nodo_actual.valor != valor: 
            nodo_anterior = nodo_anterior.siguiente
            nodo_actual = nodo_actual.siguiente
        if nodo_actual is None:  # Si el valor no se encuentra, se levanta un error
            raise ValueError("Valor no encontrado")
        else:
            nodo_anterior.siguiente = nodo_actual.siguiente  # Si el valor se encuentra, se elimina
            self.len -= 1 
    
    def insert(self, indice, valor):
        if (indice < 0) or (indice > self.len):  # Si el índice no es válido, se levanta un error
            raise ValueError("Índice no válido")
        nuevo_nodo = Nodo(valor)  # Se crea un nuevo nodo
        if indice == 0:  # Si el índice es 0, se inserta al principio
            nuevo_nodo.siguiente = self.cabeza  # El nuevo nodo apunta a la cabeza
            self.cabeza = nuevo_nodo  # La cabeza se actualiza
        else:  # Si el índice no es 0, se recorre la lista hasta llegar al nodo anterior al que se quiere insertar
            nodo_anterior = self.cabeza
            for i in range(indice - 1):
                nodo_anterior = nodo_anterior.siguiente
            nuevo_nodo.siguiente = nodo_anterior.siguiente
            nodo_anterior.siguiente = nuevo_nodo
        self.len += 1  # Se incrementa la longitud de la lista
    
    def __iter__(self): # Método para iterar sobre la lista
        self.nodo_actual = self.cabeza
        return self
    
    def __next__(self):
        if self.nodo_actual is not None: # Si el nodo actual no es None, se retorna el nodo actual y se avanza al siguiente
            nodo = self.nodo_actual
            self.nodo_actual = self.nodo_actual.siguiente
            return nodo
        else:
            raise StopIteration

# Ejemplo de uso
lista = LinkedList()
lista.append(1)
lista.append(2)
lista.append(3)
lista.append(4)
lista.append(5)
print("Lista original:")
for nodo in lista:
    print(nodo)
print("Lista después de eliminar el nodo en la posición 2:")
lista.pop(2)
for nodo in lista:
    print(nodo)
print("Lista después de eliminar el nodo con valor 1:")
lista.remove(1)
for nodo in lista:
    print(nodo)
print("Lista después de insertar el valor 10 en la posición 2:")
lista.insert(2, 10)
for nodo in lista:
    print(nodo)
print("Lista después de insertar el valor 0 al principio:")
lista.insert(0, 0)
for nodo in lista:
    print(nodo)
print("Lista después de insertar el valor 100 al final:")
lista.insert(100, 100)
for nodo in lista:
    print(nodo)
print("Lista después de eliminar el último nodo:")
lista.pop()
for nodo in lista:
    print(nodo)
print("Lista después de eliminar el primer nodo:")
lista.pop(0)
for nodo in lista:
    print(nodo)