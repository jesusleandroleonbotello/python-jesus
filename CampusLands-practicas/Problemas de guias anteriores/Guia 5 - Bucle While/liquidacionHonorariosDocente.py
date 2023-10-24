# Este programa tiene como objetivo determinar mediante una entrada de usuario
# la liquidación de uno o más docentes de manera casi que automática
# siguiendo unos parámetros establecidos por la compañía (Ejercicio en este caso).


# DEFINIENDO LAS VARIABLES PRINCIPALES
isVerdadero = True
valorTotalPagar = 0
docentesCatA = 0
docentesCatB = 0
docentesCatC = 0


while isVerdadero:
    documento = int(input("\nIngrese el documento de identidad: "))
    nombre = input("Ingrese el nombre: ")
    categoriaDocente = input("Ingrese la categoría del docente (A, B o C): ")
    horasLaboradasMes = int(input("Ingrese las horas laboradas en el mes: "))
    
    if categoriaDocente.upper() == "A":
        valorHora = 25000
        categoriaNombre = "Artística y Música"

        valorHonorariosDocente = horasLaboradasMes * valorHora
        valorTotalPagar += valorHonorariosDocente
        docentesCatA += 1
    
    elif categoriaDocente.upper() == "B":
        valorHora = 35000
        categoriaNombre = "Informática"

        valorHonorariosDocente = horasLaboradasMes * valorHora
        valorTotalPagar += valorHonorariosDocente
        docentesCatB += 1
    
    elif categoriaDocente.upper() == "C":
        valorHora = 50000
        categoriaNombre = "Matemática"

        valorHonorariosDocente = horasLaboradasMes * valorHora
        valorTotalPagar += valorHonorariosDocente
        docentesCatC += 1
    
    else:
        print("Error: Ingresa una categoría válida. Saliendo...")
        isVerdadero = False
        break
    
    
    #Imprimir los datos correspondientes en pantalla
    print("\n", "=" * 35)
    print(f"Profesor: {nombre}")
    print(f"Documento de Identidad: {documento}")
    print(f"Categoría del docente: {categoriaDocente} --> {categoriaNombre}")
    print(f"Horas laboradas en el mes: {horasLaboradasMes} horas")
    print(f"Valor a pagar por honorarios: ${valorHonorariosDocente:,.0f} COP")
    
    
    #Determinar si el usuario desea continuar o salir del programa
    continuar = input("\n¿Desea continuar? S/N: ")
    continuar = continuar.upper()
    
    if continuar == "S":
        isVerdadero = True
    elif continuar == "N":
        isVerdadero = False
    else:
        print("Debes seleccionar una entrada correcta. Saliendo...")
        isVerdadero = False
        break


#Imprimir el resumen de toda la información recolectada durante la ejecución del programa
print("\n", "--//--" * 15)
print("Total docentes:")
print(f"Docentes de la categoría A: {docentesCatA} docentes.")
print(f"Docentes de la categoría B: {docentesCatB} docentes.")
print(f"Docentes de la categoría C: {docentesCatC} docentes.")
print(f"TOTAL DOCENTES: {docentesCatA + docentesCatB + docentesCatC} docentes.")

print("\nValor total a pagar por todos los docentes:")
print(f"Pago total: ${valorTotalPagar:,.0f} COP")