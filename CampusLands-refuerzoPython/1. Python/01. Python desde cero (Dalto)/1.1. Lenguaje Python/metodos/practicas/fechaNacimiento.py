# Programa para practicar el tema de cadenas de texto.

fecha = input("Ingrese la fecha de nacimiento en el siguiente formato: dd/mm/aaaa: ")
fechaArray = fecha.split("/")

print("Día", fechaArray[0])
print("Mes", fechaArray[1])
print("Año", fechaArray[2])