import pickle
from pathlib import Path


class NodoLista:
    def __init__(self, dato=None):
        self.dato = dato
        self.siguiente = None


class ListaEnlazadaProfesores:
    def __init__(self):
        self.cabeza = None

    def insertar_profesor(self, profesor):
        nuevo_nodo = NodoLista(profesor)
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


class AlumnoUnab:
    def __init__(self, nombre, numero_alumno, carrera, correo, fecha_ingreso):
        self.nombre = nombre
        self.numero_alumno = numero_alumno
        self.carrera = carrera
        self.correo = correo
        self.fecha_ingreso = fecha_ingreso
        self.materias_cursadas = []
        self.materias_aprobadas = []
        self.profesores_unab = ListaEnlazadaProfesores()

    def cambiar_nombre_alumno(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def cambiar_numero_alumno(self, nuevo_numero):
        self.numero_alumno = nuevo_numero

    def cambiar_carrera(self, nueva_carrera):
        self.carrera = nueva_carrera

    def cambiar_correo(self, nuevo_correo):
        self.correo = nuevo_correo

    def cambiar_fecha_ingreso(self, nueva_fecha):
        self.fecha_ingreso = nueva_fecha

    def recibir_mensaje_alumno(self, mensaje):
        print(f"Mensaje para {self.nombre}: {mensaje}")

    def asignar_materia(self, materia):
        self.materias_cursadas.append(materia)

    def mostrar_materias_cursadas(self):
        print(f"Materias cursadas por {self.nombre}:")
        for materia in self.materias_cursadas:
            materia.mostrar_informacion_materia()

    def eliminar_materia_cursada(self, identificador):
        try:
            for materia in self.materias_cursadas:
                if materia.identificador == identificador:
                    self.materias_cursadas.remove(materia)
                    print(f"Materia con identificador {identificador} eliminada correctamente.")
                    return
            print(f"No se encontró una materia con identificador {identificador}.")
        except ValueError:
            print("Error al intentar eliminar la materia.")

    def cursa_materia(self, identificador):
        id_materias_cursadas = [materia.identificador for materia in self.materias_cursadas]
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

    def aprobar_materia(self, identificador):
        try:
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
        except ValueError as e:
            print(e)

    def agregar_profesor(self, profesor):
        self.profesores_unab.insertar_profesor(profesor)

    def obtener_profesores(self):
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

    def guardar_materias_aprobadas(self):
        try:
            archivo = Path.home() / "Documents" / "archivos" / "materias.dat"
            with open(archivo, 'wb') as f:
                pickle.dump(self.materias_aprobadas, f)
            print("Materias aprobadas guardadas correctamente.")
        except Exception as e:
            print(f"Error al guardar las materias aprobadas: {e}")

    def leer_materias_aprobadas(self):
        try:
            archivo = Path.home() / "Documents" / "archivos" / "materias.dat"
            with open(archivo, 'rb') as f:
                materias_aprobadas = pickle.load(f)
            print("Materias aprobadas:")
            for materia in materias_aprobadas:
                print(materia)
        except FileNotFoundError:
            print("No se encontró el archivo de materias aprobadas.")
        except Exception as e:
            print(f"Error al leer las materias aprobadas: {e}")


class Materia:
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

    def mostrar_informacion_materia(self):
        print(f"Identificador: {self.identificador}")
        print(f"Nombre: {self.nombre}")
        print(f"Descripción: {self.descripcion}")
        print("Carreras y años donde se cursa:")
        for anio, carrera in self.carrera_anio:
            print(f"Año: {anio}, Carrera: {carrera}")
        print("\n")


class ProfesorUnab:
    def __init__(self, nombre, dni, edad):
        self.nombre = nombre
        self.dni = dni
        self.edad = edad

# 1.5
# Si la clase Alumno estuviera dentro de un módulo llamado Alumos_Unab, necesitaríamos importar la clase
# con la instrucción "from Alumos_Unab import Alumno" en cualquier otro módulo o script donde queramos usar la clase Alumno.


def main():
    try:
        profesor1 = ProfesorUnab("Juan Pérez", "23456789B", 40)
        profesor2 = ProfesorUnab("María González", "34567890C", 35)
        profesor3 = ProfesorUnab("Carlos Rodríguez", "45678901D", 50)

        materia1 = Materia(1, "Matemáticas", "Curso básico de matemáticas", [(2023, "Ingeniería")])
        materia2 = Materia(2, "Programación", "Introducción a la programación", [(2023, "Ingeniería")])

        alumno1 = AlumnoUnab("Ana Gómez", "20230001", "Ingeniería", "ana.gomez@example.com", "2023-01-01")

        alumno1.asignar_materia(materia1)
        alumno1.asignar_materia(materia2)

        alumno1.materias_aprobadas.append(1)

        alumno1.guardar_materias_aprobadas()

        alumno1.leer_materias_aprobadas()

        alumno1.agregar_profesor(profesor1)
        alumno1.agregar_profesor(profesor2)
        alumno1.agregar_profesor(profesor3)

        alumno1.obtener_profesores()

        edad_promedio = alumno1.calcular_edad_promedio_profesores()
        print(f"Edad promedio de los profesores: {edad_promedio:.2f}")

    except Exception as e:
        print(f"Error: {e}")

main()
