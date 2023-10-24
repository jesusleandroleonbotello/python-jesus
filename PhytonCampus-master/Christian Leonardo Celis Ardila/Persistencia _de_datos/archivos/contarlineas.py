fd = open("Christian Leonardo Celis Ardila/Persistencia _de_datos/archivos/mbox-short.txt","r")

cl = 0
cp = 0

for linea in fd:
    linea = linea.strip()
    for lin in linea.split():
        if lin.isalnum():
            cp+=1
    #cp += len(linea.split(" "))
    cl += 1

fd.close()
print("Cantidad de lineas: ", cl)
print("Cantidad de palabras: ", cp)
