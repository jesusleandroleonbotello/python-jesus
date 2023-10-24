bandera = False

def primo(num):
    bandera = False
    cont = 0
    divisor = ""
    sum = 0
    for i in range(1,num +1):
        if(num%i==0):
            cont +=1
            sum = sum + i

        if(cont==2 and sum == (num+1)):
            bandera = True
        
        if(cont>3):
            bandera = False
            break
    return bandera


def leernumeroint(msg):
    while True:
        try:
            num = int(input(msg))
            if(num<0):
                print("ERROR NUmero no puede ser negativo")
                continue
            return num
        except Exception as e:
            print("Error ", e)


def imprimirprimos(n1,n2):
    lstprimos = []
    cont = 0
    for i in range(n1,n2+1):
        bandera = primo(i)
        if(bandera == True):
            cont +=1
            lstprimos.append(i)
    
    print(f"Los números primos entre [{n1} y {n2}) son:")
    return print(lstprimos, f"[{cont} primos]")
 

def main():
    n1 = leernumeroint("Digite un numero entero: ")
    n2 = leernumeroint("Digite otro numero entero: ")

    imprimirprimos(n1,n2)




main()
