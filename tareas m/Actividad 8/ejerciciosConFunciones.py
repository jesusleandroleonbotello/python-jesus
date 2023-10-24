# Este programa contendrá una serie de pequeños programas donde el usuario
# pueda elegir alguno de los problemas solucionados mediante un menú y que se 
# ejecute ese ejercicio en específico.



# DEFINIENDO LAS VARIABLES PRINCIPALES
isVerdadero = True


# DEFINICIÓN DE FUNCIONES
def menu(msj):
    while True:
        try:
            print("\n", "===== MENU =====")
            print("1- Cálculo de la combinatoria")
            print("2- Convertir texto a número")
            print("3- Calcular el IVA de una factura")
            print("4- Salir")
            opcionUsuario = int(input(msj))
            
            if opcionUsuario < 1 or opcionUsuario > 4:
                print("Error: Debes ingresar una opción válida (1-4).")
                continue
            return opcionUsuario
        
        except ValueError:
            print("Ha ocurrido un error en la digitación del número.")
        except:
            print("Ha ocurrido un error inesperado. Inténtelo de nuevo o comuníquese con un administrador.")


def calculoCombinatoria(n, k):
    while True:
        try:
            valorN = int(input(n))
            valorK = int(input(k))
            
            if valorN < 0 or valorK < 0:
                print("Error: No puedes ingresar números negativos. Ingresa números positivos.\n")
                continue
            elif valorN < valorK:
                print("Error: El total de elementos debe ser mayor a los elementos por grupo.\n")
                continue
            
            combinacionResultado = factorial(valorN) / (factorial(valorN-valorK) * factorial(valorK))
            return combinacionResultado
        
        except ValueError:
            print("Ha ocurrido un problema al ingresar los números. Inténtelo de nuevo.")
        except:
            print("Ha ocurrido un error inesperado. Es probable que la salida contenga un número muy elevado.")
            print("Inténtelo de nuevo o comuníquese con un administrador.\n")
            
def factorial(num):
    resultadoFactorial = 1
    
    for i in range(1, num + 1):
        resultadoFactorial *=  i
    
    return resultadoFactorial


def textoNumero(msj):
    while True:
        try:
            stringFiltrado = ""
            stringUsuario = input(msj)
            stringUsuario = stringUsuario.strip()
            
            if len(stringUsuario) == 0:
                print("Error: No puedes enviar una entrada de texto vacía.")
                continue
            
            #Algoritmo para filtrar el string a solo dígitos
            for i in range(len(stringUsuario)):
                if stringUsuario[i].isdigit():
                    stringFiltrado += stringUsuario[i]
    
            return stringFiltrado
            
        except Exception as e:
            print("Ha ocurrido un problema al ingresar la entrada de texto.")
            print(f"Error: {e}")


def factura(costoSinIva, ivaPorcentaje):
    while True:
        try:
            valorProducto = float(input(costoSinIva))
            
            if valorProducto < 0:
                print("Error: No puedes introducir un valor negativo, solo se acepta números positivos.")
                continue
                    
            valorProductoFinal = valorProducto + (valorProducto * ivaPorcentaje) / 100
            return valorProductoFinal
                        
        except ValueError:
            print("Ha ocurrido un error al digitar el valor del producto. Inténtelo de nuevo.")
        except:
            print("Ha ocurrido un error inesperado. Inténtelo de nuevo o comuníquese con un administrador.")



# ESTRUCTURA DEL PROGRAMA
while isVerdadero:
    opcionUsuario = menu("   >> Escoja una opción (1-4): ")

    if opcionUsuario == 1:
        print("\n", "==== Indicaciones ====")
        print("En la fórmula de combinaciones el valor N indica el total de elementos y el valor K los elementos por grupos.\n")    
        resultadoCombinatoria = calculoCombinatoria("Valor n: ", "Valor k: ")

        print("\n", "*** RESULTADO ***")
        print(f"Puedes realizar: C(n,k) = {resultadoCombinatoria:.0f} combinaciones distintas.")
        input("Presione cualquier tecla para continuar... ")

    elif opcionUsuario == 2:
        resultadoString = textoNumero("\nEscribe a continuación letras y números: ")
        
        print("\n", "*** RESULTADO ***")
        print(f"Tu cadena de texto de solo números quedó así: {resultadoString}")
        input("Presione cualquier tecla para continuar...")

    elif opcionUsuario == 3:
        continuar = True
        valorProductosIva = 0
        
        while continuar:
            #Estableciedo un valor de IVA fijo. Esto para evitar que el usuario tenga que 
            #digitar múltiples veces un valor de IVA que permanecerá en el mismo valor.
            
            while True:
                try:
                    valorIva = int(input("\nIngrese el porcentaje del IVA: "))
                    
                    if valorIva < 0 or valorIva > 100:
                        print("Error: No puedes introducir un valor menor a 0 o mayor a 100 como porcentaje del IVA.")
                        continue
                    break
                
                except ValueError:
                    print("Ha ocurrido un error al ingresar el porcentaje de IVA. Inténtelo de nuevo.")
                except:
                    print("Ha ocurrido un error inesperado. Inténtelo de nuevo o comuníquese con un administrador.")
            
            
            #Obteniendo los resultados del IVA.
            while True:
                try:
                    items = int(input("¿Cuántos elementos desea agregar?: "))
                    
                    if items < 0:
                        print("\nError: Debes ingresar un valor positivo entero.")
                        continue
                    
                    for i in range(items):
                        if items < 0:
                            print("Error: No puedes ingresar números negativos.")
                            continue
                        valorProductosIva += factura("\nIngrese el valor del producto para calcular su IVA: ", valorIva)
                    break
                
                except ValueError:
                    print("Ha ocurrido un error. Ingrese un número entero positivo válido.")
                except:
                    print("Ha ocurrido un error inesperado. Inténtelo de nuevo o póngase en contacto con el administrador.")
            
            
            #Imprimiendo en pantalla los valores recolectados
            print("\n", "*** RESULTADO ***")
            print(f"Con el precio del IVA, la factura ingresada tiene un valor de: ${valorProductosIva:,.2f}")
            input("Presione cualquier tecla para continuar...")
            
            
            #Preguntar al usuario si desea continuar agregando elementos por si se le ha 
            #olvidado ingresar algún dato adicional o necesita cambiar el valor del IVA.
            while True:
                try:
                    continuarPrograma = input("¿Deseas continuar? S/N: ")
                    
                    if continuarPrograma.upper() == "S":
                        continuar = True
                    
                    elif continuarPrograma.upper() == "N":
                        continuar = False
                        print("Regresando al menú...")
                                                
                    elif continuarPrograma.upper() != "S" or continuarPrograma.upper() != "N":
                        print("Error: Has digitado una opción inválida.")
                        print("Escribe \"S\" para continuar o \"N\" para salir y regresar al menú.")
                        continue
                    break
                    
                except Exception as e:
                    print("Ha ocurrido un error al ingresar la opción.")
                    print(f"Error: {e}")
                
    elif opcionUsuario == 4:
        print("¡Gracias por usar nuestro programa!")
        isVerdadero = False