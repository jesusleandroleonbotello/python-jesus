import json

def guardar_empleado(lstpersonal, ruta):
    try:
        fd = open(ruta,"w")
    except Exception as e:
        print(" errror al abrir el archivo para guardar\n",e)
        return None
    
    try:
        json.dump(lstpersonal,fd)
    except Exception as e:
        print("Error al guardar la informacion del empleado")
        return None
    fd.close()

def agregar_personal(lstpersonal):
    print("\n\n 1. agregar personal")

    id = int(input("Ingrese el id: "))
    while existe_id(id, lstpersonal):
        print(" ---> Ya existe el id")
        input()
        id = int(input("\n Ingrese el id: "))

    nombre = input("ingrese el nombre: ")
    edad = int(input("Ingrese la edad: "))
    sexo = input("Sexo (M/F): ")
    telefono = int(input("Telefono: "))

    dic_empleado = {}
    dic_empleado[id] = {"nombre":nombre,"edad":edad, "sexo":sexo, "telefono":telefono}
    lstpersonal.append(dic_empleado)
    



rutafile = ("lectura archivo/empleados.json")
def menu():
    while True:
        try:
            print("♣" *28)
            print("")
            print("♣♣♣♣♣  PRODUCTOS ACME  ♣♣♣♣♣".center(10))
            print("")
            print("♣" *28)
            print("")
            print("1. Agregar")
            print("2. Modificar")
            print("3. Eliminar")
            print("4. ver")
            print("5. Salir")
            print("")
            op = int(input(">>> Opción (1-5)? "))
            if op < 1 or op > 5:
                print("Opción no válida. Escoja de 1 a 5.")
                input("Presione cualquier tecla para continuar...")
                continue
            return op
        except ValueError:
            print("Opción no válida. Escoja de 1 a 5.")
            input("Presione cualquier tecla para continuar...")

def cargar_inf(lstpersonal, ruta):
    try:
        fd = open(ruta,"r")
    except Exception as e:
        try:
            fd = open(ruta, "w")
        except Exception as d:
            print("error al cargar el archivo\n",d)
            return None
        try:
            linea = fd.readline()
            if linea.strip() != "":

            lstpersonal = json.load(fd)
        except Exception as e:
            print("error al cargar la informacion")
            fd.close()
            return lstpersonal
        