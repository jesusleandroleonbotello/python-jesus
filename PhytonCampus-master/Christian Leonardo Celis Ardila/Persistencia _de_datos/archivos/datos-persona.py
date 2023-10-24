import json 


def menu():

    while True: 
        print("*"*4+ "Registro del personal" + "*"*4)
        print("1. Agregar")
        print("2. Modificar")
        print("3. Eliminar ")
        print("4. Ver")
        print("5. Salir")
    
        while True:
            try:
                opcion = int(input("Digite opcion: "))
                if(opcion<1 or opcion>5):
                    print("opcion no valida, digite nuevamente: ")
                    continue
                break
            except Exception as e:
                print("No valido",e)
        return opcion
    

def cargarinfo(lstPersonal,rutaFile):
    try:
        fd = open(rutaFile,"r")
    except Exception as e:
        try:
            fd = open(rutaFile,"w")
        except Exception as d:
            print("Error al intentar abrir el archivo",d)
            fd.close()
            return None
    try:
        linea = fd.readline()
        if linea.strip() != "":
            fd.seek(0)
            lstPersonal = json.load(fd)
        else:
            lstPersonal = []
    except Exception as e:
        print("Error al cargar la informacion",e)
        return None
    
    
    print(lstPersonal)
    fd.close()
    return lstPersonal

def agregarPersonal(lstPersonal,rutaFile):
    print("\n1. Agregar Personal")
    id = int(input("ingrese el ID: "))
    while existeid(id,lstPersonal):
        print("persona existe en id")
        input()
        id = int(input("ingrese el ID: "))

    nombre = input("Nombre =?: ")
    edad = input("Edad =?: ")
    sexo = input("Sexo =?: ")
    telefono = input("Telefono =?: ")
    DictEmpleado = {}
    DictEmpleado[id] = {"nombre":nombre, "edad": edad,"sexo":sexo , "telefono":telefono}
    lstPersonal.append(DictEmpleado)

    if guardarPersonal(lstPersonal,rutaFile) == True:
        print("EMpleado guardado con exito")
    else:
        print("Ocurrio un error al guardar el empleado")

def existeid(id,lstPersonal):
    for datos in lstPersonal:
        K = int(list(datos.keys())[0])
        if(K == id):
            return True
        else:
            return False

def guardarPersonal(lst,rutaFile):
    try:
        fd = open(rutaFile,"w")
    except Exception as e:
        print("error",e) 
        return None
    
    try:
        json.dump(lst,fd)
    except Exception as e:
        print("Error al guardar la información del empleado",e)

    fd.close
    return True


def borrar(lst,ruta):
    print("\n1. Agregar Personal")
    id = int(input("ingrese el ID: "))
    if not existeid(id, lst):
        print("No existe un empleado con ese ID")
        input()
        return
    for i in len(lst):
        datos = lst[i]
        K = int(list(datos.keys())[0])
        if(K == id):
            del lst[i]
            break
    if guardarPersonal(lst,ruta):
        print("EL EMPLEADO A SIDO BORRADO CON EXITO")
    else:
        print("ocurrio un error al retornar el empleado")

def main():
    lstPersonal = []
    rutafile = "Christian Leonardo Celis Ardila/Persistencia _de_datos/archivos/personal.json"
    lstPersonal = cargarinfo(lstPersonal,rutafile)
 
    opcion = menu()

    while True:
        if(opcion==1):
          agregarPersonal(lstPersonal,rutafile)
        elif(opcion==2):
            pass
        elif(opcion==3):
            pass
        elif(opcion==4):
            pass
        elif(opcion==5):
            return 
    
    
        while True:
            try:
                opcion = int(input("Desea realizar otra operacion? si: 0 no: 5: "))
                if((opcion<0 or opcion > 5) or ( opcion>0 and opcion<5)):
                    print("Rango no valido")
                    continue
                break
            except Exception as e:
                print("Error numero no valido")
        
main()