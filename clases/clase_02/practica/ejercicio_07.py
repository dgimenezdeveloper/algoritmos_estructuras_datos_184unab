import datetime

""" Diseñar un algoritmo que pida al usuario el ingreso de un horario, expresado en horas, minutos y segundos e indique la diferencia entre el horario ingresado y la hora actual en horas, minutos y segundos. """
# Obtener la hora actual
hora_actual = datetime.datetime.now().time()

# Obtener el horario ingresado por el usuario
hora_ingresada = input("Ingrese el horario (HH:MM:SS): ")

# Convertir el horario ingresado a objeto datetime.time
hora_ingresada = datetime.datetime.strptime(hora_ingresada, "%H:%M:%S").time()

# Calcular la diferencia entre el horario ingresado y la hora actual
diferencia = datetime.datetime.combine(datetime.date.today(), hora_ingresada) - datetime.datetime.combine(datetime.date.today(), hora_actual)

# Imprimir la diferencia en horas, minutos y segundos
print("La diferencia es: {} horas, {} minutos, {} segundos".format(diferencia.seconds // 3600, (diferencia.seconds // 60) % 60, diferencia.seconds % 60))