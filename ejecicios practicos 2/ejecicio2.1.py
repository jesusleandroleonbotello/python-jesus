# dalto el profe y los pibes van a armar la clase

#pedri la edad y el nombre de los compañero que vinieron hoy a clase

def obtener_compañeros(cantidad_de_compañeros):
    compañeros = [] # creamos la lista donde se guardaran los datos
    for i in range(cantidad_de_compañeros): # cleamos un bucle donde preguntara # cantidad de veces el nombre y la edad
        nombre = input("ingrese el nombre del compañero: ")
        edad = int(input("ingrese la edad del compañero: "))
        compañero =(nombre,edad) # creamos una tupla del lso datos de un solo estudiante
        compañeros.append(compañero) # agregamos el compañero a la lista
        compañeros.sort(key=lambda x:x[1]) # aqui lo que hacemos es ordenar los datos de la lista perousamos sort con un parametro
        # este parametro nos ayuda a organizarlos por una clave que ne este caso seria edad 
        # recordar que podemos elegir que parametro sera el que orde com buscar y ordenar la lista 
        # pra buscar se tiene en cuenta que estar organizados de menor a mayor
        # forma menor [0] el primer dato osea menor  y [0] porque buscamos el nombre y este esta en 0 ya que edad es 1
        asistente = compañeros[0][0] # esto es para busacr en la lista el dato con menor edad que sria asitente
        profesor = compañeros[-1][0] # con esto buscamos al que tiene mayor edad que estara a lo ultimo y el cero es para elegir nombre
    return asistente,profesor # retornamos la informacion
    
asistente,profesor = obtener_compañeros(6) # ponemos la cantidad de veces que preguntara nombre y edad la cantidad de personas 
print(f"el asistente es {asistente} y el profesor es {profesor}") # muetra al menor y al mayor
