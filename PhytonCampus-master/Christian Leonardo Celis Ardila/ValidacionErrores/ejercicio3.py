
bandera = 1
programa = ""
cont = 0
ValorNeto = 0
ValorMatricula = 0

while(bandera != 0):

    while True:
        try:
            codigo = input("Digite el codigo del estudiante: ")
            if(not codigo.isalnum):
                print("NO se aceptan caracteres especiales")
                continue
            break
        except Exception as e:
            print("Error:", e)
    
    while True:
        try:
            Nombre = input("Digite el nombre del estudiante: ")
            Nombre.strip()
            if(Nombre=="" or not Nombre.isalnum):
                print("Error hay un caracter no admitido")
                continue
            break
        except Exception as e:
            print("Error:", e)
    
    while True:
        try:
            print("*"* 30)
            print("1. Tecnico de sistemas\n")
            print("2. Tecnico en desarrollo de videojuegos")     
            print("3. Tecnico en animacion digital")
            print("*"* 30)
            n = int(input("Digite numero de programa ACADEMICO:"))
            if(n<1 or n>3):
                print("Numero fuera del rango")
                continue
            break
        except Exception as e:
            print("Error", e)

    while True:
        try:
            print("*"* 30)
            print("TIPO 1: rendimiento academico: 50% Matricula")
            print("TIPO 2. deporte: 40% Matricula")
            print("Tipo 3: No aplica")
            print("*"* 30)
            n2 = int(input("Digite el numero correspondiente al tipo de beca: "))

            if(n2<1 or n2>3):
                print("Numero fuera del rango")
                continue
            break
        except Exception as e:
            print("Error, no es un numero valido", e)    

    if(n2==1):
        Beca = 0.5
    elif(n2==2):
        Beca = 0.4
    else: Beca = 0

    if(n ==1):
        ValorMatricula = 800_000
        programa = "Tecnico de sistemas"
    elif(n ==2):
        ValorMatricula = 1_000_000
        programa = "Tecnico en desarrollo de videojuegos"

    elif(n ==2):
        ValorMatricula = 1_200_000
        programa = "Tecnico en Animacion digital" 

    ValorNeto = ValorMatricula - (ValorMatricula * Beca)
    
    print("*" * 30)    
    print(f"Nombre: {Nombre}")
    print(f"Codigo: {codigo}")
    print(f"Programa: {programa}")
    print(f"Valor Neto: ${ValorNeto:,.0f}")
    print("*" * 30)

    cont +=1

    while True:
        try:
            bandera = int(input("si desea continuar escriba 1 de lo contrario 0: "))
            if(bandera<0 or bandera>1):
                print("Valor fuera del rango")
                continue
            break

        except Exception as e:
            print("Error, numero invalido")


   

    if(bandera == 0):
        print("Vuelva Pronto")

print("Numero de veces", cont)