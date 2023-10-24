# Programa para practicar el tema de cadenas de texto.

precioProducto = input("Ingrese el precio del producto: ")
print(precioProducto[:precioProducto.find('.')], "euros y", precioProducto[precioProducto.find('.')+ 1], 'céntimos.')