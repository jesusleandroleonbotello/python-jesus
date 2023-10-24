# Hacer un algoritmo que dada una nota (de 0.0 a 5.0), calcule la curva de 8 de la nueva nota.
# La curva de 8 se calcula multiplicando la nota por 0.8 y sumándole 1.

nota = float(input("Introduzca la nota a continuación. Solo de 0.0 a 5.0: "))
print(nota)

curvaDeOcho = (nota * 0.8) + 1
print("Su curva de 8 en la nota ingresada es: {:,.1f}".format(curvaDeOcho))