
empleados = {}

eps = 0.04
pension = 0.04

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
    datempleado = {}
    ID = leerid("\nDigite el id del empleado: ")
    datempleado["nombre"]  = leernombre("Digite el nombre  del empleado: ")
    datempleado["horaempleado"]= leerhorasempleado("Digite horas trabajadas  del empleado: ")
    datempleado["valorhora"] = leervalorHora("Digite el valor de la hora  del empleado: ")
    empleados[ID] = datempleado
    agregarnominaempleado(ID)
    print(empleados)

    return

def ModificarEmpleado(ID):
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
        empleados[ID]["nombre"] = leernombre("\nDigite nuevo nombre; ")

    elif(select ==2):
        empleados[ID]["horaempleado"] = leerhorasempleado("\nDigite nueva hora trabajada empleado: ")
    elif(select == 3):
        empleados[ID]["valorhora"] = leervalorHora("\nDigite el nuevo valor de la hora: ")
    
    print(empleados[ID])       
    print("Usuario Modificado")
    
    


def BuscarEmpleado(ID):
    ind =  empleados.get(ID,-1)
    
    if( ind == -1):
        print(f"El empleado con id: {ID}, no existe")
        return -1
    else:
        print(empleados.get(ID,-1))
        return ID

def  eliminarEmpleado(ID):
    empleados.pop(ID)
    print("Usuario eliminado...")
    return


def ListarEmpleado():
    cont = 0

    listemp = empleados.keys()
    print(listemp)

    for i in listemp:
        cont += 1
        print("\n")
        print(f'Nombre del empleado es: {empleados[i]["nombre"]}')
        print(f'Horas trabajadas del empleado son : {empleados[i]["horaempleado"]}')
        print(f'El valor de la hora del empleado son : {empleados[i]["valorhora"]:,.0f}')
        print("\n")

        if(cont==5):
            op = input("\nDesea continuar? si: 0 no: s ")
            
            if(op.lower()=="s"):
                return
            else:
                cont = 0
    return  


def agregarnominaempleado(ID):
    
    Sneto = 0
    Sbruto = 0
    Auxilio = 0
    Valorhora =  empleados[ID]["valorhora"]
    hora = empleados[ID]["horaempleado"]
    Sbruto = Valorhora * hora

    empleados[ID]["SalarioBruto"] = Sbruto
    
    if(Sbruto < 1160000 ):
        Auxilio = 140606
    Sneto = Sbruto +  Auxilio  - (Sbruto* eps) - (Sbruto*pension)

    empleados[ID]["Auxilio"] = Auxilio
    empleados[ID]["SalarioNeto"] = Sneto
    empleados[ID]["Pension"] = Sbruto*pension
    empleados[ID]["Eps"] = Sbruto* eps
    return


def listarnominaempleado(ID):
    print("*"*30)    
    print(f"****Nomina*** Empleado: {ID}")
    print(f'El salario bruto es: {empleados[ID]["SalarioBruto"]:,.0f}')
    print(f'El descuento por pension es : {empleados[ID]["Pension"]:,.0f} equivalente al {pension*100}%')
    print(f'El descuento por EPS es : {empleados[ID]["Eps"]:,.0f} equivalente al {eps*100}%')
    print(f'El auxilio de transporte es: {empleados[ID]["Auxilio"]:,.0f}')
    print(f'El Salario Neto es : { empleados[ID]["SalarioNeto"] :,.0f}')
    print("*"*30)
    return
 



def Listarnominatodosemp():

    for i in empleados.keys():
        print(i)
        listarnominaempleado(i)
          
    return


   
def main():

    while True:
        opcion = menu()

        if(opcion == 1):
            AgregarEmpleado()
        elif(opcion == 2):
            idex = leerid("\nDigite el id del empleado a eliminar: ")
            idel = BuscarEmpleado(idex)
            print(idel)
            if(idel!=-1):
                ModificarEmpleado(idel)
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

    empleados