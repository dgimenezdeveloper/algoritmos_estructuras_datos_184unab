import pickle
from pathlib import Path


class Nodo:
    def __init__(self, dato=None):
        self.dato = dato
        self.siguiente = None


class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def __iter__(self):
        self.actual = self.cabeza
        return self

    def __next__(self):
        if self.actual:
            profesor = self.actual.dato
            self.actual = self.actual.siguiente
            return profesor
        else:
            raise StopIteration


class Alumno:
    def __init__(self, nombre, nro_alumno, carrera, email, fecha_ingreso):
        self.nombre = nombre
        self.nro_alumno = nro_alumno
        self.carrera = carrera
        self.email = email
        self.fecha_ingreso = fecha_ingreso  
        self.materias_cursadas = [] 
        self.materias_aprobadas = []  
        self.profesores_unab = ListaEnlazada()  
    def cambiar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def cambiar_nro_alumno(self, nuevo_nro_alumno):
        self.nro_alumno = nuevo_nro_alumno

    def cambiar_carrera(self, nueva_carrera):
        self.carrera = nueva_carrera

    def cambiar_email(self, nuevo_email):
        self.email = nuevo_email

    def cambiar_fecha_ingreso(self, nueva_fecha_ingreso):
        self.fecha_ingreso = nueva_fecha_ingreso

    def recibir_mensaje(self, mensaje):
        print(f"Mensaje para {self.nombre}: {mensaje}")

    def asignar_materias(self, materia):
        self.materias_cursadas.append(materia)

    def mostrar_materias(self):
        print(f"Materias cursadas por {self.nombre}:")
        for materia in self.materias_cursadas:
            materia.mostrar_info_materia()

    def eliminar_materia(self, identificador):
        for materia in self.materias_cursadas:
            if materia.identificador == identificador:
                self.materias_cursadas.remove(materia)
                print(f"Materia con identificador {identificador} eliminada correctamente.")
                return
        print(f"No se encontró una materia con identificador {identificador}.")

    def cursa_materia(self, identificador):
        id_materias_cursadas = [materia.identificador for materia in self.materias_cursadas]
        #Busqueda binaria
        bajo, alto = 0, len(id_materias_cursadas) - 1
        while bajo <= alto:
            medio = (bajo + alto) // 2
            if id_materias_cursadas[medio] == identificador:
                return True
            elif id_materias_cursadas[medio] < identificador:
                bajo = medio + 1
            else:
                alto = medio - 1
        return False

    def aprobo_materia(self, identificador):
        bajo, alto = 0, len(self.materias_aprobadas) - 1
        while bajo <= alto:
            medio = (bajo + alto) // 2
            if self.materias_aprobadas[medio] == identificador:
                return "Materia Aprobada por el Alumno"
            elif self.materias_aprobadas[medio] < identificador:
                bajo = medio + 1
            else:
                alto = medio - 1
        raise ValueError("Materia NO Aprobada por el Alumno")

    def agregar_profesor_unab(self, profesor):
        self.profesores_unab.insertar(profesor)

    def obtener_profesores_unab(self):
        print(f"Profesores que ha tenido el alumno {self.nombre}:")
        for profesor in self.profesores_unab:
            print(f"Nombre: {profesor.nombre}, Edad: {profesor.edad}")

    def calcular_edad_promedio_profesores(self):
        total_edades = 0
        cantidad_profesores = 0
        for profesor in self.profesores_unab:
            total_edades += profesor.edad
            cantidad_profesores += 1

        if cantidad_profesores > 0:
            return total_edades / cantidad_profesores
        else:
            return 0

    def guardar_materias(self):
        archivo = Path.home() / "Documents" / "archivos" / "materias.dat"
        with open(archivo, 'wb') as f:
            pickle.dump(self.materias_aprobadas, f)
        print("Materias aprobadas guardadas correctamente.")

    def leer_materias(self):
        archivo = Path.home() / "Documents" / "archivos" / "materias.dat"
        with open(archivo, 'rb') as f:
            materias_aprobadas = pickle.load(f)
        print("Materias aprobadas:")
        for materia in materias_aprobadas:
            print(materia)


class Materias:
    def __init__(self, identificador, nombre, descripcion, carrera_anio):
        self.identificador = identificador
        self.nombre = nombre
        self.descripcion = descripcion
        self.carrera_anio = carrera_anio

    def cambiar_identificador(self, nuevo_identificador):
        if type(nuevo_identificador) == int and nuevo_identificador > 0:
            self.identificador = nuevo_identificador
        else:
            print("Error: El identificador debe ser un entero positivo.")

    def cambiar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def cambiar_descripcion(self, nueva_descripcion):
        self.descripcion = nueva_descripcion

    def agregar_carrera_anio(self, anio, carrera):
        self.carrera_anio.append((anio, carrera))

    def eliminar_carrera_anio(self, anio, carrera):
        if (anio, carrera) in self.carrera_anio:
            self.carrera_anio.remove((anio, carrera))
        else:
            print(f"No se encontró la combinación ({anio}, {carrera}) en la lista de carreras y años.")

    def mostrar_info_materia(self):
        print(f"Identificador: {self.identificador}")
        print(f"Nombre: {self.nombre}")
        print(f"Descripción: {self.descripcion}")
        print("Carreras y años donde se cursa:")
        for anio, carrera in self.carrera_anio:
            print(f"Año: {anio}, Carrera: {carrera}")
        print("\n")


class Profesor:
    def __init__(self, nombre, dni, edad):
        self.nombre = nombre
        self.dni = dni
        self.edad = edad

def main():

    profesor1 = Profesor("Juan Pérez", "23456789B", 40)
    profesor2 = Profesor("María González", "34567890C", 35)
    profesor3 = Profesor("Carlos Rodríguez", "45678901D", 50)

    materia1 = Materias(1, "Matemáticas", "Curso básico de matemáticas", [(2023, "Ingeniería")])
    materia2 = Materias(2, "Programación", "Introducción a la programación", [(2023, "Ingeniería")])

    alumno1 = Alumno("Ana Gómez", "20230001", "Ingeniería", "ana.gomez@example.com", "2023-01-01")

    alumno1.asignar_materias(materia1)
    alumno1.asignar_materias(materia2)

    alumno1.materias_aprobadas.append(1)

    alumno1.guardar_materias()

    alumno1.leer_materias()

    alumno1.agregar_profesor_unab(profesor1)
    alumno1.agregar_profesor_unab(profesor2)
    alumno1.agregar_profesor_unab(profesor3)

    alumno1.obtener_profesores_unab()

    edad_promedio = alumno1.calcular_edad_promedio_profesores()
    print(f"Edad promedio de los profesores: {edad_promedio:.2f}")

main()