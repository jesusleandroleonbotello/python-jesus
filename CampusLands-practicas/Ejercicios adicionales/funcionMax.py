# Creación de una función que emule el funcionamiento de la ya existente función
# incorporada "max()". Se hará de tal forma que opere con solo dos números.



# IMPORTAR LAS RESPECTIVAS LIBRERÍAS
import sys


# DEFINIR LAS VARIABLES PRINCIPALES
limiteMaximo = sys.maxsize
limiteMinimo = -(sys.maxsize)


# DEFINIENDO LAS FUNCIONESS
def maxNumber(num1, num2):
    while True:
        try:
            numero1 = int(input(num1))
            numero2 = int(input(num2))
            
            if numero1 == limiteMaximo or numero2 == limiteMaximo or numero1 == limiteMinimo or numero2 == limiteMinimo:
                print("Error: No puedes insertar un número mayor o menor al que puede aceptar tu sistema.")
                continue
            break
            
        except ValueError:
            print("Ha ocurrido un error al ingresar los números.")
        except:
            print("Ha ocurrido un error inesperado. Inténtelo de nuevo o comuníquese con un administrador.")
    
    
    if numero1 > numero2:
        return numero1
    
    elif numero2 > numero1:
        return numero2
    
    elif numero1 == numero2:
        return True


# IMPRIMIENDO LA SALIDA
numeroMayor = maxNumber("\nIngrese el número 1: ", "Ingrese el número 2: ")

print("\n", "=" * 35)
if numeroMayor == True:
    print("¡Los números son iguales!")

else:
    print(f"El número mayor es el {numeroMayor}")