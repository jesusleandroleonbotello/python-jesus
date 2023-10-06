# creando una funcion con parametro args
def suma(*numeros): # args se refiere * lo que hace es hacer que todo despues de el sea una lista suma muchos numeros
    # no se pueden agregar mas parametros depues del * solo uno y antes de el si se pueden colocar 
    return sum(numeros) 
# ejecutando la funcion
resultado = suma(1,2,3,4,5,6,7,8,9,10)
print(resultado)

# creando una funcion con parametro kwargs
def suma(**numeros): # kwargs se refiere ** lo que hace es hacer que todo despues de el sea una un dic 
    return sum(numeros.values())
# ejecutando la funcion
resultado = suma(uno=1,dos=2,tres=3,cuatro=4,cinco=5,seis=6,siete=7,ocho=8,nueve=9,diez=10)
print(resultado)
# utilizando el operador * como argumento (*arsg)
# creando una funcion con parametro args conotro parametro
def suma(nombre,*numeros):
    return f"{nombre} la suma de tus numeros es: {sum(numeros)}"
# ejecutando la funcion
resultado = suma("Lucas",1,2,3,4,5,6,7,8,9,10)
#print(resultado)

# otra funcion igual mas optima que la anteriores
def suma_total(numeros): # en esta en los parametros no se coloca el arsg 
    # a ver esta forma sirve para poder pasar mas parametors a la funcion ya que el arsg es infinito y todo parametro por encima de el no se ejecuta
    return sum([*numeros])# se esta en una lista
# ejecutando la funcion
resultado2 = suma_total([1,2,3,4,5,6,7,8,9,10]) # al pasarle numeros dentro de la lista no los toma como lista y los suma
print(resultado2)
