# Este programa permite consultar y escribir información en un archivo respecto a los libros registrados
# presentes en una librería. Todas las directrices de la construcción del programa están en el ejercicio.


# IMPORTANDO LAS LIBRERIAS NECESARIAS
import json


# DECLARANDO LAS VARIABLES PRINCIPALES
isVerdadero = True
rutaFile = "Actividad 17/"


# DEFINIENDO LAS FUNCIONES COMPLEMENTARIAS
def ingresarInfoLibro(codigo, titulo, autor, precio):
    print("\n", "=== INSERTAR NUEVO LIBRO ===", "\n")
    print("Ingrese la siguiente información:")
    
    codigo = validarCodigo(codigo)
    titulo = validarTexto(titulo)
    autor = validarTexto(autor)
    precio = validarPrecio(precio)


def filtrarTexto(texto):
    textoFiltradoArray = []
    
    for i in range(len(texto)):
        if texto[i] != "":
            textoFiltradoArray.append(texto[i])
    
    textoValidacion = "".join(textoFiltradoArray)
    textoFinal = " ".join(textoFiltradoArray)
    return [textoValidacion, textoFinal]


# DEFINIENDO LAS FUNCIONES DE VALIDACIÓN
def validarOpcionUsuario(msj, min, max):
    while True:
        try:
            opcionUsuario = int(input(msj))
            
            if opcionUsuario < min or opcionUsuario > max:
                print(f"Error: Debes ingresar un valor numérico dentro del rango válido ({min}-{max}).\n")
                continue
            return opcionUsuario
        
        except ValueError:
            print("Ha ocurrido un error al ingresar la opción elegida. Inténtelo de nuevo.\n")
        except:
            print("Ha ocurrido un error inesperado. Inténtelo de nuevo o comuníquese con un administrador.\n")


def validarCodigo(msj, min):
    while True:
        try:
            codigo = int(input(msj))
            
            if codigo < min:
                print(f"Error: El código no puede ser menor a {min}. Inténtelo de nuevo.\n")
                continue
            return codigo
        
        except ValueError:
            print("Ha ocurrido un error al ingresar el código. Inténtelo de nuevo.\n")
        except:
            print("Ha ocurrido un error inesperado. Inténtelo de nuevo o comuníquese con un administrador.\n")


def validarTexto(msj, min):
    while True:
        try:
            texto = input(msj).strip()
            textoArray = texto.split(" ")
            
            if len(textoArray) < min:
                print(f"Error: El texto debe contener al menos {min} palabras.")
                continue
            textoValidacion, textoFinal = filtrarTexto(textoArray)
            
            if not textoValidacion.isalnum() or textoValidacion.isdigit() or len(textoValidacion) == 0:
                print("Error: El texto no puede contener caracteres especiales, componerse de solo números o estar vacío.")
                continue
            return textoFinal
        
        except Exception as e:
            print("Ha ocurrido un problema al ingresar la cadena de texto.")
            print(F"Error: {e}\n")
        except:
            print("Ha ocurrido un error inesperado. Inténtelo de nuevo o comuníquese con un administrador.\n")


def validarPrecio(msj, min):
    while True:
        try:
            precio = float(input(msj))
            
            if precio < min:
                print(f"Error: El valor del precio no puede ser menor a ${min:,.0f} COP.\n")
                continue
            return precio
        
        except ValueError:
            print("Ha ocurrido un error al ingresar el precio dado. Inténtelo de nuevo.")
        except:
            print("Ha ocurrido un error inesperado. Inténtelo de nuevo o comuníquese con un administrador.\n")


def validarRuta(msj, rutaFile):
    while True:
        try:
            ruta = input(msj).strip()
            rutaArray = ruta.split(".")
            
            if len(rutaArray) < 1 or len(rutaArray) > 2:
                print("Error: El nombre del archivo no puede contener puntos excepto el de la extensión. (Ejemplo: archivoDatos.txt).\n")
                continue
            
            rutaValidar, rutaFinal = filtrarTexto(rutaArray)
            
            #Finalizar validación ruta
        
        except Exception as e:
            pass


# DEFINIENDO LAS FUNCIONES PRINCIPALES
def menu(msj):
    print("\n\n", "LIBRERÍA".center(15))
    print("MENU".center(17))
    
    print("\n1. Configuración")
    print("2. Insertar Libro")
    print("3. Consultar Libro")
    print("4. Salir")
    return validarOpcionUsuario(msj, 1, 4)


def insertar(infoLibro, rutaFile):
    #Validación n°1 - Verificar si el archivo abre correctamente
    try:
        escribirArchivo = open(rutaFile, "w")
    
    except Exception as e:
        print("Ha ocurrido un error al intentar abrir el archivo. Inténtelo de nuevo.")
        print(f"Error: {e}")
        return False
    
    
    #Validación n°2 - Verificar si el archivo se escribe correctamente
    try:
        json.dump(infoLibro, escribirArchivo)
    
    except Exception as e:
        print("Ha ocurrido un error al guardar el archivo. Inténtelo de nuevo.")
        print(f"Error: {e}")
        return False
    
    escribirArchivo.close()
    return True


def consultar():
    pass


def configuracion():
    pass


# CONSTRUYENDO LA ESTRUCTURA DEL PROGRAMA
while isVerdadero:
    opcionUsuario = menu("   >> Ingrese una opción: ")
    
    if opcionUsuario == 1:
        configuracion()
    
    elif opcionUsuario == 2:
        ingresarInfoLibro("  >> Código: ", "  >> Título: ", "  >> Autor: ", "  >> Precio: ")
    
    elif opcionUsuario == 3:
        consultar()
    
    elif opcionUsuario == 4:
        isVerdadero = False
        print("Saliendo...")