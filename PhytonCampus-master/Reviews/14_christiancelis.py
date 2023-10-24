def leernombre(msg):
    while True:
        try:
            n = input(msg)
            n.strip()
            if(n==0 or not n.isalnum()):
                print("Nombre no valido")
            return n
        except Exception as e:
            print("Error al ingresar el nombre", e)

def leerint(msg):
    while True:
        try:
            n = int(input(msg))
            if(n<1):
                print("Valor invalido, debe ser mayor a cero")
            return n
        except Exception as e:
            print("Error al ingresar el numero", e)

def llenarMatriz(mat,dictciudades):

    for f in range(1):
        for c in range(len(mat[f])):
            nombreciudad = leernombre(f"Escriba el nombre de la ciudad en la red ferrovial{c+1}: ")
            mat[f][c] =  nombreciudad
            numeroCiudades = leerint("Digite numero de ciudades enlazadas: ")
            ciudadesenlazadas = []
            ciudadesenlazadas.append(nombreciudad)
            for i in range(numeroCiudades):
                ciudadesenlazadas.append(leernombre(f"Ciudadenlazada {i+1} "))   
                dictciudades[nombreciudad] = ciudadesenlazadas
    return

def main():
    dictRed = {}
    
    matrizCiudades = []

    linkedCities = []
    
    numeroCiudades = leerint("Digite numero de ciudades: ")

    filas = [" "] * numeroCiudades
    
    matrizCiudades.append(filas)
    
    print(matrizCiudades)
    
    llenarMatriz(matrizCiudades,dictRed)
    
    print(matrizCiudades)
    print(dictRed)

    ciudad1 = leernombre("Digite la ciudad 1 a comparar")
    ciudad2 = leernombre("Digite la ciudad 2 a comparar")

    for k, v in dictRed.items():
        print(v)
        if ciudad1 in v and ciudad2 in v  or ciudad1:
            print("Estan en via directa")
        else:
            print("No estan en via directa")

main()