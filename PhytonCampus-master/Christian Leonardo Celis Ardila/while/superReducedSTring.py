

i = 0

cadena = input("Digite una cadena: ")
cadena = cadena.lower()


while True:
    if(i==len(cadena)-1):
        break
    
    if(cadena[i]==cadena[i+1]):
        print(cadena[i])
        print(cadena[i+1])
        cadena.split(",")
        print(cadena)
        borrado = cadena[i:i+1]
        cadena = cadena[0:i-1] + cadena[i+2:]
        i = 0

    i+=1



print(cadena)

