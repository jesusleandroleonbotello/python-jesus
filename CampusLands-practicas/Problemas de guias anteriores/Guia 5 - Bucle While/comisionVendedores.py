# Programa para determinar el valor de las comisiones que genera cada
# vendedor en una empresa.


# DEFINIENDO LAS VARIABLES PRINCIPALES
isVerdadero = True
valorVentasTotalMes = 0
valorComisionesTotal = 0
vendedoresTipo1 = 0
vendedoresTipo2 = 0
vendedoresTipo3 = 0


# DEFINIENDO EL FUNCIONAMIENTO DEL PROGRAMA
while isVerdadero:
    cedulaCiudadania = int(input("\nIngrese la cédula de ciudadanía: "))
    
    if cedulaCiudadania != -1:
        nombre = input("Ingrese el nombre: ")
        tipoVendedor = int(input("Ingrese 1 puerta a puerta, 2 telemercadeo o 3 ejecutivo de ventas: "))
        valorVentas = int(input("Ingrese el valor de ventas realizadas en el mes: "))
        
        valorVentasTotalMes += valorVentas
        
        if tipoVendedor == 1:
            porcentajeComision = 20
            valorPagarComision = (valorVentas * porcentajeComision) / 100
            valorComisionesTotal += valorPagarComision
            tipoVendedorNombre = "Puerta a Puerta"
            vendedoresTipo1 += 1
        
        elif tipoVendedor == 2:
            porcentajeComision = 15
            valorPagarComision = (valorVentas * porcentajeComision) / 100
            valorComisionesTotal += valorPagarComision
            tipoVendedorNombre = "Telemercadeo"
            vendedoresTipo2 += 1
        
        elif tipoVendedor == 3:
            porcentajeComision = 25
            valorPagarComision = (valorVentas * porcentajeComision) / 100
            valorComisionesTotal += valorPagarComision
            tipoVendedorNombre = "Ejecutivo de ventas"
            vendedoresTipo3 += 1
        
        else:
            input("Ingrese un valor válido en la opción \"Tipo de vendedor\". Saliendo...")
            isVerdadero = False
    
    else:
        print("\n", " " * 5, "*" * 17)
        print("Gracias por usar nuestro Software.")
        print("Saliendo...")
        isVerdadero = False
        break
    
    #Escribir los resultados de las operaciones realizadas
    print("\n", "=" * 35)
    print(f"Vendedor: {nombre}")
    print(f"C.C: {cedulaCiudadania}")
    print(f"Tipo de vendedor: {tipoVendedorNombre}")
    print(f"Valor en ventas: ${valorVentas:,.0f} COP")
    print(f"Valor a pagar por comisión: ${valorPagarComision:,.0f} COP")
    print(f"Sueldo total del vendedor: ${valorVentas + valorPagarComision:,.0f} COP")
    

if valorVentasTotalMes == 0 and valorComisionesTotal == 0:
    pass
elif valorVentasTotalMes > 0 and valorComisionesTotal > 0:
    print("\n", "=" * 35)
    print(f"El valor de las ventas totales son: ${valorVentasTotalMes:,.0f} COP")
    print(f"El valor de las comisiones total a pagar son: ${valorComisionesTotal:,.0f} COP")
    print(f"\nResumen --> Puerta a Puerta: {vendedoresTipo1}  | Telemercadeo: {vendedoresTipo2}  |  Ejecutivo de ventas: {vendedoresTipo3}")
    print(f"Total vendedores: {vendedoresTipo1 + vendedoresTipo2 + vendedoresTipo3} vendedores.")