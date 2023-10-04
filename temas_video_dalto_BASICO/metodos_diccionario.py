diccionario = {
    "nombre": "leandro",
    "edad": 25,
    "pais": "Colombia",
    "ciudad": "Bogotá"
}

claves = diccionario.keys() # devuelven las claves y sirve para iterar
print(claves)

valor_de_elemento = diccionario.get("nombre") # nos sirve para buscar en el diccionarion
# si no esta no nos bota error si no None y el programa continua
print(valor_de_elemento)

# eliminando todo del diccionario
# diccionario.clear()
# print(diccionario)

# eliminando un elemento del diccionario
diccionario.pop("nombre") # para sacar mas elemntos poner , "edad" que es otra clave
print(diccionario)

# obteniendo un elmento dict_items iterable
diccionario_iterable = diccionario.items()
for elemento in diccionario.items(): # podemos recorrer los elementos
    print(elemento)
print(diccionario_iterable) # aca igual pero en linea recta
