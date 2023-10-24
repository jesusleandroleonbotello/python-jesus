n1 = int(input("Digite un numero: "))
n2 = int(input("Digite otro numero: "))
n3 = int(input("Digite otro numero: "))



if(n1>n2 and n1>n3):
    mayor = n1
elif(n2>n1 and n2>n3):
    mayor = n2
elif(n3>n1 and n3>n2):
    mayor = n3

if(n1<mayor):
    intermedio = n1
elif(n2<mayor):
    intermedio = n2
elif(n3<mayor):
    intermedio = n3


if(n1<intermedio):
    menor = n1
elif(n2<intermedio):
    menor = n2
elif(n3<intermedio):
    menor = n3


print(mayor) 
print(intermedio)
print(menor)


    