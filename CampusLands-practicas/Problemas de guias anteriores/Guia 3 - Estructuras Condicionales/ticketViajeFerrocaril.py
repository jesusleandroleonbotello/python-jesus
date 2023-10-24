# Programa para determinar el precio de un billete de ferrocarril
# según los kilómetros recorridos y días de estadía.


# DEFINIENDO LAS VARIABLES PRINCIPALES
distanciaRecorrer = int(input("Distancia a recorrer: "))
diasEstancia = int(input("Días de estancia: "))
descuento = 30
precioKilometros = 0.63


# CALCULAR VALOR BILLETE FERROCARRIL
precioBillete = distanciaRecorrer * precioKilometros

if diasEstancia > 7 and distanciaRecorrer > 800:
    precioFinal = precioBillete - ((precioBillete * descuento) // 100)
else:
    precioFinal = precioBillete


# IMPRIMIENDO LOS DATOS EN PANTALLA
print(f"El precio de su billete de ida y vuelta es de: ${precioFinal:,.2f} USD")