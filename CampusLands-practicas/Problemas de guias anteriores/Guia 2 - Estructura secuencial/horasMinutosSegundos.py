# Programa que, en base a una entrada en segundos, devolverá un valor en
# horas, minutos y segundos.


# DEFINIENDO LAS VARIABLES PRINCIPALES
segundosEntrada = int(input("\nIngrese la cantidad en segundos: "))


# CALCULANDO HORAS, MINUTOS Y SEGUNDOS
horas = segundosEntrada // (60 * 60)
minutos = (segundosEntrada // 60) % 60
segundos = segundosEntrada % 60

print("\n", "=" * 35)
print(f"Horas: {horas}")
print(f"Minutos: {minutos}")
print(f"Segundos: {segundos}")