# Programa para saber la comisión de cada vendedor y el 
# total de comisiones de los vendedores ingresados.


# ESTABLECIENDO LAS VARIABLES PRINCIPALES
valorTotalComisiones = 0
isVerdadero = True


# COMPROBANDO LOS DATOS INGRESADOS POR EL USUARIO
while isVerdadero:

    # COMPROBACIÓN NÚMERO CÉDULA DE CIUDADANÍA
    while True:
        try:
            cedula = input("\nIntroduzca la cédula de ciudadanía: ").strip()
            print(cedula)

            if cedula == "-1":
                print("Saliendo...")
                isVerdadero = False
                break
            else:
                if len(cedula) < 4 or len(cedula) > 12 or cedula.isalpha() or int(cedula) < 0:
                    print("Error: Introduce un número de cédula válido. Debe contener 8 o 10 dígitos.")
                    continue
                break

        except ValueError:
            print("Ha ocurrido un problema al ingresar su cédula de ciudadanía. Inténtelo de nuevo.")
        
        except TypeError:
            print("Ha ocurrido un error en el tipo de dato ingresado. Inténtelo de nuevo.")

    
    # COMPROBACIÓN DEL NOMBRE
    while isVerdadero:
        try:
            nombre = input("Ingrese el nombre: ").strip()
            print(nombre)

            nombreArray = nombre.split(" ")
            print(nombreArray, len(nombreArray))

            if len(nombreArray) < 2 or len(nombre) == 0 or nombre.isalnum():
                print("Error: Asegurate de ingresar al menos un nombre y un apellido y que este no contenga números.")
                continue
            break
        
        except Exception as e:
            print(f"Ha ocurrido un problema. Error: {e}")
    

    # COMPROBACIÓN TIPO DE VENDEDOR
    while isVerdadero:
        try:
            tipoVendedor = int(input("Ingrese el tipo de vendedor: 1 Puerta a Puerta, 2 Telemercadeo 3 Ejecutivo de ventas: "))

            if tipoVendedor < 0 or tipoVendedor > 3:
                print("Error: Escribe un tipo de vendedor válido.")
                continue
            break

        except ValueError:
            print("Error: Has ingresado un número inválido.")

    
    # COMPROBACIÓN VENTAS REALIZADAS
    while isVerdadero:
        try:
            ventasMes = float(input("Valor de ventas realizadas: "))

            if ventasMes < 0:
                print("Has ingresado un número negativo. Ingresa solo números positivos.")
                continue
            isVerdadero = False
            break

        except ValueError:
            print("Error: Has ingresado un valor erróneo. Intentalo de nuevo.")


    # TERMINAR LA PARTE LÓGICA DEL PROGRAMA. MANEJO DE ERRORES FINALIZADA.