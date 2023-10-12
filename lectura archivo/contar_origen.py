# un programa que cuente los correos de origen distintos que hay en el archivo

def mifun(email):
    return len(email)

fd = open("lectura archivo/mbox-short.txt","r")
setEmail = set()
cl = 0 
for linea in fd:
    if linea.startswith("From:"):
        #cl += 1
        #email = linea.split()[1]
        #print(email)
        setEmail.add(linea.split()[1])

fd.close()
cl = len(setEmail)
print("la cantidad de correos de origen son: ",cl)
for email in sorted(setEmail, reverse=False, key=mifun):
    print(email)