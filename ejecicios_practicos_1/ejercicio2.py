# ejercicio
# a) pedirle al usuario que diga cualquier texto real y:
#calcular cuanto tardaria en decir esa frase
#cuantas plabras dijo
# b) si se tarda mas de un minuto:
# decirle "para flaco tampoco te pedi un testamento"
# c) dalto habla un 30% mas rapido:
#¿cuanto tardaria el en decirlo?


# le pedimos al usuario que ingrese una frase o varias
frase = input("Decime una frase y te calculo cuantotardarias en decirla: ")

# creamos una lista con todas las palabras de la frese (se separan cada vez que hay un espacio en blanco)
palabras_separadas = frase.split(" ")

# usamos len() para ver la cantidad de datos que hay en la lista
cantidad_palabras = len(palabras_separadas)

# en caso de que tarde mas de un minuto, le decimos que pare un poco
if cantidad_palabras > 120:
    print("para flaco tampoco te pedi un testamento")

# calculamos cuanto tardaria en decir las palabras y se lo decimos
print(f"dijiste {cantidad_palabras} palabras, y tardarias {cantidad_palabras/2} segundos en decirlo")
print(f"dalto lo diria en {cantidad_palabras * 100 // 2 * 1.3 / 100} segundos")
