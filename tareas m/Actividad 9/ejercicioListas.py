# Ta difícil jefe :(


# Este programa tiene como objetivo la gestión de la nómina de empleados para la empresa
# ACME mediante una serie de requerimientos que la misma empresa proporcionó.



# DEFINIENDO LAS VARIABLES PRINCIPALES
isVerdadero = True
listaNombreFiltrado = []  #Esta variable pertenece a la función "validarNombre".
listaEmpleados = []  #Esta es la lista principal donde se almacena la info de los empleados.


# DEFINIENDO LAS FUNCIONES DE VALIDACIÓN DE DATOS
def validarID(msj):
    while True:
        try:
            id = int(input(msj))
            
            if id < 0:
                print("Error: El valor del ID no puede ser un número negativo.")
                continue
            return id
        
        except ValueError:
            print("Ha ocurrido un error al ingresar el ID del empleado. Inténtelo de nuevo.")
        except:
            print("Ha ocurrido un error inesperado. Inténtelo de nuevo o comuníquese con un administrador.")


def validarNombre(msj):
    while True:
        try:
            nombre = input(msj).strip()
            nombreArray = nombre.split(" ")
            
            # Algoritmo para filtrar el nombre y validarlo
            for i in range(len(nombreArray)):
                if nombreArray[i] != "":
                    listaNombreFiltrado.append(nombreArray[i])
            
            nombreFiltrado = "".join(listaNombreFiltrado).lower()
            nombreFinal = " ".join(listaNombreFiltrado).title()
            
            # Validación
            if len(listaNombreFiltrado) < 2 or not nombreFiltrado.isalnum() or len(nombreFiltrado) == 0:
                print("Error: Debes introducir un nombre válido con al menos un nombre y un apellido.")
                continue
            return nombreFinal
        
        except Exception as e:
            print(f"Ha ocurrido un problema al ingresar el nombre. Error: {e}")
        except:
            print("Ha ocurrido un error inesperado. Inténtelo de nuevo o comuníquese con un administrador.")


def validarHorasTrabajadas(msj):
    while True:
        try:
            horasTrabajadas = int(input(msj))
            
            if horasTrabajadas < 1:
                print("Error: Debes ingresar un valor numérico entero igual o superior a 1.")
                continue  
            elif horasTrabajadas > 160:
                print("Error: Debes ingresar un valor numérico entero igual o menor a 160.")
                continue
            return horasTrabajadas
        
        except ValueError:
            print("Ha ocurrido un error al ingresar las horas trabajadas. Inténtelo de nuevo.")
        except:
            print("Ha ocurrido un error inesperado. Inténtelo de nuevo o comuníquese con un administrador.")


def validarValorHora(msj):
    while True:
        try:
            valorHora = int(input(msj))
            
            if valorHora < 8000:
                print("Error: El valor de la hora no puede ser inferior a $8,000 COP.")
                continue
            elif valorHora > 150000:
                print("Error: El valor de la hora no puede ser superior a $150,000 COP.")
                continue
            return valorHora
        
        except ValueError:
            print("Ha ocurrido un error al ingresar el valor de la hora. Inténtelo de nuevo.")
        except:
            print("Ha ocurrido un error inesperado. Inténtelo de nuevo o comuníquese con un administrador.")


# DEFINIENDO LAS FUNCIONES COMPLEMENTARIAS A LAS FUNCIONES DE LOS ENUNCIADOS
def reiniciarListas():
    pass


# DEFINIENDO LAS FUNCIONES DE LOS ENUNCIADOS
def menu():
    print("\n", "*** NOMINA ACME ***".center(20))
    print("MENU".center(28))
    
    print("\n1. Agregar empleado")
    print("2. Modificar empleado")
    print("3. Buscar empleado")
    print("4. Eliminar empleado")
    print("5. Listar empleados")
    print("6. Listar nómina de un empleado")
    print("7. Listar nómina de todos los empleados")
    print("8. Salir")
    
    # Validar la entrada de usuario
    while True:
        try:
            opcionUsuario = int(input("    >> Escoja una opción (1-8): "))
            
            if opcionUsuario < 1:
                print("Error: No puedes ingresar un número menor que 1 ni números negativos, solo entre 1-8")
                continue
            elif opcionUsuario > 8:
                print("Error: No puedes ingresar un número mayor que 8. Ingrese un número entre 1-8")
                continue
            return opcionUsuario
        
        except ValueError:
            print("Ha ocurrido un error al ingresar la opción. Inténtelo de nuevo.")
        except:
            print("Ha ocurrido un error inesperado. Inténtelo de nuevo o comuníquese con un administrador")


def agregarEmpleado(id, nombre, horasTrabajadas, valorHora):
    pass


def modificarEmpleado():
    pass


def buscarEmpleado():
    pass


def eliminarEmpleado():
    pass


def listarEmpleados():
    pass


def listarNominaEmpleado():
    pass


def listarNominaEmpleados():
    pass


def salir():
    pass



# CREANDO LA ESTRUCTURA DEL PROGRAMA
while isVerdadero:
    eleccionUsuario = menu()
    
    if eleccionUsuario == 1:
        print("\n", "=== AGREGAR EMPLEADO ===")
        
        id = validarID("  Ingrese el ID: ")
        nombre = validarNombre("  Ingrese el nombre: ")
        horasTrabajadas = validarHorasTrabajadas("  Ingrese la cantidad de horas trabajadas: ")
        valorHora = validarValorHora("  Ingrese el valor de la hora: ")
        
        agregarEmpleado(id, nombre, horasTrabajadas, valorHora)