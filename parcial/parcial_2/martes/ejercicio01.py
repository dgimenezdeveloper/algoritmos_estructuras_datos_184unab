"""  Ejercicio 1:
Definir una clase Producto, el cual contiene los siguientes datos:
descripcion : 'string' 
ID : 'integer' 
FechaExp : date, ## importar datetime 
INFO : 'de cualquier tipo' 
La clase debe contener los siguinetes métodos:
Cambiar uno o varios datos del Producto.
calcularexpirados()Calcular en cuantos dias/horas expira un producto. Si el método detecta que el producto ha expirado, debera lanzar una excepción.
Sobrecarga de métodos:

__str__
__eq__
Importante:

Pueden agregar más atributos y métodos, si lo consideran necesario. """
import datetime
class Producto:
    def __init__(self, descripcion, ID, FechaExp, INFO):
        self.descripcion = descripcion
        self.ID = ID
        self.FechaExp = FechaExp
        self.INFO = INFO
    
    def cambiar_datos(self, descripcion = None, ID = None, FechaExp = None, INFO = None):
        if descripcion:
            self.descripcion = descripcion
        if ID:
            self.ID = ID
        if FechaExp:
            self.FechaExp = FechaExp
        if INFO:
            self.INFO = INFO
    
    def calcularexpirados(self):
        hoy = datetime.datetime.now()
        if self.FechaExp < hoy:
            raise Exception(f"El producto {self.descripcion} ha expirado.")
        else:
            diferencia = self.FechaExp - hoy
            return diferencia.days, diferencia.seconds // 3600
    
    def __str__(self):
        return f"Producto(ID={self.ID}, Descripción='{self.descripcion}', Fecha de Expiración={self.FechaExp}, INFO={self.INFO})"
    
    def __eq__(self, otro):
        return self.ID == otro.ID
    