import io

Archivo = open("Christian Leonardo Celis Ardila/Persistencia _de_datos/nombres.txt","r")

texto = Archivo.read()
print(texto)


#best way to read a file cause can crash the computer in the other ways because of the memory
Archivo.seek(0)
texto2 = Archivo.readline()
print(texto2)

Archivo.seek(0)
texto3 = Archivo.readlines()
print(texto3)

Archivo.close()
