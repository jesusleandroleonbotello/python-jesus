# las excepciones nos ayudan e vitar un error que ya sabiamos y hacer una accion

#creando una funcion que sume numeros
def sumar_dos():
    # iniciando el bucle
    while True:
        # pidiendo numeros
        a = input("numero 1: ")
        b = input("numero 2: ")
        # intentando convertirlos a enteros y sumarlos
        try:
            resultado = int(a) + int(b)
        # si lanza una excepcion pedirle que reingrese los datos
        except ValueError as e:
            print("debe ser numeros ")
            print(f"ERROR :{e}")
        # si todo sale bien terminamos el buclee
        else:
            break
        finally:  # esto se va a ejecutar siempre
            print("tu puedes")
    # mostrando el resultado
    return resultado

print(sumar_dos())