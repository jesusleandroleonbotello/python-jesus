# Programa para practicar el tema de cadenas de texto.

frase = input("Ingrese una frase: ").strip().capitalize()
vocal = input("Ingrese una vocal en minúscula: ").strip()

print(frase.replace(vocal, vocal.upper()))