# Este programa permitirá la creación de 6 tipos de matrices cuadradas distintas, cada una con un 
# patrón de números o letras diferente. El usuario podrá elegir el tamaño y matriz a generar.


# DECLARANDO LAS VARIABLES PRINCIPALES
isVerdadero = True


# DEFINIENDO LAS FUNCIONES COMPLEMENTARIAS



# DEFINIENDO LAS FUNCIONES DE VALIDACIÓN
def validarOpcionUsuario(msj, min, max):
    while True:
        try:
            opcionUsuario = int(input(msj))
            
            if opcionUsuario < min or opcionUsuario > max:
                print(f"Error: Debes elegir un valor numérico dentro del rango permitido ({min}-{max}).\n")
                continue
            return opcionUsuario
        
        except ValueError:
            print("Ha ocurrido un error al ingresar la opción elejida. Inténtelo de nuevo.\n")
        except:
            print("Ha ocurrido un error inesperado. Inténtelo de nuevo o comuníquese con un administrador.\n")


def validarNumero(msj, min, max):
    pass


#soy tu próxima función, ¡defíneme! :D


# DEFINIENDO LAS FUNCIONES DE MATRICES
def matrizSecuenciaFilas():
    pass


def matrizSecuenciaRepetitiva():
    pass


def matrizDiagonal():
    pass


def matrizDiagonalInvertida():
    pass


def matrizEscaleraRellenada():
    pass


def matrizEscaleraRellenadaInvertida():
    pass


def matrizSecuenciaColumnas():
    pass


def matrizEscalera():
    pass


# DEFINIENDO LAS FUNCIONES PRINCIPALES
def menu(msj):
    print("\n", "CREACIÓN DE MATRICES".center(25))
    print("MENÚ".center(27))
    
    print("\n1. Matriz de secuencia numérica por filas")
    print("2. Matriz de secuencia numérica repetitiva")
    print("3. Matriz numérica en diagonal")
    print("4. Matriz numérica en diagonal invertida")
    print("5. Matriz numérica con forma de escalera")
    print("6. Matriz numérica con forma de escalera invertida")
    print("7. Matriz de secuencia numérica por columnas")
    print("8. Matriz alfabética de secuencia repetitiva con forma de escalera")
    print("9. Salir")
    return validarOpcionUsuario(msj, 1, 9)


def crearMatriz(escala = 6, tipoMatriz = 1):
    pass


def mostrarMatriz(matriz):
    pass


# CREANDO LA ESTRUCTURA DEL PROGRAMA
while isVerdadero:
    opcionUsuario = menu("   >> Escoja una opción: ")
    
    if opcionUsuario == 1:
        matrizSecuenciaFilas()
        input("Presione cualquier tecla para continuar...")
    
    elif opcionUsuario == 2:
        matrizSecuenciaRepetitiva()
        input("Presione cualquier tecla para continuar...")
    
    elif opcionUsuario == 3:
        matrizDiagonal()
        input("Presione cualquier tecla para continuar...")
    
    elif opcionUsuario == 4:
        matrizDiagonalInvertida()
        input("Presione cualquier tecla para continuar...")
    
    elif opcionUsuario == 5:
        matrizEscaleraRellenada()
        input("Presione cualquier tecla para continuar...")
    
    elif opcionUsuario == 6:
        matrizEscaleraRellenadaInvertida()
        input("Presione cualquier tecla para continuar...")
    
    elif opcionUsuario == 7:
        matrizSecuenciaColumnas()
        input("Presione cualquier tecla para continuar...")
    
    elif opcionUsuario == 8:
        matrizEscalera()
        input("Presione cualquier tecla para continuar...")
    
    elif opcionUsuario == 9:
        isVerdadero = False
        print("Saliendo...")