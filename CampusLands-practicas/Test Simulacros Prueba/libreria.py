# Este programa permite almacenar información respecto a los libros que hay en una librería.
# Con ello, el programa podrá recuperar información anteriormente escrita en disco, así como realizar
# distintas acciones con la información.


# IMPORTANDO LAS LIBRERIAS NECESARIAS
import json


# DECLARANDO LAS VARIABLES PRINCIPALES
isVerdadero = True
rutaFile = "Test Simulacros Prueba/informacionLibros.json"


# DEFINIENDO LAS FUNCIONES COMPLEMENTARIAS
def filtrarTexto(texto):
    textoFiltradoArray = []
    
    for i in range(len(texto)):
        if texto[i] != "":
            textoFiltradoArray.append(texto[i])
    
    textoValidar = "".join(textoFiltradoArray)
    textoFinal = " ".join(textoFiltradoArray)
    return [textoValidar, textoFinal]


def guardarLibro(listaLibros, rutaFile):
    #Validar si se abre correctamente el archivo .json
    try:
        escribirArchivo = open(rutaFile, "w")
    
    except Exception as e:
        print("Ha ocurrido un problema al guardar el libro.")
        print(f"Error: {e}")
        return False
    
    #Validar si se escribe correctamente la información en el archivo
    try:
        json.dump(listaLibros, escribirArchivo)
    
    except Exception as e:
        print("Ha ocurrido un problema al guardar la información del libro.")
        print(f"Error: {e}")
        return False
    
    escribirArchivo.close()
    return True


def existeCodigo(codigo, listaLibros):
    if codigo in listaLibros:
        return True
    
    return False
    #Corregir error de que no encuentra elementos duplicados


def cargarInformacion(listaLibros, rutaFile):
    #Validación n°1 - Abrir archivo
    try:
        abrirArchivo = open(rutaFile, "r")
    
    except Exception as e:
        try:
            abrirArchivo = open(rutaFile, "w")
        except Exception as d:
            print("Error: Ha ocurrido un problema al intentar abrir el archivo, inténtelo de nuevo.")
            print(f"Error: {d}.\n")
            return False
    
    #Validación n°2 - Cargar información del archivo al programa
    try:
        lineaArchivo = abrirArchivo.readline()
        
        if lineaArchivo.strip() != "":
            abrirArchivo.seek(0)
            listaLibros = json.load(abrirArchivo)
        
        else:
            listaLibros = []
    
    except Exception as e:
        print("Error: Ha ocurrido un problema al cargar la información. Inténtelo de nuevo.")
        print(f"Error: {e}.\n")
        return False
    
    abrirArchivo.close()
    return listaLibros


# DEFINIENDO LAS FUNCIONES DE VALIDACIÓN
def validarOpcionUsuario(msj, min, max):
    while True:
        try:
            opcionUsuario = int(input(msj))
            
            if opcionUsuario < min or opcionUsuario > max:
                print(f"Error: Debes ingresar una opción numérica dentro del rango válido ({min}-{max}).\n")
                continue
            return opcionUsuario
        
        except ValueError:
            print("Ha ocurrido un error al ingresar su opción. Inténtelo de nuevo.\n")
        except:
            print("Ha ocurrido un error inesperado. Inténtelo de nuevo o comuníquese con un administrador.\n")


def validarTexto(msj, min, max = False):
    while True:
        try:
            texto = input(msj).strip()
            textoArray = texto.split(" ")
            
            if not max:
                if len(textoArray) < min:
                    print(f"Error: El texto ingresado debe contener al menos {min} palabras.\n")
                    continue

                textoValidar, textoFinal = filtrarTexto(textoArray)
                if not textoValidar.isalnum() or textoValidar.isdigit() or len(textoValidar) == 0:
                    print("Error: El texto no puede contener caracteres especiales, estar vacía o componerse por sólo números.\n")
                    continue
                
            else:
                if len(textoArray) < min or len(textoArray) > max:
                    print(f"Error: El texto ingresado debe contener al menos {min} palabras y no exceder las {max} palabras.\n")
                    continue
                
                textoValidar, textoFinal = filtrarTexto(textoArray)
                if not textoValidar.isalnum() or len(textoValidar) == 0:
                    print("Error: El texto no puede contener caracteres especiales, estar vacía o componerse por sólo números.\n")
                    continue
                
            return textoFinal
        
        except Exception as e:
            print("Ha ocurrido un problema al ingresar la cadena de texto.")
            print(f"Error: {e}.\n")
        except:
            print("Ha ocurrido un error inesperado. Inténtelo de nuevo o comuníquese con un administrador.\n")


