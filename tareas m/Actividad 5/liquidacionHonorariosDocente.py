# Este programa obtiene el valor de la liquidación de honorarios para el Docente.


# ESTABLECIENDO LAS VARIABLES PRINCIPALES
isVerdadero = True
docentesCategoriaA = 0
docentesCategoriaB = 0
docentesCategoriaC = 0
pagaDocenteTotal = 0

while isVerdadero:
    documentoIdentidad = int(input("Ingrese el documento de identidad: "))
    nombre = input("Ingrese el nombre del docente: ")
    categoriaDocente = input("Ingrese la categoría del docente (A, B o C): ")
    horasLaboralesMes = int(input("Ingrese las horas laborales del mes realizadas por el docente: "))

    if categoriaDocente == "A" or "a":
        valorHora = 25000

        pagaDocente = horasLaboralesMes * valorHora
        pagaDocenteTotal += pagaDocente

        docentesCategoriaA += 1

    elif categoriaDocente == "B" or "b":
        valorHora = 35000

        pagaDocente = horasLaboralesMes * valorHora
        pagaDocenteTotal += pagaDocente

        docentesCategoriaB += 1

    elif categoriaDocente == "C" or "c":
        valorHora = 50000

        pagaDocente = horasLaboralesMes * valorHora
        pagaDocenteTotal += pagaDocente

        docentesCategoriaC += 1

    else:
        print("Ingrese un valor de categoria válido. Saliendo...")
        break

    
    print("\n", "=" * 35)
    print(f"Docente: {nombre}")
    print(f"Identidad: {documentoIdentidad}")
    print(f"Categoría: {categoriaDocente}")
    print(f"Horas laboradas: {horasLaboralesMes:,.0f}")
    print(f"El valor a pagar es: {pagaDocente:,.0f}")

    
    continuar = input("¿Desea continuar? S/N: ")

    if continuar == "S" or continuar == "s":
        isVerdadero = True
    elif continuar == "N" or continuar == "n":
        isVerdadero = False
    else:
        print("Ingrese una entrada válida. Saliendo...")
        break


print("\n", "=" * 35)
print(f"Valor total a pagar a los docentes: {pagaDocenteTotal}")
print(f"Cantidad docentes categoría A: {docentesCategoriaA}")
print(f"Cantidad docentes categoría B: {docentesCategoriaB}")
print(f"Cantidad docentes categoría C: {docentesCategoriaC}")