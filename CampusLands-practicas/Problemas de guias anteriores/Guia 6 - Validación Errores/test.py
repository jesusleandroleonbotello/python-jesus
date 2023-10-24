# textoArray = "Hola  Mundo".split(" ")
# nuevoTextoArray = []
# elementosEliminadosArray = []
# string = ""


# for i in range(len(textoArray)):
#     if textoArray[i] != "":
#         nuevoTextoArray.append(textoArray[i])
#     else:
#         elementosEliminadosArray.append(textoArray[i])
    
# string += " ".join(nuevoTextoArray)
    
    
        
# print(f"Cadena de texto: {string}, {len(string)}")



# test = " 13,445.24 ".strip()
# print(test.isdigit())
# print(test.count(" "))



nuevaVariable = "65"
print(nuevaVariable.isalnum())







# NOTAS IMPORTANTES RESPECTO AL CÓDIGO:

# 1.El uso de las rebanadas en Python pueden generar una lista de listas (Listas anidadas) o
# bien, obtener el valor de un item almacenado en otra lista y copiarla en otra lista pero esta
# vez es plana (es decir, sin llaves ni caracteres raros al inicio XD)

# 2. Para unir los elementos de una lista y de paso convertirlos a un string, se usa el método
# .join() y dentro almacenará el nombre de la lista sin ninguna otra función adicional para 
# convertirla a string como "str(miLista)", esto debido a que ya estamos convirtiendo los 
# elementos de esa lista en cadenas de texto, añadir str() podría generar problemas y/o conflicto
# con el funcionamiento del método .join. Ejemplo de como se podría usar:
# string = "".join(NuevoArray)

# 3. 