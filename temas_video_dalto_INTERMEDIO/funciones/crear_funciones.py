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


#ejecutando la funcion con parametros llamando la función
#saludar("Lucas","M")
#saludar("Lucas","F")
#saludar("Lucas","O")
#saludar("Lucas","x")

# los parametros dentro de las funciones son las variables que vamos a usar que se dijitan por el usuario por asi decirlo
# se crean para ser usados dentro dela funcion y ya
# creando una funcion que nos retorne una contraseña random ("pero siempre sera igual solo es una idea")

def contraseñaRandom(num):
    letras = "abcdefghijklmnopqrstuvwxyz"  # esta servira para agregar lestra a la contraseña random
    num_entero = str(num)  # variable temporal leer abajo para entender
# con esto agarramos el numero y lo pasmos a cadena para agarrar solo el primer caracter
# che recordar que podemos agregar mas caracteres y ampliar los resultados de las contraseñas random por ahora sera solo 10
# che mire y no se puede pero si modifican o agregan otra variable nun con el segundo indice creo que si !IMPORTANTE!
# porque agarramos datos de 0 a 9 pero si agarramos dos caracteres llega a 100 claves diferentes se repiten si se ingresa el mismo numero
    num = int(num_entero[0]) # con esto agarramos el primer dijito para tener 10 resultados diferentes
    # si se quieren mas resultados solo agregar un indice mas a la variable ejemplo int(num_entero[0:1])
    # cantidad de letras random que sr meten
    c1 = num - 3
    c2 = num - 6 #esos - tal sirven para agarrar un numero de la cadena que ya tenemos de a - z
    c3 = num - 9# por eso los 10 resultados ya que si coloca 5 simepre buscara el resultado en la cadena 
# ahora que lo pienso para crear mas resultados se debne agregar mas letras ya que al restar 90 - 9 buscara el indice 81 y solo hay 26
    contraseña = f"{letras[c1]}{letras[c2]}{letras[c3]}{num *2}"# de aqui sale el resultado randon dependiendo de el numero puesto
    return contraseña # el retorn nos sirve para guardar el dato y darlo cuando llamemos la funcion 
    # es re importante el return para invocar la funcion en otro lado

# ejecutando la funcion sin input 
contraseña = contraseñaRandom(0)
#print(contraseña)

# ejecutando la funcion con input O SE PUEDE  colocar dento de la funcion pero aja como sea
#contraseña = contraseñaRandom(int(input("ingrese el numero de letras que quieres agregar: ")))
#print(contraseña)

# creando una funcion que suma dandole una lista 
#def sumaLista111(lista):
#    suma = 0
#    for num in lista:
#        suma += num # ese nas y igual es para que de una ves sume el numero siguiente 
#    return suma

# ejecutando la funcion
#suma = sumaLista111([1,2,3,4,5,6,7,8,9,10])
#print(suma) # che esta es una forma pero esta cochina 
