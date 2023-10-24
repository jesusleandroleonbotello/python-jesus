Nombre = input("Ingrese el nombre de usuario: ")
Est = int(input("Ingrese el estrato al que pertenece [1-5]: "))
Tarifa = 0

bandera = 1;

while(bandera!=0):
    if(Est==1):
        Tarifa = 10000
    elif(Est==2):
        Tarifa = 15000
    elif(Est==3):
        Tarifa = 30000
    elif(Est==4):
        Tarifa = 50000
    elif(Est==5):
        Tarifa = 65000

    print("*" * 40)
    print(f"El nombre del usuario es: {Nombre}")
    print(f"La tarifa de estrato {Est} es: {Tarifa}")
    print("*" * 40)

    Bandera = int(input("Desea continuar? 1 de lo contrario 0: "))

    if(Bandera!=0):
        Nombre = input("Ingrese el nombre de usuario: ")
        Est = int(input("Ingrese el estrato al que pertenece [1-5]: "))
    else:
        print("vuelva pronto-....")
