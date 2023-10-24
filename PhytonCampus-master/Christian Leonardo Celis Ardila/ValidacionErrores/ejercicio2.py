#Validar Nombre del usuario:
bandera = 1
Tarifa = 0

while(bandera!=0):

    while True:
        try:
            Nombre = input("Ingrese el nombre de usuario: ")
            Nombre.strip()
            if(Nombre == "" or not Nombre.isalnum()):
                continue
            break  
        except Exception as e:
            print("Error", e)

    while True:
        try:
            Est = int(input("Ingrese el estrato al que pertenece [1-5]: "))
            if(Est<1 or Est>5):
                print("Intente de nuevo")
                continue
            break
        except Exception as e:
            print("Error", e)


    if(Est==1):
        Tarifa = 10000
    elif(Est==2):
        Tarifa = 15000
    elif(Est==3):
        Tarifa = 30000
    elif(Est==4):
        Tarifa = 50000
    elif(Est==5):
        Tarifa = 60000

    print("*" * 40)
    print(f"El nombre del usuario es: {Nombre}")
    print(f"La tarifa de estrato {Est} es: ${Tarifa:,.0f}")
    print("*" * 40)

    Bandera = int(input("Desea continuar? 1 de lo contrario 0: "))

    if(Bandera ==0 ):
        print("vuelva pronto-....")
