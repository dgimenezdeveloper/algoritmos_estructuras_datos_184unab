class Nodo(object):
    def __init__(self, dato=None, proximo=None):
        self.dato = dato
        self.proximo = proximo

    def __str__(self):
        return str(self.dato)
    
class ListaEnlazada(object):
    def __init__(self):
        self.primero = None
        self.len = 0

    def __len__(self):
        return self.len

    def __str__(self):
        lista = []
        actual = self.primero
        while actual:
            lista.append(str(actual))
            actual = actual.proximo
        return ' - '.join(lista)

    def insertar(self, dato, i=None):
        if i is None:
            i = self.len
        if i < 0 or i > self.len:
            raise IndexError('Índice fuera de rango')
        nuevo = Nodo(dato)
        if i == 0:
            nuevo.proximo = self.primero
            self.primero = nuevo
        else:
            anterior = self.primero
            for pos in range(1, i):
                anterior = anterior.proximo
            nuevo.proximo = anterior.proximo
            anterior.proximo = nuevo
        self.len += 1

    def eliminar(self, i):
        if i < 0 or i >= self.len:
            raise IndexError('Índice fuera de rango')
        if i == 0:
            self.primero = self.primero.proximo
        else:
            anterior = self.primero
            for pos in range(1, i):
                anterior = anterior.proximo
            anterior.proximo = anterior.proximo.proximo
        self.len -= 1

    def __getitem__(self, i):
        if i < 0 or i >= self.len:
            raise IndexError('Índice fuera de rango')
        actual = self.primero
        for pos in range(i):
            actual = actual.proximo
        return actual.dato

    def __setitem__(self, i, dato):
        if i < 0 or i >= self.len:
            raise IndexError('Índice fuera de rango')
        actual = self.primero
        for pos in range(i):
            actual = actual.proximo
        actual.dato = dato

    def __iter__(self):
        """ Devuelve un iterador de la lista."""
        self.actual = self.primero
        return self

    def __next__(self):
        if self.actual is None:
            raise StopIteration()
        dato = self.actual.dato
        self.actual = self.actual.proximo
        return dato

    def __contains__(self, dato):
        actual = self.primero
        while actual:
            if actual.dato == dato:
                return True
            actual = actual.proximo