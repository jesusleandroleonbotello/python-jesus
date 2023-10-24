# Programa para calcular la cantidad de dígitos numéricos de
# una entrada de usuario.


# DEFINIENDO LAS VARIABLES PERTINENTES
numero = int(input("\nIngrese los números enteros que desee: "))


# CALCULANDO LA CANTIDAD DE NÚMEROS ENTEROS
if numero >= 0 and numero <= 9:
    longitudNumero = 1
elif numero >= 10 and numero <= 99:
    longitudNumero = 2
elif numero >= 100 and numero <= 999:
    longitudNumero = 3
elif numero >= 1000 and numero <= 9999:
    longitudNumero = 4
elif numero >= 10000 and numero <= 99999:
    longitudNumero = 5
elif numero >= 100000 and numero <= 999999:
    longitudNumero = 6
elif numero >= 1000000 and numero <= 9999999:
    longitudNumero = 7
elif numero >= 10000000 and numero <= 99999999:
    longitudNumero = 8
elif numero >= 100000000 and numero <= 999999999:
    longitudNumero = 9
elif numero >= 1000000000 and numero <= 9999999999:
    longitudNumero = 10
    

print("\n", "=" * 35)
print(f"El número {numero} contiene {longitudNumero} dígitos")