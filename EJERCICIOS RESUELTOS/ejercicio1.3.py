#Ejercicio 3. De 10 números ingresados indicar cuantos son mayores a cero y cuantos son menores a cero.

def ejercicio3():
    numeros = int(input("¿Cuántos números quieres introducir? "))
    mayores = 0
    menores = 0
    for x in range(numeros):
        numero = int(input("Introduce un número: "))
        if(numero>0):
            mayores+=1
        elif(numero<0):
            menores+=1
    print("Tendríamos un total de",mayores,"números mayores que 0 \n",menores,"números menores que 0.")

if __name__ == '__main__':
    ejercicio3()


#En este ejercicio hacemos uso del bucle for in, además del uso de condicionales como if y elif. También, disponemos de acumuladores para ir contando