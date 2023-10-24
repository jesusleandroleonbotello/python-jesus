# Construya un programa que verifique si un número dado es perfecto. Un número perfecto es
# un número entero positivo que es igual a la suma de sus divisores propios positivos (excluyendo
# el número mismo). En otras palabras, si sumas todos los divisores propios de un número
# perfecto, el resultado será igual al número original.
# 
# Por ejemplo, el número 6 es considerado un número perfecto. Sus divisores propios son 1, 2 y
# 3. Si sumamos estos números: 1 + 2 + 3 = 6, obtenemos el mismo número original.



# DEFINIENDO LAS VARIABLES PRINCIPALES
numero = int(input("Ingrese el número que deseea comprobar a continuación: "))
sumarNumeros = 0

print("Entrada usuario:", numero, "\n")


for i in range(1, numero):
    if numero % i == 0:
        sumarNumeros += i


if numero == sumarNumeros:
    print(f"¡El número {numero} que ingresaste es perfecto!")
else:
    print(f"¡El número {numero} que ingresaste NO es perfecto!")