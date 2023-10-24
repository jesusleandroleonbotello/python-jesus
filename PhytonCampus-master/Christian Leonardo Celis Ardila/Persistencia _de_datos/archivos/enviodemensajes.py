fl = open("Christian Leonardo Celis Ardila/Persistencia _de_datos/archivos/mbox-short.txt","r")

def mifun(email):
    return len(email)


conjuntoEmail = set()

for linea in fl:
    if linea.startswith("To:"):
        conjuntoEmail.add(linea.split()[1])

fl.close()

print("Cantidad de correos de origen distinto: ", len(conjuntoEmail))


for email in conjuntoEmail:
    print(email,"enviado", "[ok]")