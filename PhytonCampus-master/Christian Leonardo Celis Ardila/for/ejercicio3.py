#secuencia}

#hacer un programa en phyton que genere el siguiente numero de la secuencia: 


#1,1,2,-1,1,-2,?

n1 = 1
n2 = 1
sig = -1
res = 0


for i in range(6):
   res = n1 + (sig**i) * n2
   n1 = n2
   n2 = res


print(res)