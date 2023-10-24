

def leernumeroint(msg):
    while True:
        try:
            num = int(input(msg))
            if(num<2):
                print("ERROR NUmero no puede ser negativo o menor a 2")
                continue
            return num
        except Exception as e:
            print("Error ", e)



def crearMatrices(fil,col):
    m = []
    for i in range(fil):
        fila = [0] * col
        m.append(fila)
    return m

def imprimirMatrices(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j] ,end="\t")
        print("")

def llenarMatriz(mat):
    for f in range(len(mat)):
        for c in range(len(mat[f])):
            mat[f][c] = int(input(f"mat[{f+1}][{c+1}]? "))


def Caso1Matriz(mat):
    cont = 1
    for f in range(len(mat)):
        for c in range(len(mat[f])):
            mat[f][c] = cont
            cont+=1
    print("")

def Caso2Matriz(mat,tamaño):
    for f in range(len(mat)):
        cont = tamaño + 1
        for c in range(len(mat[f])):
            mat[f][c] = c+1
            if(f%2 !=0):
                cont-=1
                mat[f][c] = cont
            
    print("")


def Caso3Matriz(mat):
    num =  1
    for f in range(len(mat)):
        for c in range(len(mat[f])):
            mat[f][c] = 0
            if(f == c):
                 mat[f][c] = 1
    print("")
            

def Caso4Matriz(mat,tamaño):
    menor = 0
    mayor = tamaño-1
    for f in range(len(mat)):
        for c in range(len(mat[f])):
            mat[f][c] = 0
            if(f==menor and c==mayor):
                mat[f][c] = 1
                menor += 1 
                mayor -= 1 
                
    print("")

def Caso5Matriz(mat,tamaño):
    cont = 0
    for f in range(len(mat)):
        for c in range(len(mat[f])):
            mat[f][c] = 0
            if(cont>=c):
                mat[f][c] = 1

        cont+=1    
    print("")

def Caso6Matriz(mat,tamaño):
    cont = 0
    for f in range(len(mat)):
        for c in range(len(mat[f])):
            mat[f][c] = 0
            if(cont<=c):
                mat[f][c] = 1

        cont+=1    
    print("")


def Caso7Matriz(mat):
    cont = 1
    for f in range(len(mat)):
        for c in range(len(mat[f])):
            mat[c][f] = cont
            cont+=1
    print("")

def Caso8Matriz(mat,tamaño):
    cont = 0
    for f in range(len(mat)):
        for c in range(len(mat[f])):
            mat[f][c] = " "    
            if(cont>=c):
                mat[f][c] = "A"
                if(c%2!=0):
                    mat[f][c] = "B"
        cont+=1    
    print("")




def main():
    num = leernumeroint("Digite el valor de la matriz cuadrada ej: 2= 2*2: ")
    matriz =  crearMatrices(num,num)
    #llenarMatriz(matriz)
    Caso1Matriz(matriz)
    imprimirMatrices(matriz)
    Caso2Matriz(matriz,num)
    imprimirMatrices(matriz)
    Caso3Matriz(matriz)
    imprimirMatrices(matriz)
    Caso4Matriz(matriz,num)
    imprimirMatrices(matriz)
    Caso5Matriz(matriz,num)
    imprimirMatrices(matriz)
    Caso6Matriz(matriz,num)
    imprimirMatrices(matriz)
    Caso7Matriz(matriz)
    imprimirMatrices(matriz)
    Caso8Matriz(matriz,num)
    imprimirMatrices(matriz)

main()