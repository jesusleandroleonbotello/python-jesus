nota = int(input("Digite la nota de 0 a 100: "))
nombre = input("Digite su nombre: ")

if(nota>=0 and nota <=59):
    Calificacion = "D"
elif(nota>59 and nota <=79):
    Calificacion = "C"
elif(nota>79 and nota <=89):
    Calificacion = "B"
elif(nota>89 and nota <=100):
    Calificacion = "A"
else:
    Calificacion = ' '
    print("Nota Invalida")


print(nombre)

print("NOTA CUANTITATIVA: ", nota)
print("NOTA CUALITATIVA: ", Calificacion)
