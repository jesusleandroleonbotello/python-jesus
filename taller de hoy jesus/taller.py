# crear uuna funcion que reciba un valor n y esta esta en un bucle depende el valor puesto y inprimir el resultado
# recordar que el valor debe ser diferente de cero o dara cero
import math
num = 0
#def numero_bueno(num):
#    num = int(input("Ingrese un numero: "))
#
#    n = num
#    if n != 0:
#        for i in range(1, 1 - 1/2 + 1/3 - 1/4 + ... + 1/n):
#            resultado = float(i)
 #           resultado1 = str(len(i))
#            return resultado,resultado1
#    else:
#        print("numero debe ser diferente de sero")
#        return numero_bueno(num)
    
##print(numero_bueno(num))



# punto 2



def es_primo(numero):
    for i in range(2,numero-1): # aqui especificamos que 2 para que no se divida por dos y le colocamos -1 para que el mismo numero no se de 
        if numero % i == 0: return False # si es divicible por alguno tornamos False y cerramos bucle
    return True# si termina 

def primos_hasta(num):
    # creamos una lista
    primos = []
    for i in range(2,num+1): 
        resultado = es_primo(i) # verificamos si es primo
        if resultado == True : primos.append(i) # si lo es lo agregamos a la lista
        # devolvemos la lista
    return primos 
numero = 0
def entero(numero):
    num1 = input("Ingrese un numero: ")
    num2 = input("Ingrese el segundo numero: ")
    if int(num1) and int(num2) is True:
        if num1 <=2 and num1> num2 is True :
            primos_hasta(num)
    else:
        print("debe ser un numero entero ")
        return entero(numero) 
    return primos_hasta(num)



resultado = entero(numero)
print(resultado)