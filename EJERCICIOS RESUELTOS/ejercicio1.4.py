#Ejercicio 4. Diseñar un algoritmo que calcule la longitud de la circunferencia y el área del círculo de radio dado.
import math
def ejercicio4(radio):
    longitud = math.pi*(2*radio)
    area = math.pi*(radio*radio)
    return longitud,area

if __name__ == '__main__':
    ejercicio4()
#En este ejercicio calculamos el número pi a través del uso de variables y multiplicaciones del parámetro dado como radio