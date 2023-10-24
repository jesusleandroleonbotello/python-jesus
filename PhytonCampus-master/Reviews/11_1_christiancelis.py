dictserie = {}


def leernum(msg):
    while True:
        try:
            n = int(input(msg))
            if(n<0):
                return 0
            return n
        except Exception as e:
            print("error",e)


def ValidacionSerie(N):
    serie = 0
    for i in range(1, N+1):
        serie+= (1/i)*(-(-1)**i)
        dictserie[i] = (1/i)*(-(-1)**i)
    return serie
        
def main():
    num = leernum("Digite numero")
    if(num==0):
        print(num)
    else:
        serie = ValidacionSerie(num)
        print(dictserie.values())
        print(f'Resultado de la serie: {serie:,.2f}')       
main()