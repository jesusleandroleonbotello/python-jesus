# Programa que calcula la cantidad de años hasta que se llegue a duplicar 
# el valor de la matrícula.


# DEFINIENDO LAS VARIABLES PRINCIPALES
valorMatricula = 10000
incremento = 7
nuevoValorMatricula = valorMatricula
count = 0


for i in range(1, 100):
    if nuevoValorMatricula <= valorMatricula * 2:
        nuevoValorMatricula += (nuevoValorMatricula * incremento) / 100
        count += 1
    else:
        break


print(f"Han tenido que pasar {count} años para que el valor de la matrícula se duplicara.")