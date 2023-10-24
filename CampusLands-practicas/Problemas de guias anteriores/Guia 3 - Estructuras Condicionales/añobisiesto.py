# Programa para determinar si un año es bisiesto o no.


# DEFINIENDO LAS VARIABLES PRINCIPALES
year = int(input("\nIngrese un año: "))


# DETERMINAR SI ES BISIESTO O NO
if (year % 4 == 0) or (year % 100 == 0 and year % 400 == 0):
    print("\n", "=" * 35)
    print(f"El año {year} SI es bisiesto.")
else:
    print("\n", "=" * 35)
    print(f"El año {year} NO es bisiesto.")