import json


def menu():
    while True:
        print("*"*4+ "Registro del personal" + "*"*4)
        print("1. Agregar")
        print("2. Modificar")
        print("3. Eliminar ")
        print("4. Ver")
        print("5. Salir")
        try:
            opcion = int(input("Digite opcion: "))
            if(opcion<1 or opcion>5):
                print("opcion no valida, digite nuevamente: ")
                continue
            break
        except Exception as e:
            print("No valido",e)
        return opcion


def leernombre(msg):
    while True:
        try:
            n = input(msg)
            n.strip()
            if(n==0 or not n.isalnum()):
                print("\nNombre no valido\n")
                continue
            return n
        except Exception as e:
            print("\nError al ingresar el nombre\n", e)




def leerid(msg):
    while True:
        try:
            n = int(input(msg))
            if(n<0):
                print("\nValor invalido, debe ser mayor a cero\n")
                continue
            return n
        except Exception as e:
            print("\nError\n",e)


def leertelefono(msg):
    while True:
        try:
            n = int(input(msg))
            if(n<0):
                print("\nValor invalido, debe ser mayor a cero\n")
                continue
            return n
        except Exception as e:
            print("\nError\n",e)


def leerSexo(msg):
    while True: 
        try:
            sexo = input(msg).upper
            if(sexo!="M" or sexo != "F" or sexo != "N"):
                print("\nSexo no valido\n")
                continue
            return sexo
        except Exception as e:
            print("\nError\n",e)




def leerEdad(mensaje):
    while True:
        try:
            n = int(input(mensaje))
            if(n<0):
                print("\nValor invalido, debe ser mayor a cero\n")
                continue
            return n
        except Exception as e:
            print("\nError\n",e)



def ModificarEmpleado(lstEmpleado, rutafile):
    id = leerid("Digite id empleado a modificar")
    if existeid(id,lstEmpleado) == True:
        while True:
            try:
                print("\nOPCIONES A MODIFICAR")
                print("1. Nombre")
                print("2. Edad")
                print("3. Sexo\n")
                print("4. Telefono\n")


                select = int(input("\nDigite la opcion del empleado que quiere modificar: "))
                if(select<1 or select>4):
                    print("Error numero fuera de rango")
                    continue
                break
            except Exception as e:
                print("Error", e)
        if(select == 1):
            Nombre = leernombre("\nDigite nuevo nombre; ")
            for i in len(lstEmpleado):
                i[id]["nombre"] = Nombre
        elif(select ==2):
            Edad = leerEdad("\nDigite nueva edad: ")
        elif(select == 3):
            Sexo = leerSexo("\nDigite nuevo Sexo: ")
        elif(select == 3):
            Sexo = leertelefono("\nDigite nuevo Telefono: ")
            print(lstEmpleado)
            if guardarPersonal(lstEmpleado,rutafile) == True:
                print("EMpleado guardado con exito")
            else:
                print("Ocurrio un error al guardar el empleado")
                return
    else:
        print("Usuario no encontrado")
        return



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
    id = leerid("ingrese el ID: ")
    while existeid(id,lstPersonal):
        print("persona existe en id")
        input()
    id = leerid("ingrese el ID: ")
    nombre = leernombre("Nombre =?: ")
    edad = leerEdad("Edad =?: ")
    sexo = leerSexo("Sexo =? (M/F/N): ")
    telefono = leertelefono("Telefono =?: ")
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
rutafile = "Reviews/personal.json"
lstPersonal = cargarinfo(lstPersonal,rutafile)
opcion = menu()


while True:
if(opcion==1):
agregarPersonal(lstPersonal,rutafile)
elif(opcion==2):
ModificarEmpleado(lstPersonal,rutafile)
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
