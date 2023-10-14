# taller jesus leandro leon botello
dato = open("mbox-short.txt","r")
dato1 = open("mbox.txt","r")

def lambda2(lista): # mejor
    suma = 0
    for num in lista:
        suma += float(num)
    lambda2 = suma / len(lista)
    return lambda2

set_email = set()
setEmail = set()

for linea in dato:
    if linea.startswith("X-DSPAM-Confidence:"):
        setEmail.add(linea.split()[1])
        lambda2(setEmail)

for linea in dato1:
    if linea.startswith("X-DSPAM-Confidence:"):
        set_email.add(linea.split()[1])
        lambda2(set_email)

dato.close()
dato1.close()

while True:
    try:
        cd = input("Ingrese el nombre de su archivo: ")
        if cd == "mbox-short.txt":
            dato = open("mbox-short.txt","r")
            print("Avareje spam confidence : ",lambda2(setEmail))
            dato.close()
            break
        elif cd == "mbox.txt":
            dato1 = open("mbox.txt","r")
            print("Avareje spam confidence : ",lambda2(set_email))
            dato1.close()
            break
        else:
            print("El archivo no se ha encontrado ")
    except Exception as e:
        print(f"Errorcon el archivo: {e}")