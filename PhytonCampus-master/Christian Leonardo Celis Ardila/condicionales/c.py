fecha = input("Digite la fecha en formato dd/mm/aaaa: ")
bandera =  True 
division = fecha.split("/")

if(fecha.count("/")==2 and (len(division[0]))==2 and (len(division[1]))==2 and (len(division[2])==4)):
    for i in division:
        if( not i.isdigit()):
            bandera = False
            break
else:
    print("Formato incorrecto")

if(bandera==False):
    print("Formato incorrecto")
else:
    dia = division[0]
    mes = division[1]
    año = division[2]

    print(f"dia : {dia}")
    print(f"mes : {mes}")
    print(f"año : {año}")
