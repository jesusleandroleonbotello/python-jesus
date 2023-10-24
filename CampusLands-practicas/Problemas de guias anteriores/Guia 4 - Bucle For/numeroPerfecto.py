# Programa para saber si un número ingresado por el usuario 
# es perfecto o no.


# DEFINIENDO LAS VARIABLES PRINCIPALES
numeroUsuario = int(input("Ingrese el número a validar si es o no positivo: "))
sumaDivision = 0


# CALCULAR SI EL NÚMERO ES O NO ES POSITIVO
for i in range(1, numeroUsuario):
    if numeroUsuario % i == 0:
        sumaDivision += i
        
if sumaDivision == numeroUsuario:
    print(f"¡El número {numeroUsuario} SI es perfecto!")
else:
    print(f"El número {numeroUsuario} NO es perfecto.")