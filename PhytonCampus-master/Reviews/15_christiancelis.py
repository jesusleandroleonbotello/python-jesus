fl = open("Christian Leonardo Celis Ardila/Persistencia _de_datos/archivos/mbox-short.txt","r")

def mifun(email):
    return len(email)


conjuntoEmail = []

for linea in fl:
    if linea.startswith("From: "):
        if not linea.split()[1] in conjuntoEmail:
            conjuntoEmail.append(linea.split()[1])

fl.close()

#print("Cantidad de correos de origen distinto: ", len(conjuntoEmail))

fl2 = open("Reviews/mensajesenviados.txt","w")
for email in reversed(conjuntoEmail):
    mensajeenviado = f"{email}, enviado [ok]"
    fl2.write(mensajeenviado+ "\n")

fl2.close()