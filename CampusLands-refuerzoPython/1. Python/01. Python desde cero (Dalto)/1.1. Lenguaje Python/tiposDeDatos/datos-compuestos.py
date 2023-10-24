# Un dato compuesto se compone de 1 o más datos simples u otros datos compuestos.


#Creando una lista (Se pueden modificar)
lista = ["David Mateo", "No tengo jefe :c", True, 1.73]

#Creando una tupla (No pueden modificar)
tupla = ("David Mateo", "No tengo jefe :c", True, 1.73)

#Esto es válido
lista[3] = "Repámpanos :O"

#Esto NO es válido
# tupla[3] = "Rayos y Centellas ._."


#Creando un conjunto (set)
conjunto = {"David Mateo", "No tengo jefe :c", True, 1.73}
# print(conjunto[3]) -> No puede acceder al elemento.


#Creando un diccionario (dict)
diccionario = {
    "nombre": "David Mateo",
    "esta_emocionado": True,
    "altura": 1.73,
    "peso": 64,
    "dato_duplicado": "David Mateo"
}

print(diccionario["altura"])
print(lista[3])



# NOTAS:
# 1. Las listas se pueden modificar.
#   1.1. Una lista sería un ejemplo de una matriz sencilla.
#
# 2. Las tuplas son listas, pero de solo lectura, nunca se modificarán.
#   2.1. Para acceder a un valor de una tupla, se hace lo mismo que al querer acceder a un valor de una lista.
#
# 3. Los conjuntos no tienen un orden fijo (Desordenados), y pueden intercambiarse sin afectar los datos en él.
#   3.1. Los datos ya almacenados no se pueden modificar. Solo reconstruir.
#   3.2. No permite mostrar los elementos por su índice.
#   3.3. No puede haber datos duplicados (Útil para eliminar elementos repetidos).
#   3.4. Los conjuntos se pueden iterar.
#
# 4. La estructura en un diccionario es "Clave-Valor" o en inglés "key-value".
#   4.1. Los elementos pares "key : value" se separan por comas a excepción del último.
#   4.2. Los diccionarios en Python tienen una estructura algo parecida a un JSON.