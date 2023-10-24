# Programa que permite la creación e introducción de datos personales de los empleados en una
# empresa de forma persistente e irrepetible: ID, Nombre, Edad, Sexo, Teléfono.


# IMPORTANDO LAS LIBRERIAS NECESARIAS
import json


# DECLARANDO LAS VARIABLES PRINCIPALES
isVerdadero = True
rutaArchivo = "Actividad 16/datosEmpleados.json"
listaPersonalEmpresa = []


# DEFINIENDO LAS FUNCIONES COMPLEMENTARIAS
def filtrarTexto(texto):
    textoArray = texto.split(" ")
    textoFiltradoArray = []
    
    for i in range(len(textoArray)):
        if textoArray[i] != "":
            textoFiltradoArray.append(textoArray[i])
    
    textoValidar = "".join(textoFiltradoArray).lower()
    textoFinal = " ".join(textoFiltradoArray).title()
    
    return [textoFiltradoArray, textoValidar, textoFinal]


# DEFINIENDO LAS FUNCIONES DE VALIDACIÓN
def validarOpcionUsuario(msj, min, max):
    while True:
        try:
            opcionUsuario = int(input(msj))
            
            if opcionUsuario < min or opcionUsuario > max:
                print(f"Error: Ingresa un número válido dentro del rango establecido: ({min}-{max}).")
                continue
            return opcionUsuario
        
        except ValueError:
            print("Ha ocurrido un error al ingresar el número. Inténtelo de nuevo.")
        except:
            print("Ha ocurrido un error inesperado. Inténtelo de nuevo o comuníquese con un administrador.")


def validarId(msj, min):
    while True:
        try:
            id = int(input(msj))
            
            if id < min:
                print(f"Error: El ID no puede ser menor a {min}.")
                continue
            return id
        
        except ValueError:
            print("Ha ocurrido un error al ingresar el ID del empleado. Inténtelo de nuevo.")
        except:
            print("Ha ocurrido un error inesperado. Inténtelo de nuevo o comuníquese con un administrador")


def validarNombre(msj, min):
    while True:
        try:
            nombre = input(msj).strip()
            nombreFiltradoArray, nombreValidar, nombreFinal = filtrarTexto(nombre)
            
            if nombreValidar.isdigit():
                print("Error: El nombre no puede ser numérico\n")
                continue
            
            elif not nombreValidar.isalnum():
                print("Error: El nombre no puede contener caracteres especiales\n")
                continue
                
            elif len(nombreFiltradoArray) < min:
                print("Error: Debes ingresar al menos un nombre y un apellido\n")
                continue
            return nombreFinal
        
        except Exception as e:
            print("Ha ocurrido un problema al ingresar el nombre\n")
            print(f"Error: {e}")
        except:
            print("Ha ocurrido un error inesperado. Inténtelo de nuevo o comuníquese con un administrador\n")


def validarEdad(msj, min):
    while True:
        try:
            edad = int(input(msj))
            
            if edad < min:
                print(f"Error: El empleado no puede tener menos de {min} años de edad.")
                continue
            return edad
        
        except ValueError:
            print("Ha ocurrido un error al ingresar la edad del empleado. Inténtelo de nuevo.")
        except:
            print("Ha ocurrido un error inesperado. Inténtelo de nuevo o comuníquese con un administrador")


def validarSexo(msj):
    while True:
        try:
            sexoUser = input(msj)
            sexo = filtrarTexto(sexoUser)[-1]
            
            if sexo != "M" and sexo != "F":
                print("Error: Debes introducir una de las dos opciones válidas (M/F).")
                continue
            return sexo
            
        except Exception as e:
            print("Ha ocurrido un error al ingresar el sexo del empleado.")
            print(f"Error: {e}")
        except:
            print("Ha ocurrido un error inesperado. Inténtelo de nuevo o comuníquese con un administrador")


def validarTelefono(msj, min, max):
    while True:
        try:
            telefono = input(msj)
            telefonoArray, prefijo, telefonoFinal = filtrarTexto(telefono)
            
            if len(prefijo) < 3:
                print("Error: Introduzca un prefijo internacional válido.")
                continue
            
            elif len(telefonoFinal) < min and len(telefonoFinal) > max:
                print(f"Error: Introduzca un número telefónico válido con el siguiente rango de dígitos {min}-{max}")
                continue
            return [telefonoArray, prefijo, telefonoFinal]
        
        except Exception as e:
            print("Ha ocurrido un problema al registrar el número ingresado.")
            print(f"Error: {e}")
        except:
            print("Ha ocurrido un error inesperado. Inténtelo de nuevo o comuníquese con un administrador")


# DEFINIENDO LAS FUNCIONES PRINCIPALES
def menu(msj, min, max):
    print("\n\n", "==== REGISTRO DE PERSONAL ====".center(40))
    print("MENU\n".center(41))
    
    print("1. Agregar empleado")
    print("2. Editar empleado")
    print("3. Eliminar empleado")
    print("4. Ver empleado")
    print("5. Salir del programa")
    return validarOpcionUsuario(msj, min, max)


def agregarEmpleado():
    print("\n", "*** AGREGAR EMPLEADO ***\n")
    
    print("Ingrese a continuación la siguiente información sobre el empleado:")
    id = validarId("  >> ID: ", 1)
    nombre = validarNombre("  >> Nombre: ", 2)
    edad = validarEdad("  >> Edad: ", 16)
    sexo = validarSexo("  >> Sexo (M/F): ")
    telefono = validarTelefono("  >> Teléfono (Ej: +57 3154157800): ", 8, 15)[-1]
    
    dictEmpleado = {}
    dictEmpleado[id] = {"nombre": nombre, "edad": edad, "sexo": sexo, "telefono": telefono}
    listaPersonalEmpresa.append(dictEmpleado)
    
    print(listaPersonalEmpresa)
    input("Ingrese cualquier tecla para continuar...")
    

def editarEmpleado(msj):
    pass


def eliminarEmpleado(msj):
    pass


def verEmpleado(msj):
    pass


# CREANDO LA ESTRUCTURA DEL PROGRAMA
while isVerdadero:
    opcionUsuario = menu("   >> Ingrese una opción: ", 1, 5)
    
    if opcionUsuario == 1:
        agregarEmpleado()
    
    elif opcionUsuario == 2:
        pass
    
    elif opcionUsuario == 3:
        pass
    
    elif opcionUsuario == 4:
        pass
    
    elif opcionUsuario == 5:
        isVerdadero = False
        print("\nHasta luego!")