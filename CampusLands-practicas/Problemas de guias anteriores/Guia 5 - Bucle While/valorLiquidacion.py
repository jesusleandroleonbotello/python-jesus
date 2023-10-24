# Este programa permite calcular el valor de liquidación de cada
# conductor según lineamientos de la empresa misma.


# DEFINIENDO LAS VARIABLES PRINCIPALES
isVerdadero = True
valorTotalPagar = 0
conductoresExpertos = 0
conductoresNovatos = 0


# DEFINIENDO LA ESTRUCTURA DEL PROGRAMA
while isVerdadero:
    cedula = int(input("\nIngrese la cédula: "))
    nombre = input("Ingrese el nombre: ")
    claseConductor = int(input("Ingrese la clase del conductor: 1 Experto, 2 Novato: "))
    valorPasajesMes = int(input("Ingrese el valor total de pasajes durante el mes: "))
    valorEncomiendaMes = int(input("Ingrese el valor total de las encomiendas del mes: "))
    
    if claseConductor == 1:
        claseConductorNombre = "Experto"
        porcentajeComisionPasajesMes = 30
        porcentajeComisionEncomiendaMes = 20
        
        valorComisionPasajes = (valorPasajesMes * porcentajeComisionPasajesMes) / 100
        valorComisionEncomienda = (valorEncomiendaMes * porcentajeComisionEncomiendaMes) / 100
        valorPasajesMes += valorComisionPasajes
        valorEncomiendaMes += valorComisionEncomienda
        
        pagoConductor = valorPasajesMes + valorEncomiendaMes
        valorTotalPagar += pagoConductor
        conductoresExpertos += 1
        
    elif claseConductor == 2:
        claseConductorNombre = "Novato"
        porcentajeComisionPasajesMes = 20
        porcentajeComisionEncomiendaMes = 15
        
        valorComisionPasajes = (valorPasajesMes * porcentajeComisionPasajesMes) / 100
        valorComisionEncomienda = (valorEncomiendaMes * porcentajeComisionEncomiendaMes) / 100
        valorPasajesMes += valorComisionPasajes
        valorEncomiendaMes += valorComisionEncomienda
        
        pagoConductor = valorPasajesMes + valorEncomiendaMes
        valorTotalPagar += pagoConductor
        conductoresNovatos += 1
    
    else:
        print("\nHas elegido una clase de conductor inválida. Debe estar dentro del rango (1-2).")
        isVerdadero = False
        break
    
    
    #Imprimir los valores recolectados en pantalla
    print("\n", "=" * 35)
    print(f"Conductor: {nombre}")
    print(f"C.C: {cedula}")
    print(f"Clase conductor: {claseConductorNombre}")
    print(f"Valor de pasajes en el mes: ${valorPasajesMes - valorComisionPasajes:,.0f} COP")
    print(f"Valor de encomiendas en el mes: ${valorEncomiendaMes - valorComisionEncomienda:,.0f} COP")
    
    print(f"\nValor de comisión por el concepto de pasajes: ${valorComisionPasajes:,.0f} COP")
    print(f"Valor de comisión por el concepto de encomiendas: ${valorComisionEncomienda:,.0f} COP")
    print(f"Pago total del conductor: ${pagoConductor:,.0f} COP")
    
    
    #Verificar si el usuario desea continuar
    continuar = input("¿Desea continuar? S/N: ")
    continuar = continuar.upper()
    
    if continuar == "S":
        isVerdadero = True
        
    elif continuar == "N":
        isVerdadero = False
    

#Imprimiendo los valores recolectados durante la ejecución del While (Resumen)
print("\n", "***** RESUMEN *****")
print(f"Conductores expertos: {conductoresExpertos} conductores.")
print(f"Conductores novatos: {conductoresNovatos} conductores.")
print(f"Conductores totales ingresados: {conductoresExpertos + conductoresNovatos} conductores.")

print(f"\nValor a pagar en total: ${valorTotalPagar:,.0f} COP")

print("\n\nGracias por usar nuestro software. Saliendo...")