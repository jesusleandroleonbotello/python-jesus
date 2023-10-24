n = int(input("Digite cuantos usuarios hay: "))


TotalConsumo = 0

for i in range(1,n+1):
    print("Datos del usuario #" + str(i))
    codigo = input("Digite el codigo del usuario: ");
    nom = input("Digite el nombre del usuario: ");
    est = input("Digite el estado [S: Suspendido / V: Vigente]: ");
    estrat= input("Digite el estrato: ");
    consumo= int(input("el consumo del mes=?: "));

    if(est == "V" or est == "v"):
        if(estrat == 1):
            tarifa = 10_000
        elif(estrat == 2):
            tarifa = 20_000
        elif(estrat == 3):
            tarifa = 30_000
        elif(estrat == 4):
            tarifa = 45_000
        elif(estrat == 5):
            tarifa = 60_000
        elif(estrat == 6):
            tarifa = 70_000
        else:
            tarifa = 0

        valconsumo = consumo * 200


        #Calcular el valor a pagar

        valpag = tarifa - valconsumo

        TotalConsumo += valpag

        #imprimir

        print()
        print("=" * 20)
        print(f"Nombre: {nom}")
        print(f"Tarifa: {tarifa}")
        print(f"Valor del Consumo{consumo}")
        print(f"Valor a pagar: {valpag}")
        print()
        print("=" * 20)
        print()
        print(f"Valor Total: {TotalConsumo}")
       
        


        