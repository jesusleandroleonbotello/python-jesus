# Este programa se enfoca en la creación de matrices, esto a partir de una entrada de usuario que 
# permita determinar las filas y columnas que desea que contengan las matrices a generar. En este 
# ejemplo en específico, todas las mtrices se generarán de manera cuadriculada.


# DEFINIENDO LAS VARIABLES PRINCIPALES



# DECLARANDO LAS FUNCIONES COMPLEMENTARIAS



# DECLARANDO LAS FUNCIONES DE VALIDACIÓN
def validarNumero(msj, iterar, min, max):
    listaNumerosValidados = []
    count = 0
    
    while True:
        try:
            while count != iterar:
                numero = int(input(msj))
                
                if numero < min or numero > max:
                    print(f"Error: Ingrese un valor numérico válido dentro del rango permitido ({min}-{max})\n")
                    continue
                
                listaNumerosValidados.append(numero)
                count += 1
            
            return listaNumerosValidados
                
        except ValueError:
            print("Ha ocurrido un error al ingresar el número. Inténtelo de nuevo\n")
        except:
            print("Ha ocurrido un error inesperado. Inténtelo de nuevo o comuníquese con un administrador.\n")


def validarOpcionUsuario(msj, min, max):
    while True:
        try:
            opcionUsuario = int(input(msj))
            
            if opcionUsuario < min or opcionUsuario > max:
                print(f"Error: Debes ingresar un número numérico válido ({min}-{max}).\n")
                continue
            return opcionUsuario
        
        except ValueError:
            pass


# DECLARANDO LAS FUNCIONES NECESARIAS
def crearMatriz(matrizCuadrado, tipoMatriz):
    if matrizCuadrado:
        columnas, = validarNumero("¿Cuántas filas desea que tenga la matriz?: ", 1, 1, 75)
        filas = 1 * columnas
        matriz = []
        
        
        if tipoMatriz == 1:
            numero = 0

            for i in range(columnas):
                fila = [numero] * columnas
                matriz.append(fila)

        elif tipoMatriz == 2:
            decimal = 0.0

            for i in range(columnas):
                fila = [decimal] * columnas
                matriz.append(fila)

        elif tipoMatriz == 3:
            string = "Hola"

            for i in range(columnas):
                fila = [string] * columnas
                matriz.append(fila)

        elif tipoMatriz == 4:
            dato = None

            for i in range(columnas):
                fila = [dato] * columnas
                matriz.append(fila)

        
        return matriz

    else:
        pass


def mostrarMatriz(matriz):
    print("\n")
    for f in range(len(matriz)):
        for c in range(len(matriz[f])):
            print(matriz[f][c], end=" ")
        print("")


# CREANDO LA ESTRUCTURA DEL PROGRAMA
tipoMatriz = validarOpcionUsuario("\n¿Qué tipo de dato contendrá la matriz? (1 Numero / 2 Decimal / 3 String / 4 None): ", 1, 4)
matriz = crearMatriz(True, tipoMatriz)
mostrarMatriz(matriz)