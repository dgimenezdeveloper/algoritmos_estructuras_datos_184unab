from datetime import datetime, timedelta
import os
import random

# CLASE FECHA
class Fecha:
    def __init__(self, dd=None, mm=None, aaaa=None):
        if dd is None or mm is None or aaaa is None:
            hoy = datetime.now()
            self.dia = hoy.day
            self.mes = hoy.month
            self.anio = hoy.year
        else:
            self.dia = dd
            self.mes = mm
            self.anio = aaaa

    def __str__(self):
        return f"{self.dia:02d}/{self.mes:02d}/{self.anio}"

    def __add__(self, other):
        if isinstance(other, timedelta):
            nueva_fecha = datetime(self.anio, self.mes, self.dia) + other
            return Fecha(nueva_fecha.day, nueva_fecha.month, nueva_fecha.year)
        else:
            raise TypeError("Solo se puede sumar un objeto timedelta")

    def __eq__(self, other):
        return self.dia == other.dia and self.mes == other.mes and self.anio == other.anio

    def __lt__(self, other):
        fecha1 = datetime(self.anio, self.mes, self.dia)
        fecha2 = datetime(other.anio, other.mes, other.dia)
        return fecha1 < fecha2

    def calcular_dif_fecha(self, otra_fecha):
        fecha1 = datetime(self.anio, self.mes, self.dia)
        fecha2 = datetime(otra_fecha.anio, otra_fecha.mes, otra_fecha.dia)
        return abs((fecha2 - fecha1).days)

# CLASE ALUMNO
class Alumno(dict):
    def __init__(self, nombre, dni, fecha_ingreso, carrera):
        self["Nombre"] = nombre
        self["DNI"] = dni
        self["FechaIngreso"] = fecha_ingreso
        self["Carrera"] = carrera

    def __str__(self):
        return f"Nombre: {self['Nombre']}, DNI: {self['DNI']}, Fecha de Ingreso: {self['FechaIngreso']}, Carrera: {self['Carrera']}"

    def __eq__(self, other):
        return self["DNI"] == other["DNI"]

    def cambiar_datos(self, nombre=None, dni=None, fecha_ingreso=None, carrera=None):
        if nombre:
            self["Nombre"] = nombre
        if dni:
            self["DNI"] = dni
        if fecha_ingreso:
            self["FechaIngreso"] = fecha_ingreso
        if carrera:
            self["Carrera"] = carrera

    def antiguedad(self):
        hoy = Fecha()
        return hoy.calcular_dif_fecha(self["FechaIngreso"])

# CLASE NODO PARA LA LISTA DOBLEMENTE ENLAZADA
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class ListaDoblementeEnlazada:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def insertar_al_final(self, dato):
        nuevo = Nodo(dato)
        if self.primero is None:
            self.primero = self.ultimo = nuevo
        else:
            self.ultimo.siguiente = nuevo
            nuevo.anterior = self.ultimo
            self.ultimo = nuevo

    def __iter__(self):
        self.actual = self.primero
        return self

    def __next__(self):
        if self.actual:
            dato = self.actual.dato
            self.actual = self.actual.siguiente
            return dato
        else:
            raise StopIteration

    def lista_ejemplo(self, nombres, carreras, cantidad):
        for _ in range(cantidad):
            nombre = random.choice(nombres)
            dni = random.randint(10000000, 99999999)
            dia = random.randint(1, 28)
            mes = random.randint(1, 12)
            anio = random.randint(2000, 2023)
            fecha = Fecha(dia, mes, anio)
            carrera = random.choice(carreras)
            alumno = Alumno(nombre, dni, fecha, carrera)
            self.insertar_al_final(alumno)

    def ordenar_lista(self):
        alumnos = list(self)

        # USO ALGORITMO DE BURBUJA
        n = len(alumnos)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if alumnos[j]["FechaIngreso"] > alumnos[j + 1]["FechaIngreso"]:
                    alumnos[j], alumnos[j + 1] = alumnos[j + 1], alumnos[j]

        lista_ordenada = ListaDoblementeEnlazada()
        for alumno in alumnos:
            lista_ordenada.insertar_al_final(alumno)

        return lista_ordenada

def manejar_archivos_directorios(lista):
    try:
        # Cre0 directorio
        directorio = "ingresos_alumnos"
        os.mkdir(directorio)

        # Guardo lista de alumnos en un archivo
        archivo = os.path.join(directorio, "lista_alumnos.txt")
        with open(archivo, "w") as f:
            for alumno in lista:
                f.write(str(alumno) + "\n")

        # Muevo directorio a nueva ruta
        nueva_ruta = "nuevo_directorio_movido"
        os.rename(directorio, nueva_ruta)

        # Borro archivo y directorio
        os.remove(os.path.join(nueva_ruta, "lista_alumnos.txt"))
        os.rmdir(nueva_ruta)
    except Exception as e:
        print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    nombres = ["Juan", "Pedro", "Maria", "Lucia", "Dario", "Jose", "Ana", "Laura"]
    carreras = ["Ingenieria", "Medicina", "Tec Univ en Programacion", "Arquitectura", "Economia", "Contabilidad"]
    
    lista = ListaDoblementeEnlazada()
    lista.lista_ejemplo(nombres, carreras, 10)

    print("Lista original:")
    for alumno in lista:
        print(alumno)

    lista_ordenada = lista.ordenar_lista()

    print("\nLista ordenada por fecha de ingreso:")
    for alumno in lista_ordenada:
        print(alumno)

    manejar_archivos_directorios(lista_ordenada)
