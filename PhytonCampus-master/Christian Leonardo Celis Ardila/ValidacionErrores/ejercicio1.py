while True:
    try:
        num = int(input("Ingrese un numero: "))
        break
    except ValueError:
        print("Error de tipo: Numero no valido: ")

while True:
    try:
        num2 = int(input("Ingrese otro numero: "))
        break
    except ValueError:
        print("Error de tipo: Numero no valido: ")

try:
    num2 = "a"
    suma = num + num2
    print(suma)
except Exception as e:
    print("Error al intentar sumar:", e)

