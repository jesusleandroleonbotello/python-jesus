# Este programa permite agregar, modificar, eliminar y listar de forma ascendente varios 
# productos usando paginación. El software está destinado a la empresa ACME.


# DEFINIENDO LAS VARIABLES PRINCIPALES
isVerdadero = True
diccionarioProducto = {}


# DEFINIENDO LAS FUNCIONES DE VALIDACIÓN
def validarID(msj):    
    while True:
        try:
            id = int(input(msj))
            
            if id < 1:
                print("Error: El ID debe ser superior o igual a 1, no se acepta números negativos.\n")
                continue
            return id

        except ValueError:
            print("Ha ocurrido un error al ingresar el ID del producto. Inténtelo de nuevo.\n")
        except:
            print("Ha ocurrido un error inesperado. Inténtelo de nuevo o comuníquese con un administrador.\n")


def validarNombreProducto(msj):
    while True:
        try:
            listaNombreProducto = []
            nombreProducto = input(msj).strip()
            nombreProductoArray = nombreProducto.split(" ")
            
            for i in range(len(nombreProductoArray)):
                if nombreProductoArray[i] != "":
                    listaNombreProducto.append(nombreProductoArray[i])
            
            nombreProductoValidar = "".join(listaNombreProducto).lower()
            nombreProductoFinal = " ".join(listaNombreProducto).title()
            
            if len(listaNombreProducto) == 0 or not nombreProductoValidar.isalnum() or len(nombreProductoValidar) == 0 or nombreProductoValidar.isdigit():
                print("\nError: Has ingresado un nombre inválido.")
                continue
            return nombreProductoFinal

        except Exception as e:
            print("\nHa ocurrido un problema al ingresar el nombre del producto.")
            print(f"Error: {e}")
        except:
            print("Ha ocurrido un error inesperado. Inténtelo de nuevo o comuníquese con un administrador.\n")


def validarPrecio(msj):
    while True:
        try:
            precio = int(input(msj))
            
            if precio < 0:
                print("Error: Has ingresado un precio con números negativos.\n")
                continue
            return precio

        except ValueError:
            print("Ha ocurrido un error al ingresar el precio del producto. Inténtelo de nuevo.\n")
        except:
            print("Ha ocurrido un error inesperado. Inténtelo de nuevo o comuníquese con un administrador.\n")


def validarCantidad(msj):
    while True:
        try:
            cantidad = int(input(msj))
            
            if cantidad < 0:
                print("Error: No puedes ingresar números negativos.\n")
                continue
            
            elif cantidad > 100000000:
                print("Error: El máximo permitido en inventario es de 100 millones.\n")
                continue
            return cantidad

        except ValueError:
            print("Ha ocurrido un error al ingresar la cantidad del producto. Inténtelo de nuevo.\n")
        except:
            print("Ha ocurrido un error inesperado. Inténtelo de nuevo o comuníquese con un administrador.\n")


def validarOpcionUsuario(msj, min, max):
    while True:
        try:
            opcionUsuario = int(input(msj))
            
            if opcionUsuario < min or opcionUsuario > max:
                print(f"\nError: Introduce una opción válida ({min}-{max}).")
                continue
            return opcionUsuario
        
        except ValueError:
            print("\nHa ocurrido un error al ingresar la opción. Inténtelo de nuevo.")
        except:
            print("\nHa ocurrido un error inesperado. Inténtelo de nuevo o comuníquese con un administrador.")



# DEFINIENDO LAS FUNCIONES ADICIONALES
def extraerIdDiccionario(diccionario):
    print(diccionario)
    return diccionario.keys()


# DEFINIENDO LAS FUNCIONES PERTINENTES
def menu(msj):
    print("\n")
    print("=" * 18)
    print("  PRODUCTOS ACME")
    print("=" * 18)
    
    print("\n1. Agregar producto")
    print("2. Modificar producto")
    print("3. Eliminar producto")
    print("4. Listar varios productos")
    print("5. Estrategia de mercadeo")
    print("6. Salir")
    
    return validarOpcionUsuario(msj, 1, 6)


def agregarProducto():
    print("\n")
    id = validarID("Ingrese el ID: ")
    nombreProducto = validarNombreProducto("Ingrese el nombre del producto: ")
    precio = validarPrecio("Ingrese el precio del producto: ")
    cantidad = validarCantidad("Ingrese la cantidad del producto: ")

    diccionarioProducto[id] = [nombreProducto, precio, cantidad]
    

def modificarProducto(opcionUsuario):    
    # test = extraerIdDiccionario(diccionarioProducto)
    # print(test, len(test))

    # for i in test:
    #     print(i, test)
    #     print("N°\t\t\t", "ID\t\t\t", "Nombre")
    #     print(f"{i+1}\t\t\t", f"ID: {diccionarioProducto[i]}\t\t\t", f"Nombre: {diccionarioProducto[i['0']]}")
    
    
    # Error de dict_key a pesar de usar keys() para lista XD
    pass
    

def eliminarProducto():
    pass


def listarProductos():
    pass


def estrategiaMercadeo():
    pass


# CREANDO LA ESTRUCTURA DEL PROGRAMA
while isVerdadero:
    opcionUsuario = menu("   >> Escoja una opción (1-6): ")
    
    if opcionUsuario == 1:        
        agregarProducto()
    
    elif opcionUsuario == 2:
        # print("\n", "=" * 35)
        # print("¿Qué deseas modificar?")
        
        # print("\n1. Nombre del Producto")
        # print("2. Precio del producto")
        # print("3. Cantidad del producto")
        # optionUser = validarOpcionUsuario("   >> Escoja una opción (1-3): ", 1, 3)
        
        # modificarProducto(optionUser)
        pass
    
    elif opcionUsuario == 3:
        pass
    
    elif opcionUsuario == 4:
        pass
    
    elif opcionUsuario == 5:
        pass
    
    elif opcionUsuario == 6:
        isVerdadero = False