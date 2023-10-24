import json
import time



def menu():
    while True:
        print("*"*30)
        print("TIC TAC TOE / ACME GAME/")
        print("1. Iniciar Juego")
        print("2. Consultar tabla de posiciones")
        print("3. Salir")
        print("*"*30+ "\n")
        try:
            opcion = int(input("Digite opcion: "))
            if(opcion<1 or opcion>3):
                print("opcion no valida, digite nuevamente: ")
                continue
            break
        except Exception as e:
            print("No valido",e)
    return opcion

def leernombre(msg):
    while True:
        try:
            Nombre = input(msg)
            Nombre.strip()
            if(Nombre==""):
                print("Nombre no valido")
                continue
            return Nombre
        except Exception as e:
            print("Error al ingresar el nombre", e)


def LeerFicha(msg):
    while True:
        try:
            Ficha = input(msg)
            Ficha.strip()
            Ficha = Ficha.upper()
            if (Ficha == "X") or (Ficha == "O") and (Ficha != ""):
                return Ficha
            else:
                print("Ficha no valida")
                continue
        except Exception as e:
            print("Error al ingresar la Ficha", e)

def leerint(msg):
    while True:
        try:
            Entero = int(input(msg))
            if(Entero<1 or Entero>9):
                print("Valor invalido, debe estar entre 1 y 9")
                continue
            return Entero
        except Exception as e:
            print("Error al ingresar el numero", e)


def GuardarGanadores(lst,rutaFile):
    try:
        fd = open(rutaFile,"w")
    except Exception as e:
        print("error",e)
        return None
    try:
        json.dump(lst,fd)
    except Exception as e:
        print("Error al guardar la información del Ganador",e)
    fd.close
    return True
def PorSegundos(Segundos):
    return Segundos


def OrdenarGanadores(lstganadores,rutafile):
    for i in range(len(lstganadores)-1):
        for j in range(i+1,len(lstganadores)):
            if(lstganadores[i][1]>lstganadores[j][1]):
                t= lstganadores[i]
                lstganadores[i] = lstganadores[j]
                lstganadores[j] = t
            if(lstganadores[i][1]==lstganadores[j][1]):
                if lstganadores[i][2]>lstganadores[j][2]:
                    t= lstganadores[i]
                    lstganadores[i] = lstganadores[j]
                    lstganadores[j] = t
    GuardarGanadores(lstganadores,rutafile)
    return

def cargarinfo(lstGanadores,rutaFile):
    lstGanadores = []
    try:
        fd = open(rutaFile,"r")
    except Exception as e:
        try:
            fd = open(rutaFile,"w")
        except Exception as d:
            print("Error al intentar abrir el archivo",d)
            fd.close()
            return lstGanadores
    try:
        linea = fd.readline()
        if linea.strip() != "":
            fd.seek(0)
            lstGanadores = json.load(fd)
        else:
            lstGanadores = []
    except Exception as e:
        print("Error al cargar la informacion",e)
        return lstGanadores
    fd.close()
    return lstGanadores

def generarInterfaceMatriz(matrizJuego):
    print("+--------+--------+--------+")
    print("!        !        !        !")
    print(f"!   {matrizJuego[0][0]}    !   {matrizJuego[0][1]}    !   {matrizJuego[0][2]}    !")
    print("!        !        !        !")
    print("+--------+--------+--------+")
    print("!        !        !        !")
    print(f"!   {matrizJuego[1][0]}    !   {matrizJuego[1][1]}    !   {matrizJuego[1][2]}    !")
    print("!        !        !        !")
    print("+--------+--------+--------+")
    print("!        !        !        !")
    print(f"!   {matrizJuego[2][0]}    !   {matrizJuego[2][1]}    !   {matrizJuego[2][2]}    !")
    print("!        !        !        !")
    print("+--------+--------+--------+")

def EvaluarJugada(matrizJuego, Ficha):
    if(matrizJuego[0][0] == Ficha and matrizJuego[0][1]==Ficha and matrizJuego[0][2]==Ficha):
        return True
    elif(matrizJuego[1][0] == Ficha and matrizJuego[1][1]==Ficha and matrizJuego[1][2]==Ficha):
        return True
    elif(matrizJuego[2][0] == Ficha and matrizJuego[2][1]==Ficha and matrizJuego[2][2]==Ficha):
        return True
    elif(matrizJuego[0][0] == Ficha and matrizJuego[1][0]==Ficha and matrizJuego[2][0]==Ficha):
        return True
    elif(matrizJuego[0][1] == Ficha and matrizJuego[1][1]==Ficha and matrizJuego[2][1]==Ficha):
        return True
    elif(matrizJuego[0][2] == Ficha and matrizJuego[1][2]==Ficha and matrizJuego[2][2]==Ficha):
        return True
    elif(matrizJuego[2][0] == Ficha and matrizJuego[1][1]==Ficha and matrizJuego[0][2]==Ficha):
        return True
    elif(matrizJuego[0][0] == Ficha and matrizJuego[1][1]==Ficha and matrizJuego[2][2]==Ficha):
        return True
    else:
        return False


def RellenarMatriz(matrizJuego,opcion,Ficha):
    
    filas = len(matrizJuego)
    columnas = len(matrizJuego[0])

    for fila in range(filas):
        for columna in range(columnas):
            if str(opcion) == matrizJuego[fila][columna]:
                matrizJuego[fila][columna] = Ficha
    return

