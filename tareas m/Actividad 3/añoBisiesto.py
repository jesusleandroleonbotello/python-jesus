# Programa para que mediante la entrada de un año por parte del usuario, permita 
# conocer si es o no un año bisiesto.


# INICIALIZANDO LAS VARIABLES PRINCIPALES.
yearInput = int(input("Ingrese un año a continuación: "))


# EVALUANDO SI UN AÑO ES BISIESTO O NO.
if (yearInput % 4 == 0) or (yearInput % 100 == 0 and yearInput % 400 == 0):
    print("\nEl año", yearInput, "es un año bisiesto.")
else:
    print("\nEl año", yearInput, "NO es un año bisiesto.")