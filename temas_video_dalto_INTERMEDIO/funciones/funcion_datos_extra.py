# creando una funcion de tres parametros
#def frase(nombre,apellido,adjetivo):
#   return f"Hola {nombre} {apellido} sos muy {adjetivo}"

# ejecutando la funcion, usando keyword argumet para usar culaquier orden
#resultado_frase = frase(adjetivo = "capo", apellido = "leon", nombre = "jesus")
#print(resultado_frase)

# funcion con un parametro opcional que todas las que tengan parametros pueden serlo y dandole y valor por defecto
def frase(nombre,apellido,adjetivo = "tonto"): # estos son parametros forzados que ya vienen definidos en la funcion le odemos dar un nuevo valor a esta 
   return f"Hola {nombre} {apellido} sos muy {adjetivo}"

# ejecutando la funcion, usando keyword argumet para usar culaquier orden
resultado_frase = frase(adjetivo = "inteligente", apellido = "leon", nombre = "jesus") # qui le damos un nuevo valor al parametro
print(resultado_frase)