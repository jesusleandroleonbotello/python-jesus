# Creación de una función que emule el funcionamiento de la ya existente función
# incorporada "max()". Esta función aceptará tres valores como entrada.


# IMPORTANDO LAS BIBLIOTECAS
import sys


# DEFINIENDO LAS VARIABLES PRINCIPALES
limiteMaximo = sys.maxsize
limiteMinimo = -(sys.maxsize)


# DEFINIENDO LAS FUNCIONES
def maximoDeTres(num1, num2, num3):
    while True:
        try:
            numero1 = int(input(num1))
            numero2 = int(input(num2))
            numero3 = int(input(num3))
            
            if numero1 == limiteMaximo or numero1 == limiteMinimo:
                print("Error en num1: Ingrese un dato numérico válido.")
                continue
            
            elif numero2 == limiteMaximo or numero2 == limiteMinimo:
                print("Error en num2: Ingrese un dato numérico válido.")
                continue
            
            elif numero3 == limiteMaximo or numero3 == limiteMinimo:
                print("Error en num3: Ingrese un dato numérico válido.")
                continue
            break
        
        except ValueError:
            print("Ha ocurrido un error al ingresar los números.")
        except:
            print("Ha ocurrido un error inesperado. Inténtelo de nuevo o comuníquese con un administrador.")
    
    if numero1 > numero2 and numero1 > numero3:
        return numero1
    elif numero2 > numero1 and numero2 > numero3:
        return numero2
    elif numero3 > numero1 and numero3 > numero2:
        return numero3
    elif (numero1 == numero2 and numero1 == numero3) or (numero2 == numero1 and numero2 == numero3) or (numero3 == numero1 and numero3 == numero2):
        return True
    


resultadoNumeroMaximo = maximoDeTres("\nIngrese el número 1: ", "Ingrese el número 2: ", "Ingrese el número 3: ")

print("\n", "=" * 35)
if resultadoNumeroMaximo == True:
    print("¡Los números son iguales!")
else:
    print(f"El número {resultadoNumeroMaximo} es el más alto de todos.")