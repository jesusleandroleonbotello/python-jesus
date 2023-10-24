nombre = []
ids = []
horas = []
valorhora = []

empleados = [ids,nombre,horas,valorhora]

def menu():
    print("\n*"*4+ "Menu Acme" + "*"*4)
    print("1. Agregar empleado")
    print("2. Modificar empleado")
    print("3. Buscar empleado ")
    print("4. Eliminar empleado")
    print("5. listar empleados")
    print("6. listar nomina de un empleado")
    print("7. listar nomina de todos los empleados")
    print("8.salir\n")

    while True:
        try:
            opcion = int(input("\nDigite opcion: "))
            if(opcion<1 or opcion>8):
                print("\nopcion no valida, digite nuevamente: ")
                continue
            break
        except Exception as e:
            print("\nNo valido\n",e)
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
                print("\nValor invalido, debe ser mayor a cero o menor a 12\n")
                continue
            return n
        except Exception as e:
            print("\nError\n",e)


def leerhorasempleado(msg):
    while True:
        try:
            n = int(input(msg))
            if(n<0 or n>160):
                print("\nValor invalido, debe ser mayor a cero y menor a 160\n")
                continue
            return n
        except Exception as e:
            print("\nError\n",e)

def leervalorHora(msg):
    while True:
        try:
            n = float(input(msg))
            if(n<8000 or n>150000):
                print("\nValor invalido, debe ser mayor a 8.000 y menor a 150.000\n")
                continue
            return n
        except Exception as e:
            print("\nError\n",e)


def AgregarEmpleado():
    Id = leerid("\nDigite el id del empleado: ")
    ids.append(Id)
    Nombre = leernombre("Digite el nombre  del empleado: ")
    nombre.append(Nombre)
    HorasTrabajadas = leerhorasempleado("Digite horas trabajadas  del empleado: ")
    horas.append(HorasTrabajadas)
    ValorHora = leervalorHora("Digite el valor de la hora  del empleado: ")
    valorhora.append(ValorHora)

def ModificarEmpleado():
    imprimirNombre()
    while True:
        try:
            op = int(input("\nDigite el numero del empleado que quiere modificar"))
            if(op<1):
                print("Error")
                continue
            break
        except Exception as e:
            print("\nError\n" , e)

    imprimirempleado(op-1)

    while True:
        try:
            print("\nOPCIONES A MODIFICAR")
            print("1. Nombre")
            print("2. Horas Trabajadas")
            print("3. Valor Hora\n")

            select = int(input("\nDigite el numero del empleado que quiere modificar: "))
            if(select<1 or select>3):
                print("Error numero fuera de rango")
                continue
            break
        except Exception as e:
            print("Error", e)

    if(select == 1):
        Nombre = leernombre("\nDigite nuevo nombre; ")
        nombre[op-1] = Nombre
    elif(select ==2):
        horast = leerhorasempleado("\nDigite nueva hora trabajada empleado: ")
        horas[op-1] = horast
    elif(select == 3):
        valore = leervalorHora("\nDigite el nuevo valor de la hora: ")
        valorhora[op-1] = valore

    print("Usuario Modificado")
    imprimirempleado(op-1)


def imprimirNombre():
    for i in range(len(nombre)):
        print(f"Empleado {i+1}:  {nombre[i]}")



def BuscarEmpleado(id):
    indx = -1
    for i in ids:
        if(i == id):
            indx = ids.index(i)
    if(indx == -1):
        print("*"*30)
        print("El id no existe")
        print("*"*30)
        return indx
    else:
        imprimirempleado(indx)
        return int(indx)
    

def imprimirempleado(id):
    print("\n","*"*30)
    print(f"El id del empleado es: {empleados[0][id]}")
    print(f"El Nombre: {empleados[1][id]}")
    print(f"Las Horas trabajadas: {empleados[2][id]}")
    print(f"El Valor de la hora: {empleados[3][id]}")
    print("*"*30,"\n")

def eliminarEmpleado(idex):
    nombre.remove(nombre[idex])
    ids.remove(ids[idex])
    horas.remove(horas[idex])
    valorhora.remove(valorhora[idex])
    print("Usuario eliminado")
    return

def ListarEmpleado():
    cont = 0
    for i in range(len(ids)):
        cont += 1
        imprimirempleado(i)
        
        if(cont==5):
            op = input("\nDesea continuar? si: 0 no: s ")
            
            if(op.lower()=="s"):
                return
            else:
                cont = 0
    return            


def listarnominaempleado(id):
    eps = 0.04
    pension = 0.04
    Sneto = 0
    Sbruto = 0
    Auxilio = 0
    Valorhora = valorhora[id]
    hora = horas[id]
    Sbruto = Valorhora * hora
    
    if(Sbruto < 1160000 ):
        Auxilio = 140606
    Sneto = Sbruto +  Auxilio  - (Sbruto* eps) - (Sbruto*pension)
    print("*"*30)    
    print(f"****Nomina*** empleado con id {ids[id]}")
    print(f"El salario bruto es: {Sbruto}")
    print(f"El auxilio de transporte es: {Auxilio}")
    print(f"El Salario Neto es : {Sneto}")
    print("*"*30)
 
    return

def Listarnominatodosemp():
    for i in range(len(ids)):
        listarnominaempleado(i)
          
    return
    
def main():

    while True:
        opcion = menu()

        if(opcion == 1):
            AgregarEmpleado()
        elif(opcion == 2):
            ModificarEmpleado()
        elif(opcion==3):
            Id = leerid("\nDigite el id del empleado a buscar: ")
            BuscarEmpleado(Id)
        elif(opcion==4):
            idex = leerid("\nDigite el id del empleado a eliminar: ")
            idel = BuscarEmpleado(idex)
            if(idel!=-1):
                eliminarEmpleado(idel)
        elif(opcion==5):
                ListarEmpleado()
        elif(opcion==6):
            idex = leerid("\nDigite el id del empleado para obtener su nomina: ")
            idel = BuscarEmpleado(idex)
            if(idel!=-1):
                listarnominaempleado(idel)
        elif(opcion==7):
            Listarnominatodosemp()  
        elif(opcion==8):
            salida = input("\nDesea Salir de la aplicacion? si: s / No: n")
            if(salida.lower() != "s"):
                print("Continuemos")
            else:
                return 0

r = main()
if(r == 0):
    print("Adios")
