# creando un funcion simple
#def saludar(nombre):
    #print("Hola",nombre, "mi maestro como estas")
#ejecutando la funcion simple#
#saludar("Lucas")

# creando una funcion con parametros
def saludar(nombre,sexo):
    sexo = sexo.lower()
    if sexo == "m":
        print("Hola",nombre, "mi maestro como estas")
    elif sexo == "f":
        print("Hola",nombre, "mi maestra como estas")
    else:
        print("Hola",nombre, "mi cmpae como estas")


#ejecutando la funcion con parametros
saludar("Lucas","M")
saludar("Lucas","F")
saludar("Lucas","O")
saludar("Lucas","x")

