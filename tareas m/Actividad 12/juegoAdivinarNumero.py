# Este programa es un juego en el cuál, el usuario deberá ingresar un número de entre 1 y 1000. La computadora generará 
# un número aleatorio y el jugador tendrá que adivinar el número elegido por la PC. Tendrá 10 inténtos. Otros valores
# y parámetros están presentes dentro del enunciado del ejercicio.


# IMPORTAR LIBRERIAS NECESARIAS
import random


# DEFINIENDO LAS VARIABLES PRINCIPALES
isVerdadero = True
vidas = 10


# DECLARANDO LAS FUNCIONES COMPLEMENTARIAS
def filtradoTexto(text):
    nombreArray = text.split(" ")
    nombreFinalArray = []
    
    for n in nombreArray:
        if n != "":
            nombreFinalArray.append(n)
    
    nombreValidacion = "".join(nombreFinalArray)
    nombreFinal = " ".join(nombreFinalArray)


# DECLARANDO LAS FUNCIONES DE VALIDACIÓN
def validarNumero(msj, min, max):
    pass

def validarNombre(msj, min):
    while True:
        try:
            nombre = input(msj).strip()
            
            if len(nombre) < 0:
                print("Error: La cadena de texto no puede estar vacía.")
                continue
        
        except Exception as e:
            print("Ha ocurrido un error al ingresar su nombre. Inténtelo de nuevo.")
        except:
            print("Ha ocurrido un error inesperado. Inténtelo de nuevo o comuníquese con un administrador.")


# DECLARANDO LAS FUNCIONES PRINCIPALES



# CREANDO LA ESTRUCTURA DEL PROGRAMA
print("\n\n", "=" * 35, sep="")
print(" " * 9, "ADIVINA EL NÚMERO", sep="")
print("=" * 35)


while isVerdadero:
    nombre = validarNombre("¿Dime tu Nombre?", 0)