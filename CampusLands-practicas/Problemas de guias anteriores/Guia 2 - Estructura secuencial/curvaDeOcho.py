# Programa que calcula la curva de 8 bajo un sistema de 
# calificación numérica de 0.0 a 5.0


# DEFINIENDO LAS VARIABLES PRINCIPALES
nota = float(input("\n¿Cuál es su nota?: "))


# CALCULANDO LA CURVA DE 8
curvaDeOcho = (nota * 0.8) + 1


# IMPRIMIENDO LOS RESULTADOS
print("\n", "=" * 35)
print(f"La curva de 8 para su nota de {nota:.1f}, es de: {curvaDeOcho:.1f}")