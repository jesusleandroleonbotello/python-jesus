# aver podemos importar modulos desde los archivos con solo import y el nombre
# existen tres tipos de modulos los de python que estan escritos c
# los propios que uno los puede hacer con nuestros archivos 
# y los de terceros que son hechos por otras personas o empresas

# cuando inportemos un modulo tenemos que ejecutarlo como viene y puede ser en una variable 
# se le ouede asignar un nuevo nombre al modulo con (as) 
# podemos inportar funciones dentro de los modulos 
# ejemplo:( from funciones import sumar )listo asi esta 

# import modulo_saludar as m_saludar

# desde ese modulo importamos dos funciones 
 #from modulo_saludar import saludar, saludar_raro

# creamos las variables con los saludos

#saludo = saludar("lucas")
#saludar_raro = saludar_raro("fran")

# mostrar los resultados
#print(saludar_raro)
#print(saludar)

# tambien se puede importar todas las funciones o objetos asi
# from modulo_saludar import * 
# recordar que modulo saludar es el nombre del archvo asi que es diferente en todo lo que importemos 
# "IMPORTANTE NO HACER ESTO SI SOLO NECESITAMOS UNA QUE OTRA YA QUE SI ES MUCHO SE PUEDE LAGEAR"


# podemos usar dir para ver las propiedades y el metodo de namespace "modulo"
# print(dir(modulo))