num = int(input("Ingrese un numero: "));
factorial=1;


for i in range(1, num+1):
    factorial  = factorial * i


print("El factorial de "+ str(num) + " es: " + str(factorial))