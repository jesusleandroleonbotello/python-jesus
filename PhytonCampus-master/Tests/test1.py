def Menu():
    
    print("\n"+"="*30)
    print("","*"*4+ "PRODUCTOS ACME" + "*"*4)
    print("="*30)
    print("1. Agregar producto")
    print("2. Modificar producto")
    print("3. Eliminar producto ")
    print("4. Listar varios productos")
    print("5. Estrategia de mercadeo")
    print("-"*30)
    print("6.salir")
    print("="*30,"\n")
    while True:
        try:
            
            Opcion = int(input("\nDigite opcion: "))
            if(Opcion<1 or Opcion>6):
                print("\nopcion no valida, digite nuevamente: ")
                continue
            break
        except ValueError as e:
            print("\nNo valido\n",e)
    return Opcion


def LeerIdProducto(msg):
    while True:
        try:
            print("\n")
            Id = int(input(msg))
            if(Id < 0):
                print("\nValor invalido, debe ser mayor a cero o menor a 12\n")
                continue
            return Id
        except Exception as e:
            print("\nError\n",e)

def LeerNombreProducto(msg):
    while True:
        try:
            Nombre = input(msg)
            Nombre.strip()
            if(Nombre == 0 or not Nombre.isalnum()):
                print("\nNombre no valido\n")
                continue
            return Nombre
        except Exception as e:
            print("\nError al ingresar el nombre\n", e)

def LeerPrecioProducto(msg):
    while True:
        try:
            Precio = float(input(msg))
            if(Precio < 0):
                print("\nValor invalido, debe ser mayor a cero o menor a 12\n")
                continue
            return Precio
        except Exception as e:
            print("\nError\n",e)


def LeerCantidadProducto(msg):
    while True:
        try:
            Cantidad = int(input(msg))
            if(Cantidad < 0):
                print("\nValor invalido, debe ser mayor a cero o menor a 12\n")
                continue
            return Cantidad
        except Exception as e:
            print("\nError\n",e)



def AgregarProducto(DictProducto):
    datEmpleado = {}
    print("="*30)
    Id = LeerIdProducto("Digite el id del producto: ")
    print("="*30)
    Referencia = BuscarProducto(DictProducto,Id)

    if(Referencia==-1):
        print("="*30)
        datEmpleado["Nombre"]  = LeerNombreProducto("Digite el nombre  del producto: ")
        datEmpleado["Precio"]= LeerPrecioProducto("Digite el precio del producto: ")
        datEmpleado["Cantidad"] = LeerCantidadProducto("Digite Cantidad del Producto: ")
        DictProducto[Id] = datEmpleado
        print(DictProducto)
        print("="*30)
        print("\n")
    else:
        print("Error El producto existe")
    return




def ModificaProducto(DictProducto, Id):
    while True:
        try:
            print("="*20)
            print("\n","OPCIONES A MODIFICAR")
            print("1. Nombre")
            print("2. Precio")
            print("3. Cantidad\n")
            print("="*20)

            Seleccion = int(input("\nDigite el numero del Producto que quiere modificar: "))
            
            if( Seleccion < 1 or Seleccion > 3):
                print("Error numero fuera de rango")
                continue
            break

        except ValueError as e:
            print("Error", e)

    if(Seleccion == 1):
        DictProducto[Id]["Nombre"] = LeerNombreProducto("\nDigite nuevo nombre de producto: ")
    elif(Seleccion ==2):
        DictProducto[Id]["Precio"] = LeerPrecioProducto("\nDigite nuevo Precio de producto: ")
    elif(Seleccion == 3):
        DictProducto[Id]["Cantidad"] = LeerCantidadProducto("\nDigite el nueva cantidad de producto: ")
    
    print(DictProducto[Id])       
    print("Producto Modificado")

    return



def BuscarProducto(DictProducto, Id):
    Indice = DictProducto.get(Id,-1)
    
    if(Indice == -1):
        print("Producto no existe")
        return -1
    else:
        print( DictProducto.get(Id,-1))
        return Id
    

def EliminarProducto(DictProducto, Id):
    
    DictProducto.pop(Id)
    print("="*30)
    print("Producto eliminado...")
    return

def ListarProductos(DictProducto):

    for k, v in DictProducto.items():

        print("\n")
        print("="*30)
        print(f'Producto con codigo: {k}')
        print(f'Nombre del Producto es: {v["Nombre"]}')
        print(f'Precio del Producto : {v["Precio"]:,.0f}')
        print(f'Cantidad en Bodega : {v["Cantidad"]}')
        print("="*30)
        print("\n")
 
    return


def EstrategiaMercProducto(DictProducto):

    lst = []
    lstid = {}
    
    dictProducto2 = {}

    for k,v in DictProducto.items():
        lst.append(v["Precio"])
    
    lst.sort()
    for i in lst:
       
        for k,v in DictProducto.items():
            if i == v["Precio"]:
                 NewDictProducto = {}
                 NewDictProducto["Nombre"] = v["Nombre"]
                 NewDictProducto["Precio"] = v["Precio"]
                 NewDictProducto["Cantidad"] = v["Cantidad"]
                 dictProducto2[k] = NewDictProducto 


    ListarProductosPaginacion(dictProducto2)
    
    return dictProducto2


def ListarProductosPaginacion(DictProducto):
    print("*"*30)
    Contador = 0 
    
    for k, v in DictProducto.items():
        Contador+= 1
        NumeroPagina = 1
        print("\n")
        print("="*30)
        print(f'Producto con codigo: {k}')
        print(f'Nombre del Producto es: {v["Nombre"]}')
        print(f'Precio del Producto : {v["Precio"]:,.0f}')
        print(f'Cantidad en Bodega : {v["Cantidad"]}')
        print("="*30)
        print("\n")

        if(Contador==5):
            print("="*30)
            Opcion = input("\nDesea continuar? si: s no: n ")
            
            if(Opcion.lower()=="n"):
                return
            else:
                cont = 0
                print(f"Pagina numero: {NumeroPagina}")
                NumeroPagina+=1
                print("*"*30)
    return


   
def main():
    DictProducto = {}
    while True:
        Opcion = Menu()
        if(Opcion == 1):
            AgregarProducto(DictProducto)
        elif(Opcion == 2):
            print("="*30)
            Id = LeerIdProducto("\nDigite el id del Producto a modificar: ")
            Indice = BuscarProducto(DictProducto,Id)
            print(Indice)
            if(Indice != -1):
                ModificaProducto(DictProducto,Indice) 
        elif(Opcion==3):
            print("="*30)
            Id = LeerIdProducto("\nDigite el id del Producto a eliminar: ")
            Indice = BuscarProducto(DictProducto,Id)
            if(Indice!=-1):
                EliminarProducto(DictProducto, Indice)
        elif(Opcion==4):
                ListarProductos(DictProducto)
        elif(Opcion==5):
            EstrategiaMercProducto(DictProducto)
        elif(Opcion==6):
            print("="*30)
            salida = input("\nDesea Salir de la aplicacion? si: s / No: n   :")
            if(salida.lower() != "s"):
                print("="*30)
                print("\nContinuemos......\n")
            else:
                return 0

r = main()
if(r == 0):
    print("="*30)
    print("\nGracias por usar nuestro software: Made With Love By ACME <3")
    print("="*30)



    

