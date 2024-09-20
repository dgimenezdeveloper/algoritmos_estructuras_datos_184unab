""" 2do PARCIAL - Algoritmos y Estructuras de datos - MIERCOLES 26 - JUNIO - 2024
Modalidad:
El parcial estará habilitado para su resolución desde: Miercoles 26/06 @ 18:00hs, hasta: Jueves 27/06 @ 01:45hs. (pueden elegir cuando comenzar el intento)

Tienen 1 (uno) sólo intento para resolver la actividad; el tiempo máximo es 4 (cuatro) horas.

El tiempo será contabilizado desde el momento que aceptan realizar la actividad en Github Classroom, y cualquier "commit" realizado luego de 4 horas no será aceptado como parte del intento de resolución!!

Los resultados sólo será visibles luego de que la actividad cierre.

NOTA: TODOS LOS EJERCICIOS DEBEN SER REALIZADOS EN UN SOLO ARCHIVO.PY, O SEA LOS MÉTODOS QUE SE VAN AGREGANDO , DEBEN ESTAR EN SUS CORRESPONDIENTES CLASES EN EL ARCHIVO EJERCICIO1.PY LOS ARCHIVOS RESTANTES QUEDAN POR SI NECESITAN BORRADORES, PERO SOLO MIRAMOS EL PRIMER ARCHIVO

Ejercicios:
Ejercicio 1:
Definir una clase Fecha. Formato: (dd, mm, aaaa).

La clase debe contener métodos para facilitar:

calcular_dif_fecha(): Calcular la distancia entre dos fechas.
Sobrecarga de métodos:

__str__
__add__
__eq__
Importante:

Cuando creamos (instanciamos) una Fecha, si es llamada sin parámetros, por defecto contendra la "fecha de hoy".

Pueden agregar más atributos y métodos, si lo consideran necesario.

Ejercicio 2:
Definir una clase Alumno como un diccionario, el cual contiene los datos:


{ "Nombre" : 'string',
  "DNI" : 'integer' ,
  "FechaIngreso" : 'Fecha',
  "Carrera" : 'cualquier tipo' }
La clase debe contener métodos para facilitar:

Cambiar uno o varios datos del Alumno.
antiguedad():Calcular la hace cuánto tiempo que el alumno esta inscripto en la carrera.
Sobrecarga de métodos:

__str__
__eq__
Importante:

Un Alumno puede estar inscripto en sólo una carrera.
Pueden agregar más atributos y métodos, si lo consideran necesario.
Ejercicio 3:
Crear una clase ListaDoblementeEnlazada cuyos nodos contengan como dato objetos del tipo Alumno. Implementar un Iterador para la lista enlazada (será útil en el siguiente ejercicio). La lista tendrá un método lista_ejemplo() el cual retorna un lista doblemente enlazada de alumnos cargada con datos aleatorios (random).

Importante:

Pueden agregar más atributos y métodos, si lo consideran necesario.
Ejercicio 4:
Implementar una función que permita ordenar la Lista Doblemente Enlazada "de Alumnos" (ejer. anterior). Pueden utilizar cualquier método de ordenación, pero deben implentarlo (no pueden usar el método sort de Python).

El criterio de ordenación es: Fecha de Ingreso

Importante:

No usar el método sort de Python.
Pueden agregar más atributos y funciones/métodos, si lo consideran necesario.
Ejercicio 5:
Se debe crear un directorio en el cual guardaremos en un archivo una "lista de alumnos". Luego, deberán mover el directorio a una nueva ruta (path). Finalmente deben borrar el nuevo archivo y el nuevo directorio. NO útilizar el módulo shutil (pueden usa el módulo os).

En resumen: crear directorio; guardar en un archivo una "lista de alumnos"; mover el directorio; borrar archivo y directorio.

Importante:

NO USAR shutil
Recodar el manejo de excepciones, si las hay.
Pueden agregar más atributos y funciones/métodos, si lo consideran necesario. """

import random
from datetime import datetime, timedelta
import os

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

    # sobre carga de operador menor que para posterior uso en el ordenamiento
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
            self.insertar_al_final(Alumno(nombre, dni, fecha, carrera))

    def ordenar_lista(self):
        alumnos = list(self)

        # uSO ALGORITMO DE BURBUJA
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
        # Crea directorio
        directorio = "ingresos_alumnos"
        os.mkdir(directorio)

        # Guarda lista de alumnos en un archivo
        archivo = os.path.join(directorio, "lista_alumnos.txt")
        with open(archivo, "w") as f:
            for alumno in lista:
                f.write(str(alumno) + "\n")

        # Mueve directorio a una nueva ruta
        nueva_ruta = "nuevo_directorio_moved"
        os.rename(directorio, nueva_ruta)

        # Borrar archivo y directorio
        os.remove(os.path.join(nueva_ruta, "lista_alumnos.txt"))
        os.rmdir(nueva_ruta)
    except Exception as e:
        print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    nombres = ["Juan", "Pedro", "Maria", "Lucia", "Dario", "Jose", "Ana", "Laura"]
    carreras = ["Ingenieria", "Medicina", "Tec Univ en Programacion", "Arquitectura", "Economia", "Contabilidad"]

    # Crear una lista doblemente enlazada y cargarla con datos aleatorios
    lista = ListaDoblementeEnlazada()
    lista.lista_ejemplo(nombres, carreras, 10)

    print("Lista original:")
    for alumno in lista:
        print(alumno)

    # Ordenar la lista por fecha de ingreso
    lista_ordenada = lista.ordenar_lista()

    print("\nLista ordenada por fecha de ingreso:")
    for alumno in lista_ordenada:
        print(alumno)

    # Crear directorio
    directorio = "/tmp/ingresos_alumnos"
    os.mkdir(directorio)

    # Guardar lista de alumnos en un archivo
    archivo = os.path.join(directorio, "lista_alumnos.txt")
    with open(archivo, "w") as f:
        for alumno in lista:
            f.write(str(alumno) + "\n")

    # Mover directorio a una nueva ruta
    nueva_ruta = "/tmp/nueva_ruta"
    os.rename(directorio, nueva_ruta)

    # Borrar archivo y directorio
    os.remove(os.path.join(nueva_ruta, "lista_alumnos.txt"))
    os.rmdir(nueva_ruta)