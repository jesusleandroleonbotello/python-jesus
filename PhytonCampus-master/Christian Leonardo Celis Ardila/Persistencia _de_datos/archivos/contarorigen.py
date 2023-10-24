 
df = open("Christian Leonardo Celis Ardila/Persistencia _de_datos/archivos/mbox-short.txt","r")

def mifun(email):
    return len(email)

cl = 0
conjuntoEmail = set()

for linea in df:
    if linea.startswith("From:"):
        conjuntoEmail.add(linea.split()[1])

df.close()


print("Cantidad de correos de origen distinto: ", len(conjuntoEmail))


for email in sorted(conjuntoEmail, key= mifun):
    print(email)