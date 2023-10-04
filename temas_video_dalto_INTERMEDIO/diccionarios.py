# creando diccionarios con dict()
diccionario = dict(nombre="lucaas",apellido="dato")
print(diccionario)

# las listas no pueden ser claves y usamos frozenzet para meter conjuntos
diccionario = {("nombre","apellido"):"jajaaj"} # las tuplas si 
print(diccionario)

# creando diccionarios con fromkeys valor por defecto None
diccionario = dict.fromkeys(["nombre","apellido"])


#diccionario = dict.fromkeys("abcde") # sin corchete el primer dato se vuelve un iterable y el segundo se vuelve valor

# creando diccionarios con fromkeys valor por defecto (no se )
diccionario = dict.fromkeys(["nombre","apellido"],"no se")
print(diccionario)