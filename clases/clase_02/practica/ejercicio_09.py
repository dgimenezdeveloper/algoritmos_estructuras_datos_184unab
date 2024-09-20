""" Se necesita realizar un programa para asistir a un empleado de un Cine (o Teatro). El empleado esta encargado de enviar a las personas a la sala correcta. 

Una vez comprada la entrada la audiencia se dirige al empleado, el cual, en base al número que figura en la entrada (3 dígitos) los envía a la sala correspondiente. 
Si la entrada es par, el empleado los dirige a la Sala 1. Cuando la entrada es impar los dirige a la sala 2. 

Recientemente, por un error en la impresión de las entradas han salido muchas con el número $000$, en este caso el empleado debe comunicarle al usuario que se dirija a la administraci\'on para obtener una nueva entrada. """

entrada = input("Ingrese el número de la entrada: ")
if entrada == "000":
    print("Por favor, diríjase a la administración para obtener una nueva entrada.")
else:
    numero = int(entrada)
    if numero % 2 == 0:
        print("Diríjase a la Sala 1.")
    else:
        print("Diríjase a la Sala 2.")