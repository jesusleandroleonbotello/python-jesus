import json
import time
import os

# Ruta al archivo JSON en la carpeta "proyecto"
json_file_path = "proyecto/ganadores.json"

# Antes del inicio del juego
jugadores = {}

# Inicialización del juego
def inicio_juego(ganadores, jugadores):
    print("💎💎💎💎 BIENVENIDOS 💎💎💎💎")
    time.sleep(1)

    jugador1, jugador2 = "", ""

    while not jugador1:
        nombre = input("Jugador 1, ingrese su nombre: ").strip()
        if nombre:
            if es_ganador(nombre, ganadores):
                print(f"{nombre} ya es un ganador. Elija otro nombre.")
            else:
                jugador1 = nombre
        else:
            print("Por favor, ingrese un nombre válido.")

    ficha = input(f"{jugador1}, elija su ficha (X/O): ").strip().upper()
    while ficha not in ["X", "O"]:
        print("Por favor, elija una ficha válida (X/O).")
        ficha = input(f"{jugador1}, elija su ficha (X/O): ").strip().upper()

    if ficha == "X":
        jugador1_ficha = "X"
        jugador2_ficha = "O"
        jugador_inicia = jugador1
    else:
        jugador1_ficha = "O"
        jugador2_ficha = "X"
        jugador_inicia = jugador2

    jugadores[jugador1] = [jugador1_ficha, jugador_inicia, []]  # Agregar los datos del jugador 1 al diccionario

    while not jugador2:
        nombre = input("Jugador 2, ingrese su nombre: ").strip()
        if nombre:
            if nombre == jugador1:
                print("El nombre ya ha sido elegido por el Jugador 1. Elija otro nombre.")
            elif es_ganador(nombre, ganadores):
                print(f"{nombre} ya es un ganador. Elija otro nombre.")
            else:
                jugador2 = nombre
        else:
            print("Por favor, ingrese un nombre válido.")

    jugadores[jugador2] = [jugador2_ficha, jugador_inicia, []]  # Agregar los datos del jugador 2 al diccionario

    if not jugador_inicia:
        jugador_inicia = jugador2

    return (jugador1, jugador1_ficha, jugador2, jugador2_ficha, jugador_inicia)

# Comprobar si un jugador ya es ganador
def es_ganador(jugador, ganadores):
    for ganador in ganadores:
        if jugador in ganador:
            return True
    return False

# Crear y mostrar el tablero del juego
def tablero(matriz):
    os.system("clear")  # Usa "clear" en sistemas basados en Unix
    print(" 💎JUEGO DE TIC TAC TOE💎 ")
    print("     ┊     ┊    ")
    print("  {}  ┊  {}  ┊  {} ".format(matriz[0], matriz[1], matriz[2]))
    print("     ┊     ┊    ")
    print("----------------")
    print("     ┊     ┊    ")
    print("  {}  ┊  {}  ┊  {} ".format(matriz[3], matriz[4], matriz[5]))
    print("     ┊     ┊    ")
    print("----------------")
    print("     ┊     ┊    ")
    print("  {}  ┊  {}  ┊  {} ".format(matriz[6], matriz[7], matriz[8]))
    print("     ┊     ┊    ")

# Menú del juego con decoración
def menu():
    print("\n╔════════════════════════════════╗")
    print("║         MENÚ PRINCIPAL         ║")
    print("╠════════════════════════════════╣")
    print("║ 1. Jugar🔰                     ║")
    print("║ 2. Mostrar Ganadores           ║")
    print("║ 3. Salir                       ║")
    print("╚════════════════════════════════╝")

# Comprobar empate
def empate(matriz):
    for casilla in matriz:
        if casilla == " ":
            return False
    return True

# Comprobar victoria
def victoria(matriz):
    combinaciones_victoria = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for combinacion in combinaciones_victoria:
        a, b, c = combinacion
        if matriz[a] == matriz[b] == matriz[c] != " ":
            return True
    return False

# Movimiento del jugador
def movimiento_jugador(jugador, jugador_ficha, matriz, tiempos_jugadores, jugadores):
    while True:
        try:
            inicio_tiempo = time.time()  # Comienza a contar el tiempo
            casilla = int(input(f"{jugador}, seleccione casilla (1-9): "))
            if 1 <= casilla <= 9 and matriz[casilla - 1] == " ":
                matriz[casilla - 1] = jugador_ficha
                tiempo_transcurrido = time.time() - inicio_tiempo  # Calcula el tiempo transcurrido
                tiempos_jugadores[jugador] += tiempo_transcurrido  # Agrega el tiempo al jugador
                jugadores[jugador][2].append(casilla)  # Agrega la casilla al registro de movimientos del jugador
                break
            else:
                print("Casilla no disponible o número fuera de rango. Intente de nuevo.")
        except ValueError:
            print("Entrada no válida. Ingrese un número del 1 al 9.")

# Cargar la lista de ganadores desde el archivo JSON
def cargar_ganadores():
    try:
        with open(json_file_path, "r") as file:
            ganadores = json.load(file)
    except FileNotFoundError:
        ganadores = []
    return ganadores

# Guardar la lista de ganadores en el archivo JSON
def guardar_ganadores(ganadores):
    with open(json_file_path, "w") as file:
        json.dump(ganadores, file)

# Mostrar lista de ganadores
def mostrar_ganadores(ganadores):
    print("Lista de Ganadores:")
    for i, ganador in enumerate(ganadores, 1):
        print(f"{i}. {ganador}")

# Preguntar si los jugadores quieren jugar de nuevo
def jugar_de_nuevo():
    while True:
        respuesta = input("¿Desean jugar de nuevo? (S/N): ").strip().upper()
        if respuesta == "S":
            return True
        elif respuesta == "N":
            return False
        else:
            print("Por favor, responda con S (Sí) o N (No).")

# Bucle principal del juego
while True:
    menu()
    opcion = input("Seleccione una opción (1/2/3): ").strip()
    
    if opcion == "1":
        matriz = [" "]*9
        ganadores = cargar_ganadores()

        # Inicializar jugadores
        jugadores = {}

        # Iniciar juego
        jugador1, jugador1_ficha, jugador2, jugador2_ficha, jugador_inicia = inicio_juego(ganadores, jugadores)
        tiempos_jugadores = {jugador1: 0, jugador2: 0}
        partida = True
        movimientos = 0  # Contador de movimientos

        if jugador_inicia == jugador2:
            jugador1, jugador2 = jugador2, jugador1
            jugador1_ficha, jugador2_ficha = jugador2_ficha, jugador1_ficha

        tablero(matriz)  # Mostrar el tablero al comienzo del juego
        
        while partida:
            movimiento_jugador(jugador1, jugador1_ficha, matriz, tiempos_jugadores, jugadores)
            movimientos += 1
            tablero(matriz)  # Actualizar el tablero después del movimiento

            if victoria(matriz):
                tiempo_ganador = (jugadores[jugador1][2])
                print(f"💎💎 {jugador1} ({jugador1_ficha}) Tiempo: {tiempo_ganador:.2f} segundos - Movimientos: {movimientos} gana la partida 💎💎")
                ganadores.append(f"{jugador1} ({jugador1_ficha}) ({time.strftime('%Y-%m-%d %H:%M:%S')}) - Tiempo: {tiempo_ganador:.2f} segundos - Movimientos: {movimientos}")
                print("💎💎 Fin del juego 💎💎")
                while True:
                    jugar_de_nuevo = input("¿Desean jugar de nuevo con los mismos jugadores? (S/N): ").strip().upper()
                    if jugar_de_nuevo == "S":
                        if victoria(matriz):
                            matriz = [" "]*9
                            partida = True  # Inicia una nueva partida con los mismos jugadores
                            if jugador1_ficha == "X":
                                jugador1_ficha = "O"
                                jugador2_ficha = "X"
                                jugador_inicia = jugador2
                                tiempos_jugadores[jugador1] = 0
                                tiempos_jugadores[jugador2] = 0
                            else:
                                jugador1_ficha = "X"
                                jugador2_ficha = "O"
                                jugador_inicia = jugador2
                                tiempos_jugadores[jugador1] = 0
                                tiempos_jugadores[jugador2] = 0
                            tablero(matriz)  # Mostrar el tablero al comienzo de la nueva partida
                        elif jugador1 not in ganadores:
                            tiempo_ganador = min(jugadores[jugador1][2])
                            print(f"💎💎 {jugador1} ({jugador1_ficha}) Tiempo: {tiempo_ganador:.2f} segundos - Movimientos: {movimientos} gana la partida 💎💎")
                            ganadores.append(f"{jugador1} ({jugador1_ficha}) ({time.strftime('%Y-%m-%d %H:%M:%S')}) - Tiempo: {tiempo_ganador:.2f} segundos - Movimientos: {movimientos}")
                            print("💎💎 Fin del juego 💎💎")
                        else:
                            print("💎💎 Fin del juego 💎💎")
                        break
                    elif jugar_de_nuevo == "N":
                        partida = False
                        break  # Salir al menú principal
                    else:
                        print("Por favor, ingrese 'S' para jugar de nuevo o 'N' para salir.")
                    
            elif empate(matriz):
                print("💎💎 Empate - Movimientos: {movimientos}")
                print("💎💎 Fin del juego 💎💎")
            
                while True:
                    jugar_de_nuevo = input("¿Desean jugar de nuevo con los mismos jugadores? (S/N): ").strip().upper()
                    if jugar_de_nuevo == "S":
                        matriz = [" "]*9
                        partida = True  # Inicia una nueva partida con los mismos jugadores
                        movimientos = 0
                        if jugador1_ficha == "X":
                            jugador1_ficha = "O"
                            jugador2_ficha = "X"
                            jugador_inicia = jugador2
                            tiempos_jugadores[jugador1] = 0
                            tiempos_jugadores[jugador2] = 0
                        else:
                            jugador1_ficha = "X"
                            jugador2_ficha = "O"
                            jugador_inicia = jugador2
                            tiempos_jugadores[jugador1] = 0
                            tiempos_jugadores[jugador2] = 0
                        tablero(matriz)  # Mostrar el tablero al comienzo de la nueva partida
                        break
                    elif jugar_de_nuevo == "N":
                        partida = False
                        break  # Salir al menú principal
                    else:
                        print("Por favor, ingrese 'S' para jugar de nuevo o 'N' para salir.")
                break

            if not partida:
                break

            movimiento_jugador(jugador2, jugador2_ficha, matriz, tiempos_jugadores, jugadores)
            movimientos += 1
            tablero(matriz)  # Actualizar el tablero después del movimiento

        guardar_ganadores(ganadores)  # Guardar la lista de ganadores
        
    if opcion == "2":
        ganadores = cargar_ganadores()
        mostrar_ganadores(ganadores)
        time.sleep(4)
    
    elif opcion == "3":  # salir del programa
        print("Gracias por usar el programa")
        break