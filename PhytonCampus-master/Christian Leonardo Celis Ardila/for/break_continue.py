# #CAlcular si un numero es primo o no. divisible por si mismo o uno
# num = int(input("Digite un numero: "))
# if(num<2):
#     print("No es primo")
# elif(num==2):
#     print("Es primo")
# else:
#     bandera = True

#     for i in range(2, num):
#         if(num%i==0):
#             bandera=False
#             break
#     if(bandera==True):
#         print("Es primo")
#     else:
#         print("NO es primo, lo divide, ", i)


##CONTINUE

#Salta una iteraccion de un ciclo

#Imprima los numeros del 1 al 100 excepto los multiplos de 7-.


# for i in range(1,100):
#     if(i%7==0):
#         continue
#     else:
#         print(i,end=" ")


#Lanzamiento de dados
#100 veces el dado, cuantas veces cae el 5

import random

Cae5 = 0

for i in range(100):
    dado = random.randrange(1, 7)
    if(dado ==5):
        Cae5 += 1

print(f"El lado 5 cayo {Cae5} veces")
