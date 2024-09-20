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