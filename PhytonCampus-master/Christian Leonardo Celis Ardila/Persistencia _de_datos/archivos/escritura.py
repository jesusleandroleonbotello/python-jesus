Archivo = open("Christian Leonardo Celis Ardila/Persistencia _de_datos/archivos/salas.txt","w")

Archivo.write("SPUKNIK\n")
Archivo.write("APOLO\n")
Archivo.writelines(["HOUSTON\n","ARTEMIS\n"])
Archivo.close()

#modos de lectura: r  w  a
# r: leer
#w: escribir
# a : lectura y escritura o agregacion