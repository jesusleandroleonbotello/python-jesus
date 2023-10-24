# Programa para determinar la comisión de un vendedor de acuerdo a 
# parámetros establecidos por la compañía misma. Se validarán 
# los datos ingresados por el usuario y personalizará los posibles errores.


# DEFINIENDO LAS VARIABLES PRINCIPALES
isVerdadero = True
valorTotalVentas = 0
ValorTotalComisiones = 0


# DEFINIR LA ESTRUCTURA WHILE DEL PROGRAMA
while isVerdadero:
    #Comprobación cédula de ciudadanía
    while True:
        try:
            cedula = input("\nIngrese la cédula de ciudadanía: ").strip()

            if int(cedula) == -1:
                print("\n¡Gracias por usar nuestro programa!")
                isVerdadero = False
                break
            else:
                if len(cedula) < 4 or len(cedula) > 12 or cedula.isalpha() or int(cedula) < 0:
                    print("Error: Introduce un valor numérico positivo y que contenga entre 4 a 12 números.")
                    continue
                break
        
        except ValueError:
            print("Error: Ingresa un número entero válido.")
        except Exception as e:
            print(f"\nHa ocurrido un problema al digitar su cédula de ciudadanía. \nError: {e}")
        except:
            print("Algo ha ido mal. Asegúrate de ingresar solo valores válidos.")
            #El uso de este "except:" sin nada más, así solo (Y de los demás en el programa), 
            #es que pueda captuar algún error inesperado y así poderlo manejar de manera 
            #más amena al usuario.
    
    
    #Validación del nombre
    while isVerdadero:
        try:
            nombre = input("Ingrese el nombre: ").strip()
            nombreArray = nombre.split(" ")
            nombreFiltradoArray = []    #Creando una lista vacía - Investigado en Google para el algoritmo ;)
            
            #Algoritmo para evitar que "split()" cuente un espacio como parte del Array
            for i in range(len(nombreArray)):
                if nombreArray[i] != "":
                    nombreFiltradoArray.append(nombreArray[i])
                    #El método .append() añade un nuevo elemento al final de una lista
            
            
            #Seteo la variable "nombreFiltradoFinal" en vacío antes de agregarle 
            #información para evitar sobreescrituras no deseadas
            nombreFiltradoFinal = ""
            nombreFiltradoFinal += " ".join(nombreFiltradoArray)
            
            
            #Validación del nombre ingresado
            if len(nombreFiltradoArray) < 2 or nombreFiltradoFinal.isalnum():
                print("Error: Ingresa al menos un nombre y un apellido. Solo letras.\n")
                continue
            break
        
        except Exception as e:
            print("Ha ocurrido un problema al ingresar el nombre, inténtalo de nuevo.\n")
        except:
            print("Algo ha ido mal, inténtalo de nuevo.\n")
    
    
    
    #Verificación del tipo de vendedor
    while isVerdadero:
        try:
            tipoVendedor = int(input("Ingrese el tipo de vendedor: 1 Puerta a puerta, 2 Telemercadeo o 3 Ejecutivo de ventas: "))
            
            if tipoVendedor < 1 or tipoVendedor > 3:
                print("Error: Elije una opción válida (1, 2 o 3).\n")
                continue
            break
        
        except ValueError:
            print("Ha ocurrido un error en la digitación de la opción. Inténtalo de nuevo.\n")
        except:
            print("Ha ocurrido un error inesperado. Inténtelo de nuevo o ponte en contacto con un administrador.\n")
    
    
    
    #Validar el valor de las ventas en el mes
    while isVerdadero:
        try:
            valorVentasMes = int(input("Ingrese el valor de las ventas en el mes (Sin puntos ni comas): "))
            
            if valorVentasMes < 0:
                print("Error: Debes ingresar un valor entero positivo. Ingrese únicamente números, no letras.\n")
                continue
            break
        
        except ValueError:
            print("Ha ocurrido un problema. Asegúrate de digitar correctamente el valor de las ventas.\n")
        except:
            print("Ha ocurrido un problema inesperado. Inténtelo de nuevo o ponte en contacto con un administrador.\n")
    
    
    
    #Definir la estructura lógica del programa (if-else)
    while isVerdadero:
        valorTotalVentas += valorVentasMes
        
        if tipoVendedor == 1:
            porcentajeComision = 20
            nombreTipoVendedor = "Puerta a Puerta"
            
            valorComision = (valorVentasMes * porcentajeComision) / 100
            ValorTotalComisiones += valorComision
            pagoVendedor = valorVentasMes + valorComision
            
        elif tipoVendedor == 2:
            porcentajeComision = 15
            nombreTipoVendedor = "Telemercadeo"
            
            valorComision = (valorVentasMes * porcentajeComision) / 100
            ValorTotalComisiones += valorComision
            pagoVendedor = valorVentasMes + valorComision
            
        elif tipoVendedor == 3:
            porcentajeComision = 25
            nombreTipoVendedor = "Ejecutivo de ventas"
            
            valorComision = (valorVentasMes * porcentajeComision) / 100
            ValorTotalComisiones += valorComision
            pagoVendedor = valorVentasMes + valorComision
        
        
        #Imprimir la información + pago de cada vendedor
        print("\n", "=" * 35)
        print(f"Vendedor: {nombreFiltradoFinal.title()}")
        print(f"C.C: {cedula}")
        print(f"Tipo vendedor: {tipoVendedor} - {nombreTipoVendedor}")
        print(f"Valor ventas realizadas en el mes: ${valorVentasMes:,.0f} COP")
        print(f"Valor a pagar por comisión: ${valorComision:,.0f} COP")
        
        break   #Evita que este bucle sea infinito


#Imprimiendo los valores recolectados durante la ejecución del software
print("\n", "====== RESUMEN ======")
print(f"Valor total de las ventas del mes: ${valorTotalVentas:,.0f} COP")
print(f"Valor total a pagar por comisiones: ${ValorTotalComisiones:,.0f} COP")