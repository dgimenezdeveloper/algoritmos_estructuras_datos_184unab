LUNES
""" 1.1 - Crear una clase Comprador que contenga los datos básicos de una persona: nombre, dirección, teléfono, fecha de nacimiento y un campo puntaje que dependerá de las compras que realice. En el constructor, se deben inicializar todos los campos, y por defecto, el valor de puntaje será 0 (cero). Implementar los métodos para sumar o restar puntos del puntaje del comprador. """

""" 1.2 - Crear una clase Artículos que contenga los campos identificador (tipo entero positivo), nombre, descripción, marca, precio (float) y puntos. En el constructor se deben establecer todos estos datos. Crear los métodos necesarios para modificar estos valores. IMPORTANTE: los puntos no pueden ser negativos.
"""

""" 2.1 - Agregar a la clase Comprador un método comprar_articulo que permita adquirir Artículos y agregarlos a una lista (privada) de artículos comprados. Al comprarlos, los puntos del artículo se suman a los puntos de Comprador. """

""" Agregar a la clase Comprador un método encontrar_articulo que reciba el identificador del artículo y devuelva True o False de acuerdo a si el artículo está o no en la lista del comprador. Utilizar el método de búsqueda lineal. """


""" Agregar a la clase Comprador un método eliminar_articulo que reciba el identificador del artículo y elimine TODAS las instancias del artículo en la lista del comprador. En cada ocasión, deben eliminarse los puntos correspondientes al artículo del puntaje del Comprador. """


""" Crear seis instancias de compradores, y agregarles (mediante el método comprar_articulo) diferentes cantidades de artículos. Nota: crear las instancias necesarias de artículos diferentes.
"""

""" Crear una lista con estos compradores """


""" Utilizar el método de ordenamiento burbuja para ordenarlos de forma DESCENDENTE (de mayor valor a menor valor) de acuerdo al puntaje de cada uno. """

""" Crear una lista enlazada de todos los artículos creados en el punto 3.1, y escribir una función que pueda procesar esta lista y determinar (devolviendo un valor booleano) si existen dos artículos con la misma cantidad de puntos.
 """


""" Agregar a la clase Comprador un método lista_a_string que devuelva una lista de strings con los atributos de los artículos comprados [identificador, nombre, marca, precio, puntos] separador por puntos y comas (ej: [1;”computadora”;”del”; 100.00;30,5;”mouse”;”logitech”;200.00;15]) """

""" Escribir una función que reciba la lista de compradores creada en el punto 3.2 y genere archivos de texto con extensión .csv cuyo (usar los metodos de la libreria pathlib y os para verificar y crear directorios de ser necesario) nombre sea el nombre del comprador y que contenga la lista de artículos correspondientes, un artículo en cada línea.
 """

MARTES

""" 
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
Importante:Pueden agregar más atributos y métodos, si lo consideran necesario.

Crear una clase Mercado, el cual estara representado mediante una o varias Listas Enlazadas cuyos nodos contengan como dato objetos del tipo Producto. Cada lista enlazada corresponde a un pasillo (o sección del mercado).
La clase debe contener métodos para facilitar:
Controlar el stock de productos (añadir y remover, etc).
Calcular en cuantos productos expiran en las proximas 24hs y removerlos.
Importante:Pueden agregar más atributos y métodos, si lo consideran necesario.

Añadir un método a la clase Mercado que permita buscar un producto y removerlo (venderlo). Recordar que deben actualizar el stock. Si un producto se termina, el método debe lanzar una excepcion.
Importante:Utilizar Iteradores de ser posible.
Pueden agregar más atributos y funciones/métodos, si lo consideran necesario. 

Añadir a la clase Mercado un atributo clientes implementando una clase ColaPrioridad utilizando el siguiente modelo de definición,  Una Cola de Prioridades es similar a una cola pero sus elementos tienen una prioridad asignada. Los elementos de mayor prioridad serán desencolados primero

"""
"""
class _Node:

    __slot_s_ = '_element', '_next', '_priory' # optimiza el uso de memoria
    def _init__(self, element, prev, next):
        self._element = element #inicializar contenido del Nodo
        self._next = next # referencia al siguiente Nodo
        self._priory = priory # prioridad del elemento
        
class ColaPrioridad:

def __init__(self):
    
    self._head = None
    self._tail = None
    self._size = 0 # Numero de elementos en la Cola

Implementar un Iterador para la clase ColaPrioridad.

Escribir una función, llamada head que reciba como parámetros un archivo y un número N e imprima las primeras N líneas del archivo. 

Escribir una función, llamada grep que reciba una expresión y un archivo, e imprima las líneas del archivo que contienen la expresión recibida. 
"""

MIERCOLES

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

VIERNES


""" 'EXAMEN COMISIÓN 7 UNAB SOBRE ALGORITMOS Y ESTRUCTURAS DE DATOS
MODALIDAD: Tienen 1 (un) solo intento para resolver la actividad, el tiempo máximo es de 4 (cuatro) horas. El tiempo cuenta desde el
momento en que acepten realizar la tarea en Github Classroom y cualquier "commit" realizado luego de 4 (cuatro) horas, no será aceptado
como parte del intento de resolución.
#EJERCICIO 1 Una nueva Sucursal del Banco ILBA tiene 3 nuevos clientes, los cuales pueden hacer depósitos y extracciones. También, esta
sucursal necesita que al final del día calcule la cantidad de dinero que hay depositado. Identificar las clases Cliente y la clase Banco. Definir los
atributos y los métodos de cada clase Realizar un menú de consultas para cada operación
#EJERCICIO 2 Debes desarrollar una aplicación para administrar el inventario de una cadena de tiendas de electrónica. Cada local tiene su
propio inventario de productos, identificados por un código único. Cuando un cliente solicita un producto, se debe buscar su código en el
inventario de la tienda correspondiente para verificar si está disponible. Hay que implementar un algoritmo de búsqueda lineal para encontrar
un código de producto específico en el inventario de cada tienda. El programa debe: Permitir al usuario ingresar el código del producto que
está buscando. Permitir al usuario seleccionar la tienda en la que desea buscar el producto. Recorrer el inventario de la tienda seleccionada de
forma secuencial hasta encontrar el código solicitado. Informar al usuario si el producto está disponible o no en el inventario de la tienda.
#EJERCICIO 3 Crear y cargar en un lista los nombres de 5 países y en otra lista paralela la cantidad de habitantes del mismo. Ordenar
alfabéticamente e imprimir los resultados. Por último ordenar con respecto a la cantidad de habitantes (de mayor a menor) e imprimir
nuevamente.Importante: Utilizar algoritmo de ordenamiento no funciónes de Python
#EJERCICIO 4 Te piden desarrollar un sistema de gestión de contactos para una empresa. Cada contacto tiene un nombre, un número de
teléfono y una dirección de correo. Necesitas implementar una estructura de datos que te permita almacenar y manipular eficientemente esta
información. Tu tarea es escribir un programa que utilice una lista enlazada para implementar las siguientes funcionalidades: Agregar un nuevo
contacto a la lista. Buscar un contacto por su nombre. Eliminar un contacto de la lista. Mostrar todos los contactos en la lista.
"""
