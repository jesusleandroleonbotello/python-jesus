# crear una lista 
lista = [1,2,3,4,5,6,7,8,9,10] # o con list
# nombre = list([1,2,3,"hola","soy","el"])

resultado = len(lista) # nos da la cantidad de elementos de la lista
print(resultado)

# agregando un elemto ala lista
lista.append("ajajaj")
print(lista)

# agregando un elemto ala lista en un indice especifico
lista.insert(2,"soy")
print(lista)

# agregando varios elemntos a la lista
lista.extend([1,2,3,4,5,6,4])
print(lista)

# borrando un elemto de la lista por su indice
print(len(lista)) # deben salir 19 elementos 
lista.pop(4)
print(len(lista)) # deben salir 18 elementos porque se elimino uno
# recordar que para eiminar el ultimo elemento de la lista se puede usar -1
# asi con el penultimo -2 etc...

# removiendo un elemnto de la lista por su valor 
lista.remove("soy") # si lo encuentra lo elimina si no da un error excepsion
print(lista)

# eliminando todos los elementos de la lista
# lista.clear()
# print(lista)

# ordenando la lista de menor a mayor pero no entran los str texto
#lista.sort()
#print(lista)

# ordenando la lista pero en reverse con el parametro reverse=True
# los ordena primero y los invierte de mayor a menor 
#lista.sort(reverse=True)
#print(lista)

# invirtiendo los elementos de una lista no los ordena solo los invierte asi
#lista.reverse()