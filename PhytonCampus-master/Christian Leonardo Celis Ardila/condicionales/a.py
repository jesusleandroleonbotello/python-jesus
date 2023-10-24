num = input("Digite numero de telefono")
if num.startswith("+") and num.count("-")==2:
    partes = num.split("-")

    telefono = partes[1]
    print(telefono)
else:
    print("El telefono no cumple con el formato")