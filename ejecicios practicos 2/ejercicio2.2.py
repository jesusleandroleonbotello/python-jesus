# creando una funcion que nos devuelva numeros primos 
#entre 0 y el numero que pasamos como limite

# crear una funcion que verifique si un numero es primo 
def es_primo(numero):
    for i in range(2,numero-1): # aqui especificamos que 2 para que no se divida por dos y le colocamos -1 para que el mismo numero no se de 
        if numero % i == 0: return False # si es divicible por alguno tornamos False y cerramos bucle
    return True# si termina el bucle significa que no era divisible y es primo

# creando una funcion que retorne una lista con todos los primos
def primos_hasta(num):
    # creamos una lista
    primos = []
    for i in range(3,num+1): 
        resultado = es_primo(i) # verificamos si es primo
        if resultado == True : primos.append(i) # si lo es lo agregamos a la lista
        # devolvemos la lista
    return primos 
# ejecutando la funcion
resultado = primos_hasta(100)
print(resultado)
