#Ejercicio 2. Ingresar un número y mostrar el cuadrado del mismo.El número debe ser mayor que cero, en caso de error que aparezca el mensaje "ERROR. Reingresar numero"

def ejercicio2():
    numero = int(input("¿Qué número quieres introucir?"))
    if numero<=0:
        print("ERROR. Reingresar numero")
    else:
        cuadrado = numero*numero
        print("El cuadrado de ",numero," es ",cuadrado)

if __name__ == '__main__':
    ejercicio2()


#En este ejercicio se hace uso de funciones como input() y print(). Además, se usan variables y condicionales if, else.