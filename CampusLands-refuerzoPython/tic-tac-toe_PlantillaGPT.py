# Función para imprimir el tablero actual
def imprimir_tablero(tablero):
    for fila in tablero:
        print(' | '.join(fila))
        print('---' * len(fila))

# Función para verificar si hay un ganador
def verificar_ganador(tablero, jugador):
    # Verificar filas
    for fila in tablero:
        if all(casilla == jugador for casilla in fila):
            return True
    # Verificar columnas
    for col in range(len(tablero[0])):
        if all(tablero[fila][col] == jugador for fila in range(len(tablero))):
            return True
    # Verificar diagonales
    if all(tablero[i][i] == jugador for i in range(len(tablero))) or \
            all(tablero[i][len(tablero) - 1 - i] == jugador for i in range(len(tablero))):
        return True
    return False

# Función principal para el juego
def jugar_tic_tac_toe():
    tablero = [[' ' for _ in range(3)] for _ in range(3)]
    jugador = 'X'

    while True:
        imprimir_tablero(tablero)
        fila = int(input(f'Jugador {jugador}, elige una fila (0, 1, 2): '))
        col = int(input(f'Jugador {jugador}, elige una columna (0, 1, 2): '))

        if 0 <= fila < 3 and 0 <= col < 3 and tablero[fila][col] == ' ':
            tablero[fila][col] = jugador
            if verificar_ganador(tablero, jugador):
                imprimir_tablero(tablero)
                print(f'¡Jugador {jugador} ha ganado!')
                break
            elif ' ' not in [casilla for fila in tablero for casilla in fila]:
                imprimir_tablero(tablero)
                print('El juego ha terminado en empate.')
                break
            jugador = 'X' if jugador == 'O' else 'O'
        else:
            print('Movimiento no válido. Por favor, intenta de nuevo.')

# Iniciar el juego
jugar_tic_tac_toe()
