""" Ejercicio 1
1.1
Crear una clase Jugador, que contenga los datos básicos de una persona: nombre, dirección, teléfono, fecha de nacimiento, partidos, y un campo handicap que dependerá del puntaje obtenido en los partidos pasados. En el constructor, se deben inicializar todos los campos, y por defecto, el valor del handicap es 30 (treinta). Implementar los métodos para sumar o restar puntos al jugador.

1.2
Crear una clase Partido que contenga los campos identificador (tipo entero positivo), nombre, lugar, par (puntos totales obtenibles) , jugadores, y los puntos obtenidos por cada jugador. En el constructor se deben establecer todos estos datos. Crear los métodos necesarios para modificar estos valores.

IMPORTANTE: el handicap (los puntos) no pueden ser negativos.

Ejercicio 2:
2.1
Agregar a la clase Jugador un método iniciar_juego que le permita comenzar un nuevo partido, agregarlo a su lista de partidos y asignarle una lista (privada) de jugadores. Finalizada la partida se deben re calcular el handicap de cada jugador acorde con la siguiente formula:

Tomar en cuenta los ultimos 8 mejores puntajes de jugador.
Calcular el promedio.
2.2
Agregar a la clase Jugador un método calcular_handicap que reciba una lista de partidas y calcula el handicap del jugador. Utilizar el método de búsqueda lineal para obtener las partidas necesarias.

2.3
Agregar a la clase Jugador un método eliminar_juego que reciba el identificador del partido y elimine TODAS las instancias del partido, tanto en la lista del jugador y como de los otros jugadores. En cada ocasión, deben recalcularse los handicaps correspondientes del puntaje de los jugadores.

Ejercicio 3:
3.1
Implementar una clase Pila utilizando la siguiente definición de una Lista 'Simple' Enlazada. Utilizar el prototipo de la clase Lista Simple Enlazada mostrada a continuación.

![title] [pila_con_lista_enzada.png]

3.2
Utilizando la definición de la Pila (Ejercio 3.1). Definir una clase PilaPartidos la cual debe comportarse como una cola, es decir, redefinir las operaciones de la clase Pila para que se comporte como una cola.

3.3
Implementar iteradores para las clases definidas en los ejercicios anteriores (Ejercicios 3.1 y 3.2).

Ejercicio 4:
4.1
Agregar a la clase un método partidos_a_string que devuelva una lista de strings con los atributos de los partidos jugados (una lista de strings que luego podamos recorrer e imprimir los partidos)

4.2
Escribir una funcion que genere una lista de jugadores y partidos asociados a estos jugadores. Las listas son generadas aleatoriamente, o sin asistencia del usuario/programador.

4.3
Escribir una función que reciba la lista de jugadores creada en el punto anterior (4.2) y genere archivos de texto con extensión .csv cuyo nombre sea el nombre del jugador y que contengan la lista de partidos correspondientes, un partido en cada línea (con sus respectivos datos). """