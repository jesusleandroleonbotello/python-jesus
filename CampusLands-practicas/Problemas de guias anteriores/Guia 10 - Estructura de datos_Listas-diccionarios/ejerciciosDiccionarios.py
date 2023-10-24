# Este programa contendrá la solución de dos ejercicios: La Serie Armónica Alternada y la verificación 
# de si un numero es positivo o no y apartir de ahí, generar todos los números primos dentro de un rango
# establecido por entrada de usuario.


# DECLARANDO LAS VARIABLES PRINCIPALES
isVerdadero = True


# DEFINIENDO LAS FUNCIONES COMPLEMENTARIAS



# DEFINIENDO LAS FUNCIONES DE VALIDACIÓN
def validarOpcionUsuario(msj, min, max):
    while True:
        try:
            opcionUsuario = int(input(msj))
            
            if opcionUsuario < min or opcionUsuario > max:
                print(f"Error: Debes ingresar una opción numérica válida ({min}-{max}).\n")
                continue
            return opcionUsuario
        
        except ValueError:
            print("Ha ocurrido un error al ingresar su opción. Inténtelo de nuevo.\n")
        except:
            print("Ha ocurrido un error inesperado. Inténtelo de nuevo o comuníquese con un administrador.\n")


def validarNumero(msj, min = 0, max = 999999999):
    while True:
        try:
            numero = int(input(msj))

            if numero < min or numero > max:
                print(f"Error: El número debe estar dentro del rango permitido ({min}-{max}).\n")
                continue
            return numero
            
        except ValueError:
            print("Ha ocurrido un error al ingresar el número. Inténtelo de nuevo.\n")
        except:
            print("Ha ocurrido un error inesperado. Inténtelo de nuevo o comuníquese con un administrador.\n")


# DEFINIENDO LAS FUNCIONES PRINCIPALES
def menu(msj):
    print("\n", "=" * 35)
    print("Solución ejercicios - Guía n°10".center(37))
    print("", "=" * 35)
    
    print("\n1. Serie Armónica Alternada")
    print("2. Generación de Números Primos")
    print("3. Salir")
    return validarOpcionUsuario(msj, 1, 3)


def serieArmonicaAlternada(msj):
    print("\n\n", "*** SERIE ARMÓNICA ALTERNADA ***")
    numeroTerminos = validarNumero(msj)
    suma = 0
    signo = 1  #Permite alternar entre el signo positivo y negativo.
    
    if numeroTerminos == 0:
        return 0
    else:
        for i in range(1, numeroTerminos + 1):
            terminoSuma = signo * (1 / i)
            suma += terminoSuma
            signo *= -1
    
    return [numeroTerminos, suma]


def generacionNumerosPrimos(n, m):
    print("\n\n", "*** GENERACIÓN DE NÚMEROS PRIMOS ***", "\n")
    print("Ingrese la siguiente información:")
    
    rangoInicio = validarNumero(n, 2)
    rangoFinal = validarNumero(m, rangoInicio)
    numerosPrimos = []
    
    
    for i in range(rangoInicio, rangoFinal + 1):
        count = 0
        for j in range(2, i):
            if i % j == 0:
                count += 1
        
        if count >= 1:
            pass
        else:
            numerosPrimos.append(i)
    
    return numerosPrimos


# CREANDO LA ESTRUCTURA DEL PROGRAMA
while isVerdadero:
    opcionUsuario = menu("   >> Escoja una opción: ")
    
    if opcionUsuario == 1:
        cantidadTerminos, resultado = serieArmonicaAlternada("Introduzca la cantidad de términos a usar para realizar la serie armónica alternada: ")
        
        print(f"\nHas ingresado {cantidadTerminos} términos a la función, por tanto, el resultado es de: {resultado}.")
        input("Presione cualquier tecla para continuar...")
    
    elif opcionUsuario == 2:
        resultado = generacionNumerosPrimos("Rango inicial: ", "Rango final: ")
        count = 0  #Esta variable permitirá contar cuantas veces se ha iterado el bucle for
        
        for n in resultado:
            print(f"{n} |", end=" ")
            count += 1
        print("\nCantidad números primo:", len(resultado))
        
        input("\nPresione cualquier tecla para continuar...")
    
    elif opcionUsuario == 3:
        salir = validarOpcionUsuario("\n¿Seguro que desea salir? (1 SI / 0 NO): ", 0, 1)
        
        if salir == 0:
            input("Regresando al menú principal. Presione cualquier tecla para continuar...")
            isVerdadero = True

        elif salir == 1:
            print("¡Gracias por usar nuestro software!")
            isVerdadero = False