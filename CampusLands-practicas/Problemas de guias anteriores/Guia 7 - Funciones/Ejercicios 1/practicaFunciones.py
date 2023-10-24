# Este programa contiene tres pequeños programas y un menú donde el usuario
# podrá dirigirse a la solución de dichos sub-programas.


# DEFINIENDO LAS VARIABLES PRINCIPALES
isVerdadero = True


# DEFINIENDO LAS FUNCIONES DE VALIDACIÓN
def validarOpcionUsuario(opcion, min, max):
    while True:
        try:
            opcionUsuario = int(input(opcion))
            
            if opcionUsuario < 1 or opcionUsuario > 4:
                print(f"Error: Ingrese una opción válida ({min}-{max}).\n")
                continue
            return opcionUsuario
        
        except ValueError:
            print("Ha ocurrido un error al ingresar la opción seleccionada. Inténtelo de nuevo.\n")
        except:
            print("Ha ocurrido un error inesperado. Inténtelo de nuevo o comuníquese con un administrador.\n")


def validarNumero(num, min, max):
    while True:
        try:
            numero = int(input(num))
            
            if numero < int(min) or numero > int(max):
                print(f"Error: Ingrese un número entero válido ({min}-{max}).\n")
                continue
            return numero
        
        except ValueError:
            print("Ha ocurrido un error al ingresar el número. Inténtelo de nuevo.\n")
        except:
            print("Ha ocurrido un error inesperado. Inténtelo de nuevo o comuníquese con un administrador.\n")


def validarTexto(text):
    while True:
        try:
            texto = input(text).strip()
            
            if len(texto) == 0:
                print("Error: La cadena de texto no puede estar vacía.\n")
                continue
            return texto        
        
        except Exception as e:
            print("Ha ocurrido un problema al ingresar el texto. Inténtelo de nuevo.")
            print(f"Error: {e}\n")
        except:
            print("Ha ocurrido un error inesperado. Inténtelo de nuevo o comuníquese con un administrador.\n")



# DEFINIENDO LAS FUNCIONES PERTINENTES
def menu(msj):
    print("\n", "==== MENU ====")
    print("\n1. Factorial de un número")
    print("2. Calcular el salario de un empleado")
    print("3. Calcular palabras en un párrafo")
    print("4. Salir")
    
    return validarOpcionUsuario(msj, 1, 4)


def factorialNumero(msj):
    print("\n", "*** FACTORIAL DE UN NÚMERO ***")
    
    numero = validarNumero(msj, 0, 1558)
    multiplicar = 1
    
    for i in range(1, numero + 1):
        multiplicar *= i
    
    return multiplicar


def salarioEmpleado(msj, valorHora):
    print("\n", "*** CALCULAR EL SALARIO DE UN EMPLEADO ***")
    
    horasTrabajadas = validarNumero(msj, 0, 720)
    horaLimite = 40
    valorHoraExtra = valorHora * 1.5
    
    if horasTrabajadas < 40:
        return horasTrabajadas * valorHora
    
    elif horasTrabajadas > 41:
        horasExtra = horasTrabajadas - horaLimite
        salarioParcial = horaLimite * valorHora
        
        salarioFinal = salarioParcial + (horasExtra * valorHoraExtra)
        return salarioFinal


def palabrasParrafo(msj):
    print("\n", "*** CALCULAR PALABRAS EN UN PÁRRAFO ***")
    
    while True:
        try:
            texto = validarTexto(msj)
            textoArray = texto.split(" ")
            count = 0

            if texto.isdigit():
                print("Error: La cadena de texto no puede contener solo números.\n")
                continue
            
            for e in textoArray:
                if e != "":
                    count += 1
            return count
            
        except Exception as e:
            print("Ha ocurrido un problema al ingresar el texto. Inténtelo de nuevo.")
            print(f"Error: {e}\n")
        except:
            print("Ha ocurrido un error inesperado. Inténtelo de nuevo o comuníquese con un administrador.\n")



# CREANDO LA ESTRUCTURA DEL PROGRAMA
while isVerdadero:
    opcionUsuario = menu("   >> Ingrese una opción (1-4): ")
    
    if opcionUsuario == 1:
        factorial = factorialNumero("Ingrese un número: ")
        print(f"El factorial del número ingresado es de {factorial}")
        input("\nPresione cualquier tecla para continuar...")
    
    elif opcionUsuario == 2:
        valorHora = 10
        salario = salarioEmpleado("Ingrese las horas trabajadas: ", valorHora)
        
        print(f"El salario del empleado es de: ${salario:,.2f} USD.")
        input("\nPresione cualquier tecla para continuar...")
    
    elif opcionUsuario == 3:
        cantidadPalabras = palabrasParrafo("Ingrese un texto o párrafo: ")
        print(f"La cantidad de palabras que tiene el texto ingresado es de: {cantidadPalabras} palabras")
        input("\nPresione cualquier tecla para continuar...")
    
    elif opcionUsuario == 4:
        print("Saliendo...")
        isVerdadero = False