#variables declaradas se pueden modificar
a = 5
a = 10 # se modifico
b = 10
c = a + b
print(c)

nombre = "juan"
nombre = "jose" #se cambia a jose ahora, las variables son modificables
nombre = "yo"
print(nombre)

#una forma de sumar variables
numero = 10 
numero += 1 # aqui agarra el valor que ya tienes y el mas hace que le sume lo que esta despues del igual
numero += 4 #ahora se le suman mas al 11 dara 15
numero -= 2 # ahora dara 13
print(numero)

#ahora sigue concatenar
nombre = "juan"
apellido = "perez"
print(nombre + " " + apellido) # las comillas son para dejar un espacio

nombre1 = "hola " + nombre + " como estas" # forma dos de hacer
print(nombre1)

# ahora con los f strings
print(f"hola {nombre} como estas") # sirve para colocar "TODO" a texto

# podemos usar al operador del para borrardatos
#del nombre
#print(nombre) # dara error 

# operados de pertenencia in y not in
"juan" in "juanperez" # esta juan

nombre = "juan manuel"
print("juan" in nombre) #dara True
print("perez" in nombre) #dara False

#difiniendo una variable con camelcase
nombrePersona = "persona"
print(nombrePersona)

#definir una variable con snake_case
nombre_persona = "persona"
print(nombre_persona)

#en las variables se almacenan datos ya sea simples o complejos

