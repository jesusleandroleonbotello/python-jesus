# Este programa almacenará la solución de tres ejercicios distintos
# donde el usuario es quien decida elegir cuál solución probar.


# DEFINIENDO LAS FUNCIONES
def menu():
    while True:
        try:
            print("\n=== MENÚ PROGRAMA ===")
            print("1. Factorial de un número.")
            print("2. Calculadora salario de un empleado.")
            print("3. Calculadora de palabras en un párrafo.")
            print("4. Salir.")
            opcionUsuario = int(input("Escoja una opción (1-4): "))
            
            if opcionUsuario < 1 or opcionUsuario > 4:
                print("\nError: Elije una opción válida")
                continue
            return opcionUsuario
            
        except ValueError:
            print("Has elegido una opción errónea. Ingresa un número entero dentro del rango 1-4.")


# Ejercicio n°1: Factorial de un número.
def factorialNumero(num): 
    while True:        
        try:
            # DEFINICIÓN DE LAS VARIABLES NECESARIAS
            resultadoFactorial = 1
            numero = int(input(num))
            
            if numero < 0:
                print("Error: Debes ingresar un número entero positivo.")
                continue
            
            for i in range(1, numero + 1):
                resultadoFactorial *= i
                
            return resultadoFactorial
            
        except ValueError:
            print("Error al momento de digital el número. Inténtelo de nuevo.")
            

# Ejercicio n°2: 
def salary(horas):
    # DEFINICIÓN DE LAS VARIABLES NECESARIAS
    precioHora = 10
    porcentajeHorasExtra = 50
    
    while True:
        try:
            horasTrabajadas = int(input(horas))
            
            if horasTrabajadas < 0:
                print("Error: El número ingresado es inválido. Ingrese solo números positivos.")
                continue
            break
            
        except ValueError:
            print("Error: Ingrese un valor numérico válido.")
    
    if horasTrabajadas > 40:
        horasExtra = horasTrabajadas - 40
        
        precioHoraRegular = horasTrabajadas * precioHora
        precioHoraExtra = horasExtra * ((precioHora * porcentajeHorasExtra) // 100)
        precioTotal = precioHoraRegular + precioHoraExtra
        
    else:
        precioHoraRegular = horasTrabajadas * precioHora
        precioTotal = precioHoraRegular
    
    return precioTotal


# Ejercicio n°3

def palabrasParrafo(palabra):
    while True:
        try:
            palabras = input(palabra)
        
            if palabras == "" or palabras.isdigit():
                print("Error: Debes introducir una palabra, no una cadena vacía ni números.")
                continue
            break
        
        except Exception as e:
            print(f"Ha ocurrido un problema al ingresar la palabra. Error: {e}")
        
    palabrasArray = palabras.split(" ")
    print(palabrasArray)
    longitudPalabra = len(palabrasArray)
    
    return longitudPalabra
    


# ESTRUCTURA LÓGICA DEL PROGRAMA
while True:
    opcionUsuario = menu()

    if opcionUsuario == 1:
        print("\n\n*** FACTORIAL DE UN NÚMERO ***")
        resultadoFactorial = factorialNumero("Ingrese el número del que desea conocer su factorial: ")
        
        print(f"\nEl factorial del número ingresado es: {resultadoFactorial}")
    
    elif opcionUsuario == 2:
        print("\n\n*** CALCULAR SALARIO ***")
        resultadoSalario = salary("Ingrese las horas trabajadas: ")

        print(f"\nEl salario del empleado es de: {resultadoSalario}")
    
    elif opcionUsuario == 3:
        print("\n\n*** CALCULAR NÚMERO DE PALABRAS ***")
        resultadoPalabraCantidad = palabrasParrafo("Ingrese la(s) palabra(s) a contar: ")
        
        print(f"La cantidad de palabras que contiene la entrada anterior es de: {resultadoPalabraCantidad} palabras.")
    
    else:
        print("\n\nGracias por usar el software. Saliendo...")
        break
    
    input("Presione cualquier tecla para continuar.")