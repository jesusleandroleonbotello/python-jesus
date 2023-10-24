# Este programa replica una simulación de un experimento realizado
# en Monte Carlo, donde aplica la probabilidad y generación de números
# aleatorios para resolver problemas.


# IMPORTAR LAS BIBLIOTECLAS NECESARIAS
import math as Math
import random


# DEFINIENDO LAS VARIABLES / CONSTANTES PRINCIPALES
RADIO_CIRCULO = 1
AREA_CIRCULO = Math.pi
AREA_CUADRADO = 4
CANTIDAD_PUNTOS = 1000000

probabilidadPuntoCirculo = (AREA_CIRCULO / AREA_CUADRADO)
numberOfHits = 0


# RESOLVIENDO EL EJERCICIO
for i in range(CANTIDAD_PUNTOS):
    numeroAleatorioCuadrado = random.random()
    
    if numeroAleatorioCuadrado > 0 and numeroAleatorioCuadrado <= probabilidadPuntoCirculo:
        numberOfHits += 1

aproximacionPi = 4 * numberOfHits / CANTIDAD_PUNTOS
cantidadNumberOfHits = CANTIDAD_PUNTOS * (aproximacionPi / 4)


# IMPRIMIENDO LOS RESULTADOS EN PANTALLA
print("\n", "=" * 35)
print(f"La cantidad de puntos que se generaron dentro del circulo fueron de: {cantidadNumberOfHits:,.0f}")
print(f"Por tanto, el aproximado del número PI es de: {aproximacionPi:.5}")