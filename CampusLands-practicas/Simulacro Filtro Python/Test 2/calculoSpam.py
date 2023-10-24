# Este programa permite el cálculo del índice de spam de correos para la empresa ACME.


# DECLARANDO LAS VARIABLES PRINCIPALES
isVerdadero = True
formatosPermitidos = ["txt", "csv", "dat"]


# DEFINIENDO LAS FUNCIONES COMPLEMENTARIAS
def abrirArchivo(param, rutaArchivo):
    lstPromedio = []
    
    try:
        fd = open(rutaArchivo, "r")

    except Exception as e:
        return [0, False]
    

    for linea in fd:
        if linea.startswith(param):
            lstPromedio.append(linea.split()[1])
    fd.close()

    for promedio in lstPromedio:
        print(promedio)
    print(len(lstPromedio))

    return promedioMath(lstPromedio)


def promedioMath(lstPromedio):
    sumaPromedios = 0

    for i in range(len(lstPromedio)):
        sumaPromedios += float(lstPromedio[i])
    
    promedioResultado = sumaPromedios / len(lstPromedio)
    
    return [promedioResultado, True]


# DEFINIENDO LAS FUNCIONES DE VALIDACIÓN
def validarNombreArchivo(msj):
    while True:
        try:
            nombreArchivo = input(msj).strip()
            nombreArchivoValidacionArray = nombreArchivo.split(" ")
            nombreArchivoArray = nombreArchivo.split(".")
            

            # Validar que el nombre del archivo introducido no contenga espacios
            if len(nombreArchivoValidacionArray) > 1:
                print("Error: El nombre del archivo no puede contener espacios.\n")
                continue

            elif len(nombreArchivoArray) < 1 or len(nombreArchivoArray) > 2:
                print("Error: El nombre del archivo a leer no puede contener caracteres especiales ni puntos y debe contener la extensión del mismo.\n")
                continue


            # Verificando que el usuario haya ingresado una extensión de archivo válida y no uno binario.
            for i in range(len(formatosPermitidos)):
                if nombreArchivoArray[-1] == formatosPermitidos[i]:
                    checked = True
                    return ".".join(nombreArchivoArray)
                checked = False
            

            # Determinar si no hubo coincidencias en la validación de archivos válidos.
            if not checked:
                print("Error: La extensión del archivo ingresado no es compatible. Ingrese archivos .txt, .csv o .dat\n")
                continue
            break

        except Exception as e:
            print("Ha ocurrido un problema al ingresar el nombre del archivo. Inténtelo de nuevo.\n")
            print(f"Error: {e}")
        except:
            print("Ha ocurrido un error inesperado. Inténtelo de nuevo o comuníquese con un administrador.\n")


def validarOpcionUsuario(msj, min, max):
    while True:
        try:
            opcionUsuario = int(input(msj))

            if opcionUsuario < min or opcionUsuario > max:
                print(f"Error: Ingrese un valor dentro del rango establecido ({min}-{max}).")
                continue
            return opcionUsuario

        except ValueError:
            print("Ha ocurrido un error al ingresar la opción digitada. Inténtelo de nuevo.")
        except:
            print("Ha ocurrido un error inesperado al ingresar la opción digitada. Inténtelo de nuevo o comuníquese con un administrador.")


# DEFINIENDO LAS FUNCIONES PRINCIPALES
def nombreArchivoLeer(msj):
    nombreArchivo = validarNombreArchivo(msj)
    rutaArchivo = f"Simulacro Filtro Python/Test 2/{nombreArchivo}"
    return rutaArchivo


def promedioSpamCorreo(param, rutaArchivo):
    return abrirArchivo(param, rutaArchivo)


# CREANDO LA ESTRUCTURA DEL ARCHIVO
print("=" * 35)
print("CALCULO DE SPAM - ACME".center(34))
print("\n")
print("=" * 35, "\n")


while isVerdadero:
    rutaArchivo = nombreArchivoLeer("\nIntroduzca el nombre del archivo que se va leer (Ejemplo: archivo.txt): ")
    promedioSpam, estadoPromedioSpam = promedioSpamCorreo("X-DSPAM-Confidence:", rutaArchivo)

    if not estadoPromedioSpam:
        continuar = validarOpcionUsuario("Algo ha ido mal al manipular el archivo. ¿Deseas volver a iniciar el programa? (1 SI / 0 NO): ", 0, 1)
        
        if continuar == 0:
            print("\n¡Gracias por usar nuestro software!")
            break

        elif continuar == 1:
            isVerdadero = True
            continue
    
    print("\n\n=== RESULTADOS ===")
    print(f"El promedio del Spam de correo electrónico es de: {promedioSpam}")

    if isVerdadero:
        continuarPrograma = validarOpcionUsuario("¿Desea continuar en el programa?: (1 SI / 0 NO): ", 0, 1)

        if continuarPrograma == 0:
            print("\n¡Gracias por usar nuestro software!")
            isVerdadero = False
        
        elif continuarPrograma == 1:
            isVerdadero = True
    
    else:
        print("\n¡Gracias por usar nuestro software!")
        break