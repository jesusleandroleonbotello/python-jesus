# hacer un juego de tic tac toe
# importar
import json
import time
import random
import os 

# parte inicial del juego 

def inicio_juego():
    print("💎💎💎💎 BIENVENIDOS 💎💎💎💎")
    time.sleep(2)
    while True: 
        ficha = input("Seleccione ficha: X / O\n")
        ficha = ficha.upper() # listo con esto eliegen la ficha asi la pongan en minuscula
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
    return(jugador1,jugador2)
# crear tablero

def tablero():
    print(" 💎JUEGO DE TIC TAC TOE💎 ")
    print("     ┊     ┊    ")
    print("  {}  ┊  {}  ┊  {} ".format(matriz[0],matriz[1],matriz[2]))
    print("     ┊     ┊    ")
    print("----------------")
    print("     ┊     ┊    ")
    print("  {}  ┊  {}  ┊   {} ".format(matriz[3],matriz[4],matriz[5]))
    print("     ┊     ┊    ")
    print("----------------")
    print("     ┊     ┊    ")
    print("  {}  ┊  {}  ┊  {} ".format(matriz[6],matriz[7],matriz[8]))
    print("     ┊     ┊    ")
# algorimos para definir empates o victorie

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
        posiciones = [0,1,2,3,4,5,6,7,8,9]
        jugador = int(input("Seleccione casilla: "))
        if jugador not in posiciones:
            print("Casilla no disponible")
        else: 
            if matriz[jugador-1]==" ":
                matriz[jugador-1]=jugador1
                break
            else:
                ("Casilla no disponible")

def movimiento_jugador2():

    posiciones=[0,1,2,3,4,5,6,7,8,9]
    casilla = 9
    parar = False

    for i in posiciones:
        copia = list(matriz)
        if copia[i]==" ":
            copia[i]=jugador2
            if victoria(copia)==True:
                casilla = i
    if casilla == 9:
        for j in posiciones:
            if copia[j]==" ":
                copia[j]=jugador1
                if victoria(copia)==True:
                    casilla = j
                
    if casilla== 9:
        while(not parar):
            casilla=random.randint(0,8)
            if matriz[casilla]==" ":
                parar=True
    matriz[casilla]=jugador2
        

# desarrollo de la partida

while True:
    
    matriz=[" "]*10
    os.system("cls")
    jugador1,jugador2=inicio_juego()
    partida = True
    ganador = 0
    
    while partida:
        ganador = ganador+1
        tablero()
        
        if victoria(matriz):
            if ganador%2==0:
                print("💎💎 Gana el jugador 1 💎💎")
                print("💎💎 Fin del juego 💎💎")
                print("\n Reiniciando ")
                time.sleep(5)
                partida=False
                
            else:
                print("💎💎 Gana el jugador 2 💎💎")
                print("💎💎 Fin del juego 💎💎")
                print("\n Reiniciando ")
                time.sleep(5)
                partida=False
                
        elif empate(matriz):
            print("💎💎 Empate")
            print("💎💎 Fin del juego 💎💎")
            print("\n Reiniciando ")
            time.sleep(5)
            partida=False
            
        elif ganador%2==0:
            print(" El jugador dos sigue ")
            time.sleep(2)
            movimiento_jugador2()
        
        else:
            movimiento_jugador1()