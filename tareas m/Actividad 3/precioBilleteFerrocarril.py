# Programa para determinar el precio de un billete de ferrocarril, teniendo en cuenta descuentos bajo variables definidas:
# Km > 800 y días > 7 (una semana).


# INICIALIZANDO LAS VARIABLES PRINCIPALES.
distancia = int(input("Ingrese la distancia a recorrer [En Kilómetros y solo números, no letras ni espacios]: "))
diasEstancia = int(input("Ingrese el número de días de estancia [Sólo números, no letras ni espacios] : "))
precioPorKilometros = 0.63
cantKmDescuento = 800
cantDiasDescuento = 7
descuento = 30

# CALCULANDO EL PRECIO DEL BILLETE SIN DESCUENTO
precioBillete = distancia * precioPorKilometros


# CONDICIONAL PARA DESCUENTO AL VALOR TOTAL DEL BILLETE DEL FERROCARRIL.
if distancia > cantKmDescuento and diasEstancia > cantDiasDescuento:
    resultadoDescuento = (precioBillete * descuento) / 100
    
    precioBillete -= resultadoDescuento     # Es igual a decir "precioBillete -= resultadoDescuento"

    #RESULTADO EN CASO DE ENTRAR EN EL IF
    print("\n¡Acabas de obtener un descuento! Su tarifa queda en:", "${:,.2f}".format(precioBillete), end="USD\n")   # Empleando el método .format()
else:
    # RESULTADO A MOSTRAR EN CONSOLA
    print(f"\n¡Esperamos que hayas disfrutado de tu viaje! El precio de tu boleto es de: ${precioBillete:,.2f}USD")  # Empleando f-strings (Python > v3.8)