def validarPrecio(msj, min):
    while True:
        try:
            precio = float(input(msj))
            
            if precio < min:
                print(f"Error: El precio ingresado no puede ser menor que ${min:,.0f} COP.\n")
                continue
            return precio
        
        except ValueError:
            print("Ha ocurrido un error al ingresar el precio indicado. Inténtelo de nuevo.\n")
        except:
            print("Ha ocurrido un error inesperado. Inténtelo de nuevo o comuníquese con un administrador.\n")


# DEFINIENDO LAS FUNCIONES PRINCIPALES
def menu(msj):
    print("\n\n", "Programa Librería".center(25))
    print("Menú".center(26))
    
    print("\n1. Insertar Libro")
    print("2. Consultar Libro")
    print("3. Editar Información Libro")
    print("4. Borrar libro")
    print("5. Listar libros")
    print("6. Salir")
    return validarOpcionUsuario(msj, 1, 6)


def insertarLibro(codigo, titulo, autor, precio, rutaFile):
    print("\n\n", "=== AGREGAR LIBRO ===", "\n")
    print("Ingrese la siguiente información:")
    codigoLibro = validarTexto(codigo, 1, 1)
    
    while existeCodigo(codigo, listaLibros):
        print("El código ingresado ya ha sido registrado")
        input("Presione Enter para continuar...")
        
        codigoLibro = validarTexto(codigo, 1, 1)
    
    titulo = validarTexto(titulo, 1)
    autor = validarTexto(autor, 1)
    precio = validarPrecio(precio, 50)
    
    dicLibro = {}
    dicLibro[codigoLibro] = {"titulo": titulo, "autor": autor, "precio": precio}
    
    listaLibros.append(dicLibro)
    
    if guardarLibro(listaLibros, rutaFile):
        print(f"El libro '{titulo}' bajo el código '{codigoLibro}' ha sido registrado correctamente.")
        input("Presione cualquier tecla para continuar...")
    
    else:
        print("Error: La información del libro no se guardó correctamente. Inténtelo de nuevo.")
        input("Presione cualquier tecla para continuar...")
    

def consultarLibro():
    pass


def editarLibro():
    pass


def borrarLibro():
    pass


def listarLibros():
    print("\n\n", "=== LISTAR LIBROS ===", "\n")
    
    print("¿Cómo desea listar los libros?")
    print("1. Listar libros por orden de nombre")
    print("2. Listar libros por orden de autor")
    print("3. Listar libros por orden de precio")
    opcionUsuarioListar = validarOpcionUsuario("  >> Ingrese una opción (Digite 0 para regresar): ", 0, 3)
    
    
    if opcionUsuarioListar == 0:
        input("Regresando al menú principal...")
        return False
    
    elif opcionUsuarioListar == 1:
        pass
    
    elif opcionUsuarioListar == 2:
        pass
    
    elif opcionUsuarioListar == 3:
        pass


# CREANDO LA ESTRUCTURA DEL PROGRAMA
listaLibros = []
listaLibros = cargarInformacion(listaLibros, rutaFile)

while isVerdadero:
    opcionUsuario = menu("   >> Ingrese una opción: ")
    
    if opcionUsuario == 1:
        insertarLibro("Código: ", "Título: ", "Autor: ", "Precio: ", rutaFile)
    
    elif opcionUsuario == 2:
        consultarLibro()
    
    elif opcionUsuario == 3:
        editarLibro()
    
    elif opcionUsuario == 4:
        borrarLibro()
    
    elif opcionUsuario == 5:
        listarLibros()
    
    elif opcionUsuario == 6:
        isVerdadero = False
        print("Saliendo...") #Mensaje provisional