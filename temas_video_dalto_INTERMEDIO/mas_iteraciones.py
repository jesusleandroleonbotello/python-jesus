# creando las listas 
frutas = ["banana","manzana","ciruela","pera","naranja","granada","durazno"]
cadena = "hola soy dalto"
numeros = [2,5,8,10]

# evitando que se coma una manzana con la secuencia continue
for fruta in frutas:
    if fruta == "manzana":
        continue
    print(f"me voy a comer una {fruta}")

# evitar que el bucle siga ejecutandose ( el else no se ejecuta tampoco)
for fruta in frutas:
    print(f"me voy a comer una {fruta}")
    if fruta == "pera":
        break
    else:
        print("bucle terminado")

# recorrer una cadena de texto ltra por letra
for letra in cadena:
    print(letra)

# for en una sola linea de codigo (duplicamos los nuemros)
numero_dupicados = [x*2 for x in numeros]
print(numero_dupicados)
