# las funciones lambda sirven para crear funciones rapidas pero anonimas usar solo para cosas simpes 
# no recomendado para que cumpla mas de una funcion

# creando una funcion lambda para multiplicar por dos 
multiplicar_dos = lambda x: x * 2

# ejecutando la funcion
resultado_multiplicar_dos = multiplicar_dos(5)
#print(resultado_multiplicar_dos)

numeros = [1,2,3,4,5,6,7,8,9,10,12,13,18,32,31]

# creando una funcion para buscar los pares o inmpares
#def es_par(num):
    #if num % 2 == 0: # si queremos numeros impares solo se cambiaria el 0 por 1 y ya 
        #return True
    
# buscando filter con una funcion comun
#pares = filter(es_par, numeros)
#print(list(pares)) # con list nos dara una lista de los numeros pares o inmpares

# creando lo mismo de antes pero con lambda
pares = list(filter(lambda x: x % 2 == 0, numeros)) # la funcion filter nos va a ejecutar cada uno de los iterables  de la lista en la funcion
print(pares) # para dar impares lo mismo solo se cambia el 0 por 1 y ya esta


# creando una funcion para calcular el promedio de una lista

def promedio(lista):
    suma = 0
    for num in lista:
        suma += num
    promedio = suma / len(lista)
    return promedio

# ejecutando la funcion
resultado_promedio = promedio([1,2,3,4,5,6,7,8,9,10])
#print(resultado_promedio)




