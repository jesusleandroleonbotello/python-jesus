def calcular_serie_alterna(n):
    suma = 0
    signo = 1  # Para alternar entre sumar y restar
    
    for i in range(1, n + 1):
        termino = signo * (1 / i)
        suma += termino
        signo *= -1  # Cambia el signo para el siguiente término
    
    return suma

n = int(input("Ingrese el valor de 'n': "))
resultado = calcular_serie_alterna(n)
print(f"La suma de la serie hasta 1/{n} es: {resultado}")
