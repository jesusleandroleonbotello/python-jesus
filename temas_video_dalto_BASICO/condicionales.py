# los condicionales funcionan si esto es verdadero se ejecuta si no se ejecuta un segundo codigo

#if condicion:
#    accion

#edad = 18
#if edad >= 18:
#    print("es mayor de edad")
# si no se ejecuta el codigo que se encuentra dentro del if se ejecuta el codigo que se encuentra dentro del else

edad = 18
if edad >= 18:
    print("es mayor de edad")
    # todo lo que este dentro del if se cumple con if 
else:
    print("no es mayor de edad")
    # todo lo que este dentro del else se cumple con else
# si no se ejecuta el codigo que se encuentra dentro 

# ejemplo con datos escritos str
contraseña_almacenada = "soytupadre"
contraseña_usuario = "soytupadre"
if contraseña_almacenada == contraseña_usuario:
    print("contraseña correcta")
else:
    print("contraseña incorrecta")

# ahora se agrega mas condiciones que seria elif
# se pueden colocar if y else anidados al primer if o el que sea
# se debe colocar en el estacio de ese if  ejemplo
#horas = 3
#if horas >= 8:
#    print("es mucho")
#    if horas >= 12:
#        print("es mucho trabajo")
#    else:
#        print("no es mucho trabajo")#

ingreso_mesual = 10000
gasto_mensual = 8000
if ingreso_mesual >= 10000:
    print("el ingreso es mayor a 10000 eres rico")
    if ingreso_mesual - gasto_mensual > 1000:
        print("estas gatando mucho rey")
elif ingreso_mesual >= 5000:
    print("el ingreso es mayor a 5000 eres normal")
elif ingreso_mesual >= 1000:
    print("el ingreso es mayor a 1000 eres bajo")
else:
    print("el ingreso es menor a 1000 eres muy bajo")

