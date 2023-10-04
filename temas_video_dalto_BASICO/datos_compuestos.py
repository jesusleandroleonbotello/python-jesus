# tenemos una lista que es un conjunto de datos
lista = ["a", "b", "c", "d",1 ,2]
print(lista)
print(lista[1]) # esto es para pedir undato de la lista
print(lista[-1]) # esto es para pedir el ultimo dato de la lista
print(lista[0:3]) # esto es para pedir los primeros 3 datos de la lista
print(lista[1:4]) # esto es para pedir los 2 primeros datos de la lista
print(lista[1:]) # esto es para pedir los datos de la lista hasta el final
print(lista[:3]) # esto es para pedir los datos de la lista desde el inicio hasta el 3
print(lista[2:]) # esto es para pedir los datos de la lista desde el 3 hasta el final
print(lista[:]) # esto es para pedir los datos de la lista desde el inicio hasta el final

# en los elemntos de la lista se cuenta desde 0 en adelante

# siguiente dato es la tupla entender que la tupla no se puede modificar
tupla = ("a", "b", "c", "d",1,2)
print(tupla)
print(tupla[1]) # esto es para pedir undato de la tupla
print(tupla[-1]) # esto es para pedir el ultimo dato de la tupla
print(tupla[0:3]) # esto es para pedir los primeros 3 datos de la tupla
print(tupla[1:4]) # esto es para pedir los 2 primeros datos de la tupla
print(tupla[1:]) # esto es para pedir los datos de la tupla hasta el final
print(tupla[:3]) # esto es para pedir los datos de la tupla desde el inicio hasta el 3
print(tupla[2:]) # esto es para pedir los datos de la tupla desde el 3 hasta el final
print(tupla[:]) # esto es para pedir los datos de la tupla desde el inicio hasta el final

# en los elemntos de la tupla se cuenta desde 0 en adelante

# creandro un conjunto (set) en los conjuntos no hay orden fijo osea pueden cambiar
# en los conjuntos no se puede acceder por un indice print(conjunto[2])
# no muestra valores o datos que se repiten
set = {1,2,3,4,5,6,7,8,9,10}
print(set)
print(set[1]) # esto es para pedir undato del conjunto
print(set[-1]) # esto es para pedir el ultimo dato del conjunto
print(set[0:3]) # esto es para pedir los primeros 3 datos del conjunto
print(set[1:4]) # esto es para pedir los 2 primeros datos del conjunto
print(set[1:]) # esto es para pedir los datos del conjunto hasta el final
print(set[:3]) # esto es para pedir los datos del conjunto desde el inicio hasta el 3
print(set[2:]) # esto es para pedir los datos del conjunto desde el 3 hasta el final

# crear un diccionario es otro dato compuesto
# en los diccionarios se llama es por clave y se separa por comas 
diccionario = {
    "nombre": "juan",  # la clave es nombre y el valor es juan
    "apellido": "perez"
    }
print(diccionario)
print(diccionario["nombre"])
print(diccionario["apellido"])
print(diccionario["nombre"] + " " + diccionario["apellido"])
