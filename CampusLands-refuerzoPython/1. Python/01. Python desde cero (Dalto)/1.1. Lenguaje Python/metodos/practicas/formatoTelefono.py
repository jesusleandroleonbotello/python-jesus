# Programa para practicar el tema de cadenas de texto.

numeroTelefono = input("Ingrese el número telefónico de la empresa en el formato prefijo-número-extensión (Ej: +34-913724710-56): ").strip()
print(numeroTelefono.split("-")[1])