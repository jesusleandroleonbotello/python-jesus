cadena1 = "hola soy"
cadena2 = "leandro c4"

# print(dir(cadena1)) # el dir nos dice que los metodos que le podemos colocar a esa cadena 
# o lo que se ponga dentro del parentesis
# recordar que dir es una funcion

resultado = cadena1.upper
print(resultado)
resultado = cadena1.lower
print(resultado)
resultado = cadena1.capitalize
print(resultado)

"upper" # convierte a mayusculas
mayus = cadena1.upper
"lower" # convierte a minusculas
minusculas = cadena1.lower
"capitalize" # convierte a mayusculas y minus
mayuculas_inicial = cadena1.capitalize
"find" # encuentra la primera aparicion del valor dicho si no da -1
encontrar1 = cadena1.find
"index" # encuentra la primera aparicion del valor dicho si no da una exception
encontrar2 = cadena1.index
"isnumeric" # si es numerico da True
numerico = cadena1.isnumeric
"isalnum" # si es alfanumerico da True
alfanumerico = cadena1.isalnum
"isalpha" # si es alfabetico da True
alfabetico = cadena1.isalpha
"islower" # si es minuscula da True
"isupper" # si es mayuscula da True
"isspace" # si es espacio da True
espacio = cadena1.isspace
"istitle" # si es un titulo da True
titulo = cadena1.istitle
"isdecimal" # si es decimal da True
decimal = cadena1.isdecimal
"isdigit" # si es numerico da True
"isidentifier" # si es un identificador da True
identificador = cadena1.isidentifier
"isprintable" # si es un printable da True
printable = cadena1.isprintable
"isascii" # si es ascii da True
ascii = cadena1.isascii
"isidentifier" # si es un identificador da True
"count" # devuelve el numero de ocurrencias de una sudcadena de una cadena dada
ocurrencias = cadena1.ocurrencias
"len" # cuenta los caracteres de una cadena len es una funcion
longitud = len(cadena1)
"startswith" # devuelve True si la cadena empieza con el valor dado
"endswith" # devuelve True si la cadena termina con el valor dado
"replace" # remplaza un valor por otro
"split" # devuelve una lista de cadenas separadas por el valor dado
cadena_separada = cadena1.split(",")
"splitlines" # devuelve una lista de lineas separadas por el valor dado
"strip" # devuelve una cadena sin espacios en blanco
"lstrip" # devuelve una cadena sin espacios en blanco izquierda
"rstrip" # devuelve una cadena sin espacios en blanco derecha
"center" # devuelve una cadena centrada en el valor dado
"zfill" # devuelve una cadena con el valor dado rellenado con ceros
"join" # devuelve una cadena con los valores dadas separados por el valor dado
"replace" # devuelve una cadena con los valores dadas separados por el valor dado (remplaza)
cadena_nueva = cadena1.replace("hola","hello")
