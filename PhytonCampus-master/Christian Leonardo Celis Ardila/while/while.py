num = int(input("INGRESE UN NUMERO ENTERO: "))
cpares = 0
cimpares = 0 



while(num!=-1):
    if(num%2==0):
        print("El numero es par")
        cpares += 1
    else:
        print("El numero es impar")
        cimpares += 1
    num = int(input("INgrese otro numero"))


print("Cantidad de numero pares es:", cpares)

print("Cantidad de numero impares es:", cimpares)
