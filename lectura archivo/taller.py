import random

lista_emails = []
lista_destino = []
enviar = set()
destino = set()

def enviar_email(email, enviar):    
    for enviar in sorted(enviar, reverse=True):
        lista_emails.append(f"{enviar} se envio a {email} [ok]\n")
        print(f"\n{enviar} se envio a {email} [ok]", end="")
    return lista_emails

def elegir_email(email_list):
    numero_alazar = random.randrange(0, len(email_list))
    return numero_alazar

def crear_archivo(lista_email):
    informacion_archivo = open("lectura archivo\mensajes_archvo.txt", "w")
    
    for i in range(len(lista_email)):
        informacion_archivo.write(lista_email[i])
    
    informacion_archivo.close()


fd = open("lectura archivo\mbox-short.txt", "r")

for linea in fd:
    if linea.startswith("From:"):
        destino.add(linea.split()[1])
fd.close()

direccion_email = open("lectura archivo/mbox-short.txt", "r")

for linea in direccion_email:
    if linea.startswith("To:"):
        enviar.add(linea.split()[1])
direccion_email.close()

for destino in sorted(destino, reverse=False, key=lambda x:x):
    lista_destino.append(destino)
    
while not len(lista_destino) == 0:
    resultado_alazar = elegir_email(lista_destino)
    email = lista_destino.pop(resultado_alazar)
    lista_emailss = enviar_email(email, enviar)

crear_archivo(lista_emailss)