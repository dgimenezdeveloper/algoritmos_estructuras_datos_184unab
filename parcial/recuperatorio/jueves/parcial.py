""" 
Ejercicio 1)
1.1)
Crear una clase Alumno, está contendrá los datos básicos de un Alumno de la facultad  : nombre, Nro de Alumno,  carrera,  email y fecha de ingreso a la facultad, además de los métodos necesarios para cambiar estos datos. Además el usuario tendrá un método especial para "recibir mensajes" e imprimirlos.
1.2)
- Modelar la clase Materias que contendrá los campos identificador (tipo entero positivo), nombre, descripción, carrera en que se cursa (solo un string)). En el constructor se deben establecer todos estos datos. Crear los métodos necesarios para modificar estos valores. 
1.3)
Ahora Modificar al atributo de clase que hace referencia a "Carrera en que se cursa"
para que ese dato almacenado sea en vez de un único string como se definió en el punto 1.1, una  lista  sea una lista tipo combinación, del año/carrera donde se curse la materia 
1.4)
Agregar a la Clase Materias un método mostrar_info_materia()  que imprima toda la información relacionada con la materia, incluida los años y materias donde se cursa
 1.5)
Explicar brevemente cuál sería el cambio necesario  en la implementación, para poder utilizarla, si la clase Alumno estuviera dentro de un módulo llamado Alumos_Unab.

Ejercicio 2)
2.1 ) Agregar a la clase Alumno atributos y métodos para  Asignar  materias (el método debe llamarse asignar_materias) que permita instanciar y  asignar materias  a una lista de materias a cursar dentro de la clase Alumno. 

2.2 ) Agregar a la clase Alumno un método cursa_materia que reciba el identificador de la materia  y devuelva True o False de acuerdo a si la materia  está o no en la lista del Alumno. Para tal búsqueda, utilizar el método de búsqueda binaria.

2.3 - Agregar a la clase Alumno  un método eliminar materia que reciba el identificador de la materia y elimine las instancias de la materias asignadas en la lista del Alumno.

2.4 )
Agregar a la clase Alumno, una lista de materias aprobados que sólo contenga el identificador (int) de materias aprobadas, en una simple lista
Implementar en la clase Alumno, un método llamado aprobo_materia,  el cual realiza una búsqueda binaria  en la lista antes mencionada. El método devolverá un string  "Materia Aprobada  Por el Alumno" si el identificador recibido por ese método como parámetro está en la lista de materias aprobadas. En caso de no encontrarlo, levantará una excepción con el comando RAISE, indicando "Materia NO Aprobada  Por el Alumno"

Ejercicio 3)
3.1) Modelar la Clase Profesores
Esta clase representará un Profesor, con sus propias variables de instancia : nombre, dni , edad. Solo sus atributos y constructor, sin métodos adicionales 
 
3.2 ) Agregar a la clase Alumno, una lista enlazada que contenga el listado de profesores que el alumno tuvo. 
Para ello crear dos métodos :
 agregar_profesor_unab
 obtener_profesores_unab
instanciar objetos de tipo Profesor y almacenar al menos tres instancia en la lista enlazada. 

3.3) Crear un iterador para la lista enlazada de Alumnos.profesores e imprimir iterando  la edad promedio de los profesores 

Ejercicio 4)
Importar los módulos pickle,  y  Path de pathlib, para crear dos métodos en Alumnos,  guardar_materias() y leer_materias() para almacenar las materias aprobadas que están en alumnos.materias_aprobadas y luego levantar esa info,  e imprimirla sencillo
La serialización se realizará en un supuesto archivo llamado
materias.dat, al cual se accede concatenando el path home  + Documents/archivos/materias.dat para acceder a la ubicación del archivo 
"""
# Importar los módulos necesarios
from datetime import datetime
import pickle
from pathlib import Path

# -----------------------------------------------
# Módulo: Alumnos_Unab
# Descripción: Este módulo contiene la definición
#              de las clases Alumno, Materias y Profesor,
#              que representan los datos básicos de
#              un alumno de la facultad, las materias
#              que cursa y un profesor, respectivamente.
#
# Uso:
# 1. Coloca este archivo en el directorio donde
#    desees utilizar las clases.
# 2. Importa las clases en otros archivos donde
#    desees utilizarlas con la siguiente sintaxis:
#    from Alumnos_Unab import Alumno, Materias, Profesor
# 3. Crea instancias de Alumno, Materias y Profesor y utiliza
#    sus métodos según sea necesario.
# -----------------------------------------------

# Importar los módulos necesarios
import pickle
from pathlib import Path


# -----------------------------------------------
# Módulo: Alumnos_Unab
# Descripción: Este módulo contiene la definición
#              de las clases Alumno, Materias y Profesor,
#              que representan los datos básicos de
#              un alumno de la facultad, las materias
#              que cursa y un profesor, respectivamente.
#
# Uso:
# 1. Coloca este archivo en el directorio donde
#    desees utilizar las clases.
# 2. Importa las clases en otros archivos donde
#    desees utilizarlas con la siguiente sintaxis:
#    from Alumnos_Unab import Alumno, Materias, Profesor
# 3. Crea instancias de Alumno, Materias y Profesor y utiliza
#    sus métodos según sea necesario.
# -----------------------------------------------


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

if __name__ == "__main__":

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
