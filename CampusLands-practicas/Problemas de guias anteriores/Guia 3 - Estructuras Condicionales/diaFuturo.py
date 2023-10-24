# Programa para calcular el día actual y el día futuro en 
# base a números 0-6


# DEFINIENDO LAS VARIABLES PRINCIPALES
diaSemanaActual = int(input("Introduzca el número del día de la semana (0 Domingo, 1 Lunes ... 6 Sábado): "))
diaSemanaFuturo = int(input("Introduzca la cantidad de días a futuro: "))

if diaSemanaActual == 0:
    diaActual = "Domingo"
    diaFuturo = diaSemanaFuturo % 7

    if diaFuturo == 0:
        nombreDiaFuturo = "Domingo"
    elif diaFuturo == 1:
        nombreDiaFuturo = "Lunes"
    elif diaFuturo == 2:
        nombreDiaFuturo = "Martes"
    elif diaFuturo == 3:
        nombreDiaFuturo = "Miércoles"
    elif diaFuturo == 4:
        nombreDiaFuturo = "Jueves"
    elif diaFuturo == 5:
        nombreDiaFuturo = "Viernes"
    elif diaFuturo == 6:
        nombreDiaFuturo = "Sábado"
    
elif diaSemanaActual == 1:
    diaActual = "Lunes"
    diaFuturo = diaSemanaFuturo % 7

    if diaFuturo == 0:
        nombreDiaFuturo = "Domingo"
    elif diaFuturo == 1:
        nombreDiaFuturo = "Lunes"
    elif diaFuturo == 2:
        nombreDiaFuturo = "Martes"
    elif diaFuturo == 3:
        nombreDiaFuturo = "Miércoles"
    elif diaFuturo == 4:
        nombreDiaFuturo = "Jueves"
    elif diaFuturo == 5:
        nombreDiaFuturo = "Viernes"
    elif diaFuturo == 6:
        nombreDiaFuturo = "Sábado"

elif diaSemanaActual == 2:
    diaActual = "Martes"
    diaFuturo = diaSemanaFuturo % 7

    if diaFuturo == 0:
        nombreDiaFuturo = "Domingo"
    elif diaFuturo == 1:
        nombreDiaFuturo = "Lunes"
    elif diaFuturo == 2:
        nombreDiaFuturo = "Martes"
    elif diaFuturo == 3:
        nombreDiaFuturo = "Miércoles"
    elif diaFuturo == 4:
        nombreDiaFuturo = "Jueves"
    elif diaFuturo == 5:
        nombreDiaFuturo = "Viernes"
    elif diaFuturo == 6:
        nombreDiaFuturo = "Sábado"

elif diaSemanaActual == 3:
    diaActual = "Miércoles"
    diaFuturo = diaSemanaFuturo % 7

    if diaFuturo == 0:
        nombreDiaFuturo = "Domingo"
    elif diaFuturo == 1:
        nombreDiaFuturo = "Lunes"
    elif diaFuturo == 2:
        nombreDiaFuturo = "Martes"
    elif diaFuturo == 3:
        nombreDiaFuturo = "Miércoles"
    elif diaFuturo == 4:
        nombreDiaFuturo = "Jueves"
    elif diaFuturo == 5:
        nombreDiaFuturo = "Viernes"
    elif diaFuturo == 6:
        nombreDiaFuturo = "Sábado"

elif diaSemanaActual == 4:
    diaActual = "Jueves"
    diaFuturo = diaSemanaFuturo % 7

    if diaFuturo == 0:
        nombreDiaFuturo = "Domingo"
    elif diaFuturo == 1:
        nombreDiaFuturo = "Lunes"
    elif diaFuturo == 2:
        nombreDiaFuturo = "Martes"
    elif diaFuturo == 3:
        nombreDiaFuturo = "Miércoles"
    elif diaFuturo == 4:
        nombreDiaFuturo = "Jueves"
    elif diaFuturo == 5:
        nombreDiaFuturo = "Viernes"
    elif diaFuturo == 6:
        nombreDiaFuturo = "Sábado"

elif diaSemanaActual == 5:
    diaActual = "Viernes"
    diaFuturo = diaSemanaFuturo % 7

    if diaFuturo == 0:
        nombreDiaFuturo = "Domingo"
    elif diaFuturo == 1:
        nombreDiaFuturo = "Lunes"
    elif diaFuturo == 2:
        nombreDiaFuturo = "Martes"
    elif diaFuturo == 3:
        nombreDiaFuturo = "Miércoles"
    elif diaFuturo == 4:
        nombreDiaFuturo = "Jueves"
    elif diaFuturo == 5:
        nombreDiaFuturo = "Viernes"
    elif diaFuturo == 6:
        nombreDiaFuturo = "Sábado"

elif diaSemanaActual == 6:
    diaActual = "Sábado"
    diaFuturo = diaSemanaFuturo % 7

    if diaFuturo == 0:
        nombreDiaFuturo = "Domingo"
    elif diaFuturo == 1:
        nombreDiaFuturo = "Lunes"
    elif diaFuturo == 2:
        nombreDiaFuturo = "Martes"
    elif diaFuturo == 3:
        nombreDiaFuturo = "Miércoles"
    elif diaFuturo == 4:
        nombreDiaFuturo = "Jueves"
    elif diaFuturo == 5:
        nombreDiaFuturo = "Viernes"
    elif diaFuturo == 6:
        nombreDiaFuturo = "Sábado"


print(f"El día actual es {diaActual} y el día a futuro es el {nombreDiaFuturo}")