ingreso_mensual = 81000
gasto_mensual = 80000

#if anidados y else if (elif)
if ingreso_mensual > 10000:
    if ingreso_mensual - gasto_mensual < 0:
        print("Estás en déficit")
    elif ingreso_mensual - gasto_mensual > 3000:
        print("Bien pa, estás bien")
    else:
        print("Y pa, estás gastando una banda, hay que ver si te alcanza")
        
elif ingreso_mensual > 1000:
    print("Estas bien en latinoamérica")

elif ingreso_mensual > 500:
    print("Estás bein en Argentina")

elif ingreso_mensual == 200:
    print("Estás bien en Venezuela")

else:
    print("Sos pobre")