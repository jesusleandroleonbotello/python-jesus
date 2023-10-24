# Calculadora del valor de nómina, bajo parámetros personalizados
# como precio hora y descuentos.


# DEFINIENDO LAS VARIABLES PRINCIPALES
valorHora = 20000
cantidadHoras = int(input("\n¿Cuántas horas has trabajado?: "))
descuentoEPS = 4
descuentoPension = 4


# CALCULANDO EL VALOR DEL SUELDO BRUTO
sueldoBruto = valorHora * cantidadHoras


# CALCULANDO EL VALOR DEL SUELDO NETO
valorDescuentoEPS = (sueldoBruto * descuentoEPS) // 100
sueldoNeto = sueldoBruto - valorDescuentoEPS

valorDescuentoPension = (sueldoBruto * descuentoPension) // 100
sueldoNeto -= valorDescuentoPension


# IMPRIMIENDO LOS VALORES CORRESPONDIENTES EN PANTALLA
print("\n", "=" * 35)
print(f"El valor del sueldo bruto es de: ${sueldoBruto:,.0f}.")
print(f"El valor del sueldo neto es de: ${sueldoNeto:,.0f}.")