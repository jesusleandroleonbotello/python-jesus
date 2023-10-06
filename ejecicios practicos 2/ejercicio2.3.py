# creando una funcion que nos muestre la serie fibonacci entre el 0 y el numero dado

def fibonacci(numero):
    # creamos una lista
    lista = [0,1]
    for i in range(2,numero+1): 
        resultado = lista[-1] + lista[-2] # sumamos los ultimos datos de la lista
        lista.append(resultado) # agregamos el resultado a la lista
    return lista

# ejecutando la funcion
resultado = fibonacci(10)
print(resultado)
