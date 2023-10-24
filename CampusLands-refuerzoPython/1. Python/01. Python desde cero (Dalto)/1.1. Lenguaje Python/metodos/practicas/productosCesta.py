# Programa para practicar el tema de cadenas de texto.

productos = input("Ingrese los nombres de los productos separados por comas: ").strip()
productosArray = productos.split(",")

for i in range(len(productosArray)):
    print(productosArray[i].strip())