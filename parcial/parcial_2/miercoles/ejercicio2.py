""" Definir una clase Alumno como un diccionario, el cual contiene los datos:


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
Pueden agregar más atributos y métodos, si lo consideran necesario. """
from datetime import datetime, timedelta
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

    def calcular_dif_fecha(self, otra_fecha):
        fecha1 = datetime(self.anio, self.mes, self.dia)
        fecha2 = datetime(otra_fecha.anio, otra_fecha.mes, otra_fecha.dia)
        return abs((fecha2 - fecha1).days)

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
        return self["FechaIngreso"].calcular_dif_fecha(Fecha())