# Programa para practicar el tema de cadenas de texto.

#SOLUCIÓN DE LA FORMA CORTA
frase = input("Escriba una frase: ")
print(frase[::-1])


#SOLUCIÓN DE LA FORMA LARGA
# for i in range(len(frase) - 1, -1, -1):
#     print(frase[i], end="")