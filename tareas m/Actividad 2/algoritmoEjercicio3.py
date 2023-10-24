# La empresa ACME desea calcular el valor de la nómina de un empleado, tanto el sueldo bruto como el
# sueldo neto. El sueldo bruto se calcula a partir del valor de la hora y la cantidad de horas trabajadas. A
# esto se le descuenta el valor de la EPS que es el 4%, el valor de la Pensión que es el 4%. El sueldo neto
# es el sueldo bruto menos los descuentos. Mostrar al final, el valor del sueldo bruto, cada uno de los
# descuentos y el valor del sueldo Neto. Para este ejercicio el valor de la hora es $20.000.


# SUELDO BRUTO
valorHora = 20000
cantidadHoras = int(input("Introduzca la cantidad de horas trabajadas: "))

descuentos = (((valorHora * cantidadHoras) * 4) / 100) * 2

sueldoBrutoTotal = (valorHora * cantidadHoras) - descuentos
print("Su saldo bruto total es de ${:,.1f}".format(sueldoBrutoTotal))


# SUELDO NETO
sueldoNeto = sueldoBrutoTotal - descuentos
print("Su saldo neto total es de ${:,.1f}".format(sueldoNeto))