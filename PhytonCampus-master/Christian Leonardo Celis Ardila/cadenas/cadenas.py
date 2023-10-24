#Cadenas

s = "Yo soy tu padre"

print(s[7])
# print(s[-8])

# #recorrer cadenas

# for i in range(len(s)):
#     print(s[i], end=",")

# #recorrido por elemento

# for i in s:
#     print(i, end=",")

#slice --- porcion
print(s[3:])
print(s[4:7])
print(s[::-1]) #invertir una cadena.

print("tu" in s)
print("yt" not in s)

s = s.upper()

print(s)

s=s.lower()

print(s)

s = s.capitalize()
print(s)

s = s.title()
print(s)

print(s.count("a"))

print(s.find("Pa")) #inicio a final

print(s.rfind("Pa")) ##de final al principio e imprime el indice de la ultima aparición


print(s.isdigit())

print(s.isalnum())
print(s.isalpha()) #devuelve true si la cadena es alphabetica
s = s.lower()
print(s.islower())
print(s.isupper())

print(s.isspace()) #SI LA CADENA TIENE ESPACIOS
print(s.startswith("y"))
print(s.endswith("y"))

print(s.split())
print(s.split("soy"))

print(s.join(","))

#.strip borra espacio delante y detras de la cadena.
#.replace -> reemplaza una cadena por otra.

