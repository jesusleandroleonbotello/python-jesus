import io
fd = open("Christian Leonardo Celis Ardila/Persistencia _de_datos/archivos/nombres.txt","r")

fd2 = open("Christian Leonardo Celis Ardila/Persistencia _de_datos/archivos/backupnames.txt","w")

for linea in fd:
    fd2.write(linea)

fd.close()
fd2.close()



