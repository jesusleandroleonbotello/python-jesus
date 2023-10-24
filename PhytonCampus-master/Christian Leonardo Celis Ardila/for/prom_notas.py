
# capturar y Calcular el promedio de las notas de un curso
#mostrar en pantalla el resultado.

num = int(input("Digite numero de notas: "))
sum = 0;

for i in range(1, num + 1):
    nota = float(input("ingrese la nota: " + str(i) + ": "))
    sum += nota

prom = sum/num
print(prom)