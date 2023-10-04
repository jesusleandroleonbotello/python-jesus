animales = {"gato","perro","loro","cebra","pez"}
numeros = {52,16,14,72}

#recorriendo la conjunto de animales
for animal in animales:
    print(f"ahora la variable animal es : {animales}")

#recorriendo la conjunto de numeros y mltiplicando cada valor por 10
for numero in numeros:
    resultado = numero * 10
    print(resultado)

# iterando dos conjunto del mismo tamaño al mismo teiempo
for numero,animal in zip(numeros, animales):
    print(f"recorriendo conjunto 1: {animal}")
    print(f"recorriendo conjunto 2: {numero}")

# forma no correcta de recorrer una conjunto con su indice
#for num in range(len(numeros)): #no funcio en conjuntos
    #print(numeros[num])

#forma correcta de recorrer una conjunto con su indice
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f"el indice es: {indice} y el valor: {valor}")

# usando el for/else
for numero in numeros:
    print(f"ejecutando el ultimo bucle, valor actual: {numero}")
else:
    print("el bucle termino")

# todo lo anterior funciona igual para tuplas y conjuntos 