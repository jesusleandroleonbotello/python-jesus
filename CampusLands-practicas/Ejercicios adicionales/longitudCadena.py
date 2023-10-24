# Este programa calculará la longitud de una lista o cadena dada, realizando una función 
# similar a la ya existente "len()" incorporada en Python.


# DEFINIENDO LAS FUNCIONES NECESARIAS
def longitud(elemento):
    count = 0
    
    while True:
        try:
            if type(elemento) == int or type(elemento == float):
                print("Error: Debes ingresar una cadena de texto o una lista.")
                continue
            break
        
        except Exception as e:
            print(f"Ha ocurrido un problema. Error {e}")
        except:
            print("Ha ocurrido un error desconocido. Inténtelo de nuevo o comuníquese con un administrador.")
    
    
    for i in elemento:
        count += i
    
    return count


# ESTRUCTURANDO EL PROGRAMA
while True:
    try:
        print("Elige alguna de las siguientes opciones:")
        eleccionEntradaUsuario = int(input("1 para Lista o 2 para String >> "))
        
        if eleccionEntradaUsuario < 1 or eleccionEntradaUsuario > 2:
            print("Error: Introduce un valor que corresponda a las opciones mostradas.")
            continue
        break
    
    except ValueError:
        print("Ha ocurrido un error al ingresar el número. Inténtelo de nuevo.")
    except:
        print("Ha ocurrido un error desconocido. Inténtelo de nuevo o comuníquese con un administrador.")
    

# De acuerdo a la decisión tomada por el usuario, 
if eleccionEntradaUsuario == 1:
    listaUsuario = []
    isVerdadero = True
    
    while isVerdadero:
        listaUsuario.append(input("Ingrese un valor a la lista: "))
        
        continuar = input("¿Desea continuar? (S/N): ")
    
    
    

resultadoLongitud = longitud()

print(f"La longitud de la {eleccionEntradaUsuario} ingresado es de: {resultadoLongitud}")



# TERMINAR EL CÓDIGO MENOS OPTIMIZADO DEL MUNDO XD