fd = open("Christian Leonardo Celis Ardila/Persistencia _de_datos/archivos/mbox-short.txt","r")

fd2 = open("Christian Leonardo Celis Ardila/Persistencia _de_datos/archivos/envioemails.txt","w")

lstEMail  = []

for linea in fd:
    if(linea.startswith("From:")):
        email = linea.split()[1]
        if email not in lstEMail:
            lstEMail.append(email)
            msg = f"{email},enviado [ok]"
            print(msg)

for i in range(len(lstEMail)-1,0-1,-1):
     msg = f"{lstEMail[i]},enviado [ok]"
     fd2.write(msg + "\n")

fd.close()
fd2.close()