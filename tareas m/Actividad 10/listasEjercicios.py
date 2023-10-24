def leerValHoraEmpl():
    while True:
        try:
            n = int(input("Ingrese el valor de la hora trabajada del empleado: "))
            if n < 8000 or n > 150000:
                print("Valor de la Hora inválida. Debe estar en el rango de [8000, 150000]")
                continue
            return n
        except ValueError:
            print("Error al ingresar el valor de la hora trabajada.")

def leerHoraTrabEmpl():
    while True:
        try:
            n = int(input("Ingrese la horas trabajadas del empleado: "))
            if n < 0 or n > 160:
                print("Horas inválidas. Debe estar en el rango de [0, 160]")
                continue
            return n
        except ValueError:
            print("Error al ingresar las horas.")

def leerNombreEmpl():
    while True:
        try:
            nom = input("Ingrese el nombre del empleado: ")
            nom = nom.strip()
            if len(nom) == 0 or not nom.isalnum():
                print("Nombre inválido")
                continue
            return nom
        except Exception as e:
            print("Error al ingresar el nombre.", e)

def leerIDEmpl():
    while True:
        try:
            n = int(input("Ingrese el ID del empleado: "))
            if n < 1:
                print("ID inválido. Debe ser mayor a cero")
                continue
            return n
        except ValueError:
            print("Error al ingresar el ID.")
            

def listarEmpleados(diccionarioEmpleados):
    print("\n\n5. Listar empleados")
    
    valoresClaveDiccionario = diccionarioEmpleados.keys()
    
    for i in valoresClaveDiccionario:
        print("\n", "=" * 35)
        print(f"Nombre: {diccionarioEmpleados[i]['nombre']}")
        print(f"Horas trabajadas: {diccionarioEmpleados[i]['HorasTrabajadas']} horas.")
        print(f"Valor hora: ${diccionarioEmpleados[i]['ValorHora']:,.0f} COP.")
        print(f"Salario: ${diccionarioEmpleados[i]['Salario']:,.0f} COP.")
    input("\nPresione cualquier tecla para regresar al menú...")
        

def eliminarEmpleado(diccionarioEmpleados):
    print("\n\n4. Eliminar empleado\n")
    
    idEmpleado = leerIDEmpl()
    existeEmpleado = buscarEmpleado(dicEmpleados, idEmpleado)
    
    if existeEmpleado == False:
        print("El empleado que deseas eliminar no existe.")
        input()
        return
    
    try:
        del diccionarioEmpleados[idEmpleado]
        print(diccionarioEmpleados)
    
    except Exception as e:
        print(f"Ha ocurrido un problema al eliminar el empleado. Error: {e}")
    except:
        print("Ha ocurrido un error inesperado, inténtelo de nuevo o comuníquese con un administrador.")
    

def buscarEmpleado(dicEmpleados, idEmpl):
    # return dicEmpleados.get(idEmpl) != None
    return idEmpl in dicEmpleados

def mnubuscarEmpleado(dicEmpleados):
    print("\n\n3. Buscar Empleado\n")
    
    idEmpl = leerIDEmpl()
    existEmpl = buscarEmpleado(dicEmpleados, idEmpl)
    if existEmpl == False:
        print("El Empleado con ese código no ha sido ingresado.")
        input()
        return
    
    print("\n", "=" * 30)
    print("Nombre:", dicEmpleados[idEmpl]["nombre"])
    print("Horas trabajadas:", dicEmpleados[idEmpl]["HorasTrabajadas"])
    print("Valor de la hora:", dicEmpleados[idEmpl]["ValorHora"])
    print(f"Salario: ${dicEmpleados[idEmpl]['Salario']:,.2f}")
    input("\n Presione cualquier tecla para volver al menu...")

def modificarEmpleado(dicEmpleados):
    print("\n\n2. Modificar Empleado\n")
    
    idEmpl = leerIDEmpl()
    existEmpl = buscarEmpleado(dicEmpleados, idEmpl)
    if existEmpl == False:
        print("El código del empleado no existe.")
        input()
        return
    
    print("\n")
    while True:
        op = int(input("\n1. Nombre\n2. Cantidad de Horas\n3. Valor de la hora\nOpcion? "))
        if op < 1 or op > 3:
            print("Opción inválida")
            input()
            continue
        break
    
    if op == 1:
        nombre = leerNombreEmpl()
        dicEmpleados[idEmpl]["nombre"] = nombre
    elif op == 2:
        cantHoras = leerHoraTrabEmpl()
        dicEmpleados[idEmpl]["HorasTrabajadas"] = cantHoras
        
    elif op == 3:
        valHora = leerValHoraEmpl()
        dicEmpleados[idEmpl]["ValorHora"] = valHora
        
    dicEmpleados[idEmpl]["Salario"] = dicEmpleados[idEmpl]["ValorHora"] * dicEmpleados[idEmpl]["HorasTrabajadas"]

def agregarEmpleado(dicEmpleados):
    print("\n\n*** 1. Agregar empleado\n")
    dicDatos = {}
    id = leerIDEmpl()
    if buscarEmpleado(dicEmpleados, id) == True:
        print("El id ya existe en la lista")
        input()
        return
    
    dicDatos["nombre"] = leerNombreEmpl()
    dicDatos["HorasTrabajadas"] = leerHoraTrabEmpl()
    dicDatos["ValorHora"] = leerValHoraEmpl()
    dicDatos["Salario"] = dicDatos["ValorHora"] * dicDatos["HorasTrabajadas"]
    
    dicEmpleados[id] = dicDatos

def menu():
    while True:
        try:
            print("*** NOMINA ACME ***".center(40))
            print("MENU".center(40))
            print("1. Agregar empleado")
            print("2. Modificar empleado")
            print("3. Buscar emplado")
            print("4. Eliminar empleado")
            print("5. Listar empleados")
            print("6. Listar nómina de un empleado")
            print("7. Listar nómina de todos los empleados")
            print("8. Salir")
            op = int(input(">>> Opción (1-8)? "))
            if op < 1 or op > 8:
                print("Opción no válida. Escoja de 1 a 8.")
                input("Presione cualquier tecla para continuar...")
                continue
            return op
        except ValueError:
            print("Opción no válida. Escoja de 1 a 8.")
            input("Presione cualquier tecla para continuar...")

## PROGRAMA PRINCIPAL
dicEmpleados= {}
while True:
    op = menu()
    if op == 1:
        agregarEmpleado(dicEmpleados)
        # print(dicEmpleados)
        # input()
        
    elif op == 2:
        modificarEmpleado(dicEmpleados)
        # print(dicEmpleados)
        # input()

    elif op == 3:
        mnubuscarEmpleado(dicEmpleados)

    elif op == 4:
        eliminarEmpleado(dicEmpleados)

    elif op == 5:
        listarEmpleados(dicEmpleados)

    elif op == 6:
        pass

    elif op == 7:
        pass

    elif op == 8:
        print("\n\nGracias por usar el software. Adios")
        break