def InicializarJugador(dictJugadores,indice):
    dicttemp ={}
    Jugador = leernombre(f"Nombre Jugador {indice}: ")
    dicttemp["Nombre"] = Jugador
    
    if indice==1:
        Ficha = LeerFicha(f"{Jugador}: Digite ficha a usar -> [X/O]: ")
        dicttemp["Ficha"] = Ficha
    if indice ==2: 
        if dictJugadores[1]["Ficha"] == "X":
            dicttemp["Ficha"] = "O"
        else:
            dicttemp["Ficha"] = "X"
    dicttemp["Movimientos"] = 0
    dicttemp["Segundos"] = 0
          
    dictJugadores[indice] = dicttemp
    return

def NumeroJugada(dictJugadores, PosiblesJugadas,Turno):
    numero = leerint(f"Turno de {dictJugadores[Turno]['Nombre']}: Ingrese numero del 1 al 9: ")
    print("\n")
    while True:
        if(numero in PosiblesJugadas):
            PosiblesJugadas.pop(PosiblesJugadas.index(numero))
            break
        else:
            numero = leerint(f"Turno de {dictJugadores[Turno]['Nombre']}: Error - Ingrese numero disponible [1-9]: ")
    return numero

def TablaGanadores(lstGanadores):
    tamaño = 10
    print("+--------------+--------------+--------------+---------------+")
    print("!              !              !              !               !")
    print(f"!   Posición   !    Nombre    ! Movimientos  !   Segundos    !")
    print("!              !              !              !               !")
    print("+--------------+--------------+--------------+---------------+")
  
    for i in range(len(lstGanadores)):
        print("!              !              !              !               !")
        print("!"," "*(int((14-2)/2)),i+1," "*(int((14-1)/2)-3)," "*(int((14-len(lstGanadores[i][0]))/2)),lstGanadores[i][0]," "*(int((14-len(lstGanadores[i][0]))/2)-1), " "*(int((14-2)/2)),lstGanadores[i][1], " "*(int((14-2)/2)-1)," "*(int((14-5)/2)), f"{lstGanadores[i][2]:,.2f}","sg", " "*(int((14-5)/2)-1))
        print("!              !              !              !               !")
        print("+--------------+--------------+--------------+---------------+")

def inicio(lstganadores,rutafile):
    dictJugadores= {}
    matrizJuego = [["1","2","3"],["4","5","6"],["7","8","9"]]
    PosiblesJugadas = [1,2,3,4,5,6,7,8,9]
    print("\nTIC TAC TOE")
    print("\nIniciando Juego................................................................\n")
    for i in range(0,2):
        InicializarJugador(dictJugadores,i+1)

  
    intentos =  9
    Turno =  1
    Evalua = False
    for i in range(intentos):
        generarInterfaceMatriz(matrizJuego)
        print(f"\n {dictJugadores[1]['Nombre']} : [{dictJugadores[1]['Ficha']}]  / {dictJugadores[2]['Nombre']} : [{dictJugadores[2]['Ficha']}] \n")
        
        inicio = time.time()
        Numero = NumeroJugada(dictJugadores,PosiblesJugadas,Turno)
        fin = time.time()
        
        RellenarMatriz(matrizJuego,Numero,dictJugadores[Turno]['Ficha'])
        dictJugadores[Turno]['Segundos'] += (fin-inicio)
        dictJugadores[Turno]['Movimientos'] += 1
        
        Evalua = EvaluarJugada(matrizJuego,dictJugadores[Turno]['Ficha'])
        
        if(Evalua==True):
            generarInterfaceMatriz(matrizJuego)
            print(f"{dictJugadores[Turno]['Nombre']} Gano el Juego")
            print(f"Numero de movimientos: {dictJugadores[Turno]['Movimientos']}")
            print(f"Segundos: {dictJugadores[Turno]['Segundos']:,.3f}")
            lstGanador = []
            lstGanador.append(dictJugadores[Turno]['Nombre'])
            lstGanador.append( dictJugadores[Turno]['Movimientos'])
            lstGanador.append(dictJugadores[Turno]['Segundos'])
            lstganadores.append(lstGanador)
            GuardarGanadores(lstganadores,rutafile)
            return 
        
        if (Turno %2) != 0:   
            Turno+=1
        else:
            Turno=1
    
    generarInterfaceMatriz(matrizJuego)       
    print("Empate")
    print("Juego finalizado")
    return 

def main():
    lstGanadores = []
    rutafile = "proyectos/TablaGanadores.json"
    lstGanadores = cargarinfo(lstGanadores,rutafile)
    
    while True:
        opcion = menu()
        if(opcion==1):
            inicio(lstGanadores, rutafile)
        elif(opcion==2):
            OrdenarGanadores(lstGanadores,rutafile)
            TablaGanadores(lstGanadores)
        elif(opcion==3):
            print("Saliendo del juego.....................................")
            return
        
        try:
            op = str(input("Volver a jugar? si: cualquier caracter / no: n: "))
            if op.lower()=="n":
                print("Saliendo del juego.....................................")
                return
            continue
        except Exception as e:
            print("Error numero no valido")
            
main()