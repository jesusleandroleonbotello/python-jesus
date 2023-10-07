# nos basaremos en estruccturas anteriores modificadas para el funcionamiento de la pagina

def leer_id_producto():
    while True:
        try:
            n = int(input("Ingrese el ID del producto: "))
            if n < 1:
                print("ID inválido. Debe ser mayor a cero")
                continue
            return n
        except ValueError:
            print("Error al ingresar el ID.")

def leer_nombre_producto():
    while True:
        try:
            nom = input("Ingrese el nombre del producto: ")
            nom = nom.strip()
            if len(nom) == 0 or not nom.isalnum():
                print("Nombre inválido")
            elif nom.isdigit(): # esto es para que el nombre no sean solo numeros 
                print("Nombre inválido")
                continue
            return nom
        except Exception as e:
            print("Error al ingresar el nombre del producto.", e)

def leer_valor_producto():
    while True:
        try:
            n = int(input("Ingrese el valor del producto: $"))
            if n < 50 or n > 100000000000000000000:
                print("El valor del producto debe ser superior a $50 pesos COP:")
                continue
            return n
        except ValueError:
            print("Ingrese el valor de $50 pesos en adelante.")

def leer_cant_producto():
    while True:
        try:
            n = int(input("Ingrese la cantidad de unidades por vender: "))
            if n < 0:
                print("Error. La cantidad de unidades debe ser entero superior a 0 ")
                continue
            return n
        except ValueError:
            print("Error al ingresar la cantidad.")

def modificar_producto(productos_clash):
    print("\n\nΔΔΔ 2. Modificar producto ΔΔΔ\n")
    
    id_producto = leer_id_producto()
    pos_producto = buscar_produc(productos_clash, id_producto)
    if pos_producto == -1:
        print("El código del producto no existe.")
        input(" ENTER ")
        return
    
    print("\n")
    while True:
        op = int(input(f"\n1. Nombre del producto?,\n2. Cantidad del producto?,\n3. Valor del producto?\n Que opcion? "))
        if op < 1 or op > 3:
            print("Opción inválida")
            input(" ENTER para continuar")
            continue
        break
    
    if op == 1:
        nombre_producto = leer_nombre_producto()
        productos_clash[pos_producto]["NOMBRE DEL PRODUCTO"] = nombre_producto
    elif op == 2:
        cantidad = leer_cant_producto()
        productos_clash[pos_producto]["CANTIDAD PRODUCTO"] = cantidad
    elif op == 3:
        valHora = leer_valor_producto()
        productos_clash[pos_producto]["VALOR PRODUCTO"] = valHora

def buscar_producto(productos_clash):
    print("\n\n©©© 3. Buscar producto ©©©\n")
    
    id_producto = leer_id_producto()
    exis_producto = buscar_producto(productos_clash, id_producto)
    if exis_producto == False:
        print("El producto con ese código no ha sido ingresado.")
        input("CONTINUAR? ""ENTER"" ")
        return
    
    print("\n", "=" * 30)
    print("Nombre:", productos_clash[id_producto]["NOMBRE PRODUCTO"])
    print("Cantidad de productos:", productos_clash[id_producto]["CANTIDAD PRODUCTO"])
    print("Valor del producto: $", productos_clash[id_producto]["VALOR PRODUCTO"])
    
    input("\n Presione cualquier tecla para volver al menu...")

def buscar_produc(productos_clash, id_producto):
    productos_clash.get(id_producto) != None
    return id_producto in productos_clash

def agregar_productos(productos_clash):
    print("\n\n®®®  1. Agregar producto  ®®®\n")
    producto_unidad = {}
    id_producto = leer_id_producto()
    if buscar_produc(productos_clash, id_producto) == True:
        print("El id ya existe en la lista")
        input()
        return 
    
    producto_unidad["NOMBRE DEL PRODUCTO"] = leer_nombre_producto()
    producto_unidad["CANTIDAD PRODUCTO"] = leer_cant_producto()
    producto_unidad["VALOR PRODUCTO"] = leer_valor_producto()
    
    productos_clash[id_producto] = producto_unidad
    print("Empleado agregado")
    return 

def eliminar_producto(productos_clash):
    print("\n\n*** 2. Eliminar producto\n")
    id_producto = leer_id_producto()
    pos_producto = buscar_produc(productos_clash, id_producto)
    if pos_producto == -1:
        print("El código del producto no existe.")
        input(" ENTER ")
        return
    
    print("\n")
    n =input("¿Está seguro que desea eliminar el producto S/N ?")
    if n is ("N"):
        return menu
    else:
        print(" OK ")
    productos_clash.pop(pos_producto)
    return productos_clash

def mostrar_productos(productos_clash):
    for i in range(0, len(productos_clash), 5):
        print(productos_clash[i:i+5])
        input("Presione cualquier tecla para continuar viendo...")
        print("\n")
    return productos_clash

def menu():
    while True:
        try:
            print("♣" *28)
            print("")
            print("♣♣♣♣♣  PRODUCTOS ACME  ♣♣♣♣♣".center(10))
            print("")
            print("♣" *28)
            print("")
            print("1. Agregar producto")
            print("2. Modificar producto")
            print("3. Eliminar producto")
            print("4. Listar varios productos")
            print("5. Estrategia de mercado")
            print("6. Salir")
            print("")
            op = int(input(">>> Opción (1-6)? "))
            if op < 1 or op > 6:
                print("Opción no válida. Escoja de 1 a 6.")
                input("Presione cualquier tecla para continuar...")
                continue
            return op
        except ValueError:
            print("Opción no válida. Escoja de 1 a 6.")
            input("Presione cualquier tecla para continuar...")


## TERMINAL PRPGRAMA
productos_clash = {} #donde se guardan todos los productos
while True:
    op = menu()
    if op == 1:
        agregar_productos(productos_clash)
        print(productos_clash)
        input(" ENTER ")
    elif op == 2:
        modificar_producto(productos_clash)
        print(productos_clash)
        input(" ENTER ")
    elif op == 3:
        eliminar_producto(productos_clash)
        print("Empleado eliminado")
        input("Presione cualquier tecla para continuar...")
    elif op == 4:
        print(mostrar_productos(productos_clash))
    elif op == 5:
        merca =mostrar_productos(productos_clash)
        print(merca.sort(key=lambda x:x[2]))
    elif op == 6:
        print("\n\nGracias por usar el software. Adios")
        break
