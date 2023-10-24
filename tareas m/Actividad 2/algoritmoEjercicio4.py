# ALgoritmo para calcular la cantidad de segundos, minutos y horas a partir de los segundos.

segundosUsuario = int(input("Ingrese los segundos: "))

hora = segundosUsuario // (60 * 60)
minutos = (segundosUsuario % (60 * 60)) // 60
segundos = (segundosUsuario % 60)

print("Horas: {:,.0f}".format(hora))
print("Minutos: {:,.0f}".format(minutos))
print("Segundos: {:,.0f}".format(segundos))