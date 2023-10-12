fd = open("lectura archivo/mbox-short.txt","r")
setEmail = set()
cl = 0 
for linea in fd:
    if linea.startswith("To:"):

        setEmail.add(linea.split()[1])

fd.close()
for email in sorted(setEmail):
    print(f"{email} enviado [ok]")