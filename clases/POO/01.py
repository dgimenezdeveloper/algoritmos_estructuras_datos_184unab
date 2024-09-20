import random

class Dado:
    def __init__(self):
        self.valor = None
        self.cara_actual = None

    def tirar(self):
        self.valor = random.randint(1, 6)
        self.cara_actual = self.valor

    def __str__(self):
        return str(self.valor)  # Devolver el valor del dado como un string

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.puntaje_total = 0
        self.puntaje_por_ronda = 0

    def __str__(self):
        return self.nombre

class Marcador:
    def __init__(self, jugadores):
        self.jugadores = jugadores
        self.combinaciones_validas = ["Generala", "Poker", "Full", "Escalera", "Trío", "Dos pares", "Par"]
        self.puntajes = {combinacion: 0 for combinacion in self.combinaciones_validas}

    def mostrar_puntajes(self):
        for jugador in self.jugadores:
            print(f"Puntaje de {jugador}: {jugador.puntaje_total}")

    def anotar_puntaje(self, jugador, combinacion, puntaje):
        jugador.puntaje_total += puntaje
        jugador.puntaje_por_ronda += puntaje
        self.puntajes[combinacion] += puntaje

def tirar_dados(dados):
    for dado in dados:
        dado.tirar()
    print("Tirada:", [str(dado) for dado in dados])  # Mostrar los valores de los dados como una lista de números

def menu_jugador(jugador):
    print(f"Turno de {jugador}")
    print("1. Tirar dados")
    print("2. Anotar combinación")
    opcion = int(input("Seleccione una opción: "))
    return opcion

def calcular_puntaje(dados):
    valores = [dado.valor for dado in dados]
    valores.sort()

    if valores == [1, 2, 3, 4, 5] or valores == [2, 3, 4, 5, 6]:
        return 20  # Escalera
    elif valores.count(valores[0]) == 5:
        return 50  # Generala
    elif valores.count(valores[0]) == 4 or valores.count(valores[1]) == 4:
        return 40  # Poker
    elif (valores.count(valores[0]) == 3 and valores.count(valores[3]) == 2) or \
            (valores.count(valores[0]) == 2 and valores.count(valores[2]) == 3):
        return 30  # Full
    elif valores.count(valores[0]) == 3 or valores.count(valores[1]) == 3 or valores.count(valores[2]) == 3:
        return 10  # Trío
    elif valores.count(valores[0]) == 2 and valores.count(valores[2]) == 2:
        return 5  # Dos pares
    elif valores.count(valores[0]) == 2 or valores.count(valores[1]) == 2 or valores.count(valores[2]) == 2:
        return 1  # Par
    else:
        return 0

def jugar_ronda(jugadores, marcador):
    dados = [Dado() for _ in range(5)]
    for _ in range(3):
        tirar_dados(dados)
        opcion = menu_jugador(jugadores[0])
        if opcion == 2:
            combinacion = input("Ingrese la combinación: ")
            puntaje = calcular_puntaje(dados)
            marcador.anotar_puntaje(jugadores[0], combinacion, puntaje)

def main():
    num_jugadores = int(input("Ingrese el número de jugadores: "))
    jugadores = [Jugador(input(f"Nombre del jugador {i+1}: ")) for i in range(num_jugadores)]
    marcador = Marcador(jugadores)

    for _ in range(3):
        jugar_ronda(jugadores, marcador)
        marcador.mostrar_puntajes()

    # Determinar ganador
    puntajes_finales = [jugador.puntaje_total for jugador in jugadores]
    indice_ganador = puntajes_finales.index(max(puntajes_finales))
    ganador = jugadores[indice_ganador]
    print(f"El ganador es {ganador} con {ganador.puntaje_total} puntos.")

if __name__ == "__main__":
    main()
