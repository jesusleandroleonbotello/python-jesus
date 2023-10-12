#Ejercicio 1. Ingresar n números y mostrar su promedio:

def ejercicio1():
    numeros = int(input("¿Cuántos números quieres introducir? "))
    suma = 0.0
    for xxx in range(numeros):
        suma += float(input("Introduce un número: "))
    print("Has introducido", numeros, "números que suman ",
          suma, "y su media es", round(suma/numeros,2))
   
#if __name__ == '__main__':
ejercicio1()

#En cuanto al código es una función muy sencilla, se usa la función "range(n)", que lo que devuelve es una lista de 0 al n-1. Esto nos permite dar vueltas con el bucle "for" las veces especificadas por la n. Profundizaremos en esta función más adelante.
#La función "round(n,digits)" redondea el número "n" con los dígitos especificados en el segundo parámetro, si no se le da este número de dígitos lo redondea en un entero.
#Funciones como "int()" o "float()" transforman un "string" a dicho tipo.
#En cuanto a la función "input()" devuelve en forma de "string" lo que se escribe por consola en consecuencia del "string" que recibe dicha función como parámetro.