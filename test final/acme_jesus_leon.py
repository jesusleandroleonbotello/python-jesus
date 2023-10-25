# debemos hacer un programa que leva los datos de un archivo y los meta al json organizados
import json
import csv
ruta = "test final/archivo_met.json"
ruta2 = "test final/archivo.csv"
datos_agru = {}

def leer_codigo():
    while True:
        try:
            n = int(input("Ingrese el codigo del observatorio: "))
            if n < 1:
                print("Codigo inválido. Debe ser mayor a cero")
                continue
            return n
        except ValueError:
            print("Error al ingresar el codigo.")

def leer_nombre():
    while True:
        try:
            nom = input("Ingrese el nombre del observatorio: ")
            nom = nom.strip()
            if len(nom) == 0 or not nom.isalnum():
                print("Nombre inválido")
            elif nom.isdigit(): # esto es para que el nombre no sean solo numeros 
                print("Nombre inválido")
                continue
            return nom
        except Exception as e:
            print("Error al ingresar el nombre del observatorio.", e)

def leer_temperatura_min():
    while True:
        try:
            nmin = float(input("Ingrese la temperatura minima: "))
            if nmin == "":
                print("La temperatura es numerica")
                continue
            return nmin
        except ValueError:
            print("Error al ingresar la cantidad.")

def leer_temperatura_max():
    while True:
        try:
            nmax = float(input("Ingrese la temperatura maxima: "))
            if nmax == "":
                print("La temperatura debe ser un numero")
                continue
            return nmax
        except ValueError:
            print("Error al ingresar la cantidad.")

def leer_fecha():
    while True:
        try:
            fecha = input("Ingrese la fecha 2000/06/30: ")
            fecha.strip("/")
            if fecha == 0 or fecha == "":
                print("la fecha debe ser numeros")
                continue
            return fecha
        except Exception:
            ("Ingrese bien la fecha ")

def buscar(codigo):
    with open(ruta, "r") as file:
        for codigo in file:
            if codigo in file:
                return True
        return False

def agregar_datos():
    print("ingresar los datos...")
    codigo = leer_codigo()
    nombre = leer_nombre()
    fecha = leer_fecha()
    tempemin = leer_temperatura_min()
    tempemax = leer_temperatura_max()
    # Agregar la información recolectada al diccionario.
    datos_agru[codigo] = {
        "nombre": nombre, 
        "fecha": fecha, 
        "temperatura minima": tempemin,
        "temperatura maxima": tempemax
    }
    return 
def cargar_dato():
    try:
        with open(ruta, "r") as file:
            datos_agru = json.load(file)
    except FileNotFoundError:
        datos_agru = []
    return datos_agru

def guardar_datos(datos_agru):
    with open(ruta, "a") as file:
        json.dump(datos_agru, file)

def punto2():
    with open(ruta, "r") as datosc:
        list(datosc).sort
        print(datosc)
def punto3():
    with open(ruta, "r") as datos:
        list(datos).sort(key='nombre')
        print(datos)
def buscar_codigo():
    print("\n\n©©© 3. Buscar por codigo ©©©\n")
    codigo = leer_codigo()
    existe = buscar(datos_agru,codigo)
    if existe == False:
        print("El informe con ese código no ha sido ingresado.")
        input("CONTINUAR? ""ENTER"" ")
        return
    print("\n", "=" * 30)
    print("Nombre:", datos_agru[codigo]["nombre"])
    print("Fecha:", datos_agru[codigo]["fecha"])
    print("temperatura minima:", datos_agru[codigo]["temperatura minima"])
    print("temperatura maxima:", datos_agru[codigo]["temperatura maxima"])
    input("\n Presione cualquier tecla para volver al menu...")

def mostrar_observacion(datos_agru):
    for i in range(0, len(datos_agru), 10):
        print(datos_agru[i:i+10])
        input("Presione cualquier tecla para continuar viendo...")
        print("\n")
    return datos_agru

def punto6(datos_agru):
    pass

def menu():
    print("\n╔════════════════════════════════════════════════════════════════════════════════════╗")
    print("║                              SERVICIO METEOROLÓGICO ACME                           ║")
    print("╠════════════════════════════════════════════════════════════════════════════════════╣")
    print("║ 2. ingresar los datos                                                              ║")
    print("║ 2. Listado de observatorios ordenados ascendentemente por sus códigos              ║")
    print("║ 3. Listado de observatorios ordenados ascendentemente por su nombre                ║")
    print("║ 4. Listado de observaciones de un observatorio en particular ingresando su código  ║")
    print("║ 5. Listado de cantidades de observaciones                                          ║")
    print("║ 6. Listado de todas las observaciones a nivel nacional                             ║")
    print("║ 7. Listado de todas las observaciones a nivel nacional                             ║")
    print("╚════════════════════════════════════════════════════════════════════════════════════╝")


while True:
    menu()  
    opcion = input("\nIngrese la opcion del 1 al 7: ")

    if opcion == "1":
        cargar_dato()
        agregar_datos()
        guardar_datos(datos_agru)
        print("listo")
    elif opcion == "2":
        punto2()
    elif opcion == "3":
        punto3()
    elif opcion == "4":
        buscar_codigo(datos_agru)
    elif  opcion == "5":
        mostrar_observacion()
    elif opcion == "6":
        pass
    elif opcion == "7":
            print("Gracias por usar el programa")
            break
    
# lo intente f :(