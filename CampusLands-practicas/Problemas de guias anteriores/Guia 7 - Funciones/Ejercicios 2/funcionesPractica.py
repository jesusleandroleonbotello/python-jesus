# Este programa contiene tres soluciones a ejercicios individuales que podrán ser
# accedidos mediante el uso de funciones, donde el usuario elejirá en un menú que 
# solución desea ejecutar.


# DEFINIR LAS VARIABLES PRINCIPALES
isVerdadero = True


# DECLARANDO LAS FUNCIONES COMPLEMENTARIAS
def factorial(num):
    multiplicar = 1
    
    for i in range(1, int(num) + 1):
        multiplicar *= i
    
    return multiplicar

def filtrarTexto(text):
    textoArray = text.split(" ")
    textoArrayFiltrada = []
    
    for i in range(len(textoArray)):
        if textoArray[i] != "":
            textoArrayFiltrada.append(textoArray[i])
    
    textoFinal = "".join(textoArrayFiltrada)
    return textoFinal


# DEFINIENDO LAS FUNCIONES DE VALIDACIÓN
def validarOpcionUsuario(num, min, max):
    while True:
        try:
            opcion = int(input(num))
            
            if opcion < int(min) or opcion > int(max):
                print(f"Error: Introduce una opción válida ({min}-{max}).\n")
                continue
            return opcion
        
        except ValueError:
            print("Ha ocurrido un error al ingresar la opción elejida. Inténtelo de nuevo.\n")
        except:
            print("")

def validarNumero(num, min, max):
    while True:
        try:
            numero = int(input(num))
            
            if numero < min:
                print(f"Error: No puedes elegir un valor menor a {min}.\n")
                continue
            
            # "max" será negativo si es "False", será "True" si contiene algún valor.
            if max:
                if numero > max:
                    print(f"Error: No puedes elegir un valor mayor a {max}.\n")
                    continue

            return numero
        
        except ValueError:
            print("Ha ocurrido un error al ingresar la opción elejida. Inténtelo de nuevo.\n")
        except:
            print("Ha ocurrido un error inesperado. Inténtelo de nuevo o comuníquese con un administrador.\n")

def validarTexto(text, min):
    while True:
        try:
            texto = input(text).strip()
            
            if len(texto) == min or texto.isdigit():
                print("Error: El texto NO puede estar vacía o tener solo números.\n")
                continue
            return filtrarTexto(texto)
        
        except Exception as e:
            print("Ha ocurrido un problema al momento de ingresar la cadena de texto.\n")
            print(f"Error: {e}")
        except:
            print("Ha ocurrido un error inesperado. Inténtelo de nuevo o comuníquese con un administrador.\n")


# DEFINIENDO LAS FUNCIONES IMPORTANTES
def menu(msj):
    print("\n", "======== MENU ========")
    print("\n1. Cálculo de la combinatoria")
    print("2. Convertir texto a número")
    print("3. Calcular el IVA de una factura")
    print("4. Salir")
    return validarOpcionUsuario(msj, 1, 4)

def calculoCombinatoria(num1, num2):
    print("\n", "*** CÁLCULO DE LA COMBINATORIA ***")
    
    n = validarNumero(num1, 1, False)
    k = validarNumero(num2, 1, n)
    # El objetivo del "False" al invocar "validarNumero()" para la variable "n" es para que cuando se
    # ingrese el valor de "k", se asegure el programa que ese valor no supera a "n". Ese condicional
    # está dentro de otro condicional cuya validación es el valor de "False"
    
    return (factorial(n)) / (factorial(k) * (factorial(n-k)))

def textoNumero(msj):
    print("\n", "*** CONVERTIR TEXTO A NÚMERO ***")
    
    texto = validarTexto(msj, 0)
    textoFiltrarArray = list()
    
    for n in texto:
        if n.isdigit():
            textoFiltrarArray.append(n)
    
    textoNumeros = "".join(textoFiltrarArray)
    return textoNumeros

def ivaFactura(valor, iva):
    print("\n", "*** CALCULAR EL IVA DE UNA FACTURA ***")
    
    valorProducto = validarNumero(valor, 0, False)
    valorIva = (valorProducto * iva) / 100
    
    return valorProducto + valorIva


# CREANDO LA ESTRUCTURA DEL PROGRAMA
while isVerdadero:
    opcionUsuario = menu("   >> Ingrese una opción (1-4): ")
    
    if opcionUsuario == 1:
        combinatoria = calculoCombinatoria("Ingrese el número total de elementos: ", "Ingrese el número de elementos por grupo: ")
        
        print(f"\nPuedes realizar: C(n,k) = {combinatoria:.0f} combinaciones distintas.")
        input("Presione cualquier tecla para continuar...")
    
    elif opcionUsuario == 2:
        textoFiltradoNumero = textoNumero("Ingrese el texto a filtrarle los números: ")
        
        print(f"Tu cadena de texto quedó así: {textoFiltradoNumero}")
        input("\nPresione cualquier tecla para continuar...")
    
    elif opcionUsuario == 3:
        valorTotal = ivaFactura("Introduce el valor del producto: ", 19)
        
        print(f"El precio total del producto con IVA es: ${valorTotal:,.0f} COP")
        input("\nPresione cualquier tecla para continuar...")
    
    elif opcionUsuario == 4:
        print("\nSaliendo...")
        isVerdadero = False