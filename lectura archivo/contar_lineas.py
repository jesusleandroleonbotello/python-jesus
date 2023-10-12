fd = open("lectura archivo/mbox-short.txt","r")
cp = 0
cl = 0
for linea in fd:
    linea = linea.strip()
    #cp += len(linea.split())
    for lin in linea.split(" "):
        if lin.isalnum():
            cp += 1
    cl += 1

fd.close()

print("cantidad de lineas:", cl)
print("cantidad de palabras", cp)