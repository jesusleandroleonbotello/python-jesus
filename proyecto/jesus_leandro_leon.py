# hacer un juego de tic tac toe
# importar
import json
import time

# parte inicial del juego 

def inicio_juego():
    print("💎💎💎💎 BIENVENIDOS 💎💎💎💎")
    time.sleep(1)
    while True: 
        ficha = input("Seleccione ficha: X / O\n")
        ficha = ficha.upper # listo con esto eliegen la ficha asi la pongan en minuscula
        if ficha == "X":
            jugador1 = "x"
            jugador2 = "O"
            break
        elif ficha == "O":
            jugador1 = "O"
            jugador2 = "X"
            break
        else:
            print("Por favor introce una ficha posible ")

# crear tablero

def tablero():
    print(" 💎JUEGO DE TIC TAC TOE💎 ")
    matriz = 0
    print(" {} ┊ {} ┊ {} ".format(matriz[0],matriz[1],matriz[2]))
    print("-------------")
    print(" {} ┊ {} ┊ {} ".format(matriz[3],matriz[4],matriz[5]))
    print("-------------")
    print(" {} ┊ {} ┊ {} ".format(matriz[6],matriz[7],matriz[8]))

# algorimos para definir empates o victoria

def empate(matriz):
    empate = True
    i = 0
    while(empate==True and i<9):
        if matriz[i]==" ":
            empate=False
        i=i+1
    return empate

def victoria(matriz):
    if (matriz[0]==matriz[1]==matriz[2]!=" " or matriz[3]==matriz[4]==matriz[5]!=" " or matriz[6]==matriz[7]==matriz[8]!=" " or matriz[0]==matriz[3]==matriz[6]!=" " or matriz[1]==matriz[4]==matriz[7]!=" " or matriz[2]==matriz[5]==matriz[8]!=" " or matriz[0]==matriz[4]==matriz[8]!=" " or matriz[2]==matriz[4]==matriz[6]!=" "):
        return True
    else:
        return False
    
# programr movimientos

def movimiento_jugador1():
    while True:
        posiciones = [1,2,3,4,5,6,7,8,9]
        jugador1 = int(input("Seleccione casilla: "))
        if posiciones not in posiciones:
            print("Casilla no disponible")
        else: 
            if matriz[posiciones-1]==" ":
                matriz[posiciones-1]==jugador1
                break
            else:
                ("Casilla no disponible")
        posiciones1 = posiciones-(jugador1)
        return posiciones1

def movimiento_jugador2():
    while True:
        posiciones=[1,2,3,4,5,6,7,8,9]
        casilla = 9
        parar = False

        for i in posiciones:
            copia = list(matriz)
            if copia[i]==" ":
                copia[i]=jugador2:
                if victoria(copia)==True:
                    casilla = i
        if casilla == 9:
            for j in posiciones:
                if copia[i]==" ":
                    