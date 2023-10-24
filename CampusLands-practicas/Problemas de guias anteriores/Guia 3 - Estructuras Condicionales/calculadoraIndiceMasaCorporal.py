# Este programa calculará el índice de masa corporal
# mostrándola en pantalla junto a la interpretación 
# de la misma.


# DEFINIENDO LAS VARIABLES PRINCIPALES
pesoLibras = float(input("\nIngrese su peso en libras: "))
alturaPulgadas = float(input("Ingrese su altura en pulgadas: "))

# CONVIRTIENDO LOS VALORES DE LIBRAS Y PULGADAS A KG Y MTS
pesoKilogramos = pesoLibras * 0.45359237
alturaMetros = alturaPulgadas * 0.0254

# CALCULANDO EL BMI
valorBMI = pesoKilogramos / (alturaMetros) ** 2

print("\n", "=" * 35)
if valorBMI < 18.5:
    print(f"Tu índice de masa corporal es muy bajo. Valor: {valorBMI:.1f} BMI")
elif valorBMI > 18.5 and valorBMI < 24.9:
    print(f"Tu índice de masa corporal es normal. Valor: {valorBMI:.1f} BMI")
elif valorBMI > 25.0 and valorBMI < 29.9:
    print(f"Tú índice de masa corporal indica sobrepeso. Valor: {valorBMI:.1f} BMI")
elif valorBMI > 30.0:
    print(f"Tu índice de masa corporal indica obesidad. Valor: {valorBMI:.1f} BMI")
else:
    input("Por favor introduzca un valor válido.")