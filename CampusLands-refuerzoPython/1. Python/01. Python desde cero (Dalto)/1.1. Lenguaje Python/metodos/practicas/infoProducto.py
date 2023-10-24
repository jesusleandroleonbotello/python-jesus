# Programa para practicar el tema de cadenas de texto.


# DECLARANDO LAS VARIABLES PRINCIPALES
isVerdadero = True
dictProductos = {}


# DEFINIENDO LAS FUNCIONES COMPLEMENTARIAS
def costeTotal(precioProducto):
    precio, cantidad = precioProducto
    return float(precio * cantidad)


def filtrarTexto(texto):
    textoFiltrarArray = []
    for i in range(len(texto)):
        if texto[i] != "":
            textoFiltrarArray.append(texto[i])
    
    textoValidar = "".join(textoFiltrarArray)
    textoFinal = " ".join(textoFiltrarArray)
    
    return [textoValidar, textoFinal]


def existeCodigo(cod):
    validarExisteCodigo = dictProductos.get(cod)
    
    if validarExisteCodigo == None:
        return False
    
    else:
        return True


# DEFINIENDO LAS FUNCIONES DE VALIDACIÓN
def validarOpcionUsuario(msj, min, max):
    while True:
        try:
            opcionUsuario = int(input(msj))
            
            if opcionUsuario < min or opcionUsuario > max:
                print(f"Error: Debes elegir una opción numérica dentro del rango válido ({min}-{max}).\n")
                continue
            return opcionUsuario
        
        except ValueError:
            print("Ha ocurrido un error al ingresar la opción elegida. Inténtelo de nuevo.\n")
        except:
            print("Ha ocurrido un error inesperado. Inténtelo de nuevo o comuníquese con un administrador.\n")


def validarCodigo(msj, min, max):
    while True:
        try:
            codigo = input(msj).strip()
            codigoArray = codigo.split(" ")
            
            if len(codigo) == 0:
                print("Error: El campo de texto no puede estar vacío.\n")
                continue
            codigoValidar, codigoFinal = filtrarTexto(codigoArray)
            
            if len(codigoValidar) < min or len(codigoValidar) > max:
                print(f"Error: Ingrese un código válido, estos tienen entre {min}-{max} caracteres entre letras y números sin espacios.\n")
            
            elif codigoFinal.count(" ") > 0:
                print("Error: El código no puede contener espacios.\n")
            
            elif codigoValidar.isdigit() or not codigoValidar.isalnum() or len(codigoValidar) == 0:
                print("Error: El campo de texto no puede estar compuesto de números, ni estar vacía o contener caracteres especiales.\n")
                continue
            
        
        except Exception as e:
            print("Ha ocurrido un problema al ingresar el código. Inténtelo de nuevo.")
            print(f"Error: {e}.\n")
        except:
            print("Ha ocurrido un error inesperado. Inténtelo de nuevo o comuníquese con un administrador.\n")


def validarTexto(msj, min):
    while True:
        try:
            texto = input(msj).strip()
            textoArray = texto.split(" ")
            
            if len(textoArray) < min:
                print(f"Error: El texto debe tener al menos {min} palabras.\n")
                continue
            textoValidar, textoFinal = filtrarTexto(textoArray)
            
            if textoValidar.isdigit() or not textoValidar.isalnum() or len(textoValidar) == 0:
                print("Error: El texto no puede tener caracteres especiales, componerse de números o estar vacío.\n")
                continue
            return textoFinal
        
        except Exception as e:
            print("Ha ocurrido un error al ingresar el texto. Inténtelo de nuevo.\n")
        except:
            print("Ha ocurrido un error inesperado. Inténtelo de nuevo o comuníquese con un administrador.\n")


def validarPrecio(msj, min):
    while True:
        try:
            precio = float(input(msj))
            
            if precio < min:
                print("\nError: El precio ingresado no puede ser menor que ${min} EUR.\n")
                continue
            return precio
        
        except ValueError:
            print("Ha ocurrido un error al ingresar el precio. Inténtelo de nuevo.\n")
        except:
            print("Ha ocurrido un error inesperado. Inténtelo de nuevo o comuníquese con un administrador.\n")


def validarNumero(msj, min):
    while True:
        try:
            numero = int(input(msj))
            
            if numero < min:
                print("\nError: El número ingresado no puede ser menor que {min}.\n")
                continue
            return numero
        
        except ValueError:
            print("Ha ocurrido un error al ingresar el número. Inténtelo de nuevo.\n")
        except:
            print("Ha ocurrido un error inesperado. Inténtelo de nuevo o comuníquese con un administrador.\n")


# DEFINIENDO LAS FUNCIONES PRINCIPALES
def menu(msj):
    print("\n\n", "=== MENU ===")
    print("1. Ingresar Producto")
    print("2. Mostrar Productos")
    print("3. Salir")
    return validarOpcionUsuario(msj, 1, 3)


def ingresarProducto(code, text, price, num):
    print("\n", "=== INGRESAR PRODUCTO ===", "\n")
    
    print("Ingrese la siguiente información: ")
    codigo = validarCodigo(code, 1, 1)
    producto = validarTexto(text, 1)
    precio = validarPrecio(price, 50)
    numero = validarNumero(num, 0)
    
    return [producto, precio, numero]
    

def mostrarInformacion(infoProducto):
    print("\n", "*** RESULTADOS ***", "\n")
    
    print("{:<5} {:<35} {:<17} {:<10} {:<17}".format("N°", "NOMBRE PRODUCTO", "PRECIO UNITARIO", "UNIDADES", "COSTE TOTAL"))
    


# CREANDO LA ESTRUCTURA DEL PROGRAMA
while isVerdadero:
    opcionUsuario = menu("   >> Ingrese una opción: ")
    
    if opcionUsuario == 1:
        infoProducto = ingresarProducto("Código: ", "Nombre Producto: ", "Precio: ", "Cantidad disponible: ")
        
    elif opcionUsuario == 2:
        mostrarInformacion(infoProducto)
    
    elif opcionUsuario == 3:
        isVerdadero = False
        print("Saliendo...")