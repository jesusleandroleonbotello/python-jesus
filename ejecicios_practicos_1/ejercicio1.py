#ejercicio
# a) diferencia en porcentaje entre el curso actual y:
#el mas rapido de los cursos 
#el mas lento de los otros cursos
#el promedio de los cursos
# b) porcentaje de material inservible que se reduce en:
#el promedio de los cursos
#el curso actual
# c) ver 10 horas de este curso a cuantas de otros equivale
# y alreves

# promedios de duraciones 

otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
dalto_curso = 1.5

#duracion de crudos

crudo_promedio = 5
crudo_dalto = 3.5

# diferencia de duracion

diferencia_min = 100 - dalto_curso / otros_cursos_min * 100
diferencia_max = 100 - dalto_curso * 1000 // otros_cursos_max / 10
diferencia_promedio = 100 - dalto_curso / otros_cursos_promedio * 100

#calculando el porcentaje de tiempo vacio removido

tiempo_vacio_promedio = 100 - otros_cursos_promedio * 1000 // crudo_promedio / 10
tiempo_vacio_dalto = 100 - dalto_curso * 1000 // crudo_dalto / 10

#mostrando las diferncias de duracion (punto A)
print("El curso de dalto dura: ")
print(f"un: {diferencia_min}% menos que el mas rapido")
print(f"un: {diferencia_max}% menos que el mas lento")
print(f"un: {diferencia_promedio}% menos que el promedio")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#mostrando la cantidad de espacios vacios que se remueven (punto B)

print(f"Un curso promedio elimina un {tiempo_vacio_promedio}% de tiempo vacio")
print(f"el curso de dalto elimina un {tiempo_vacio_dalto}% de tiempo vacio")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
#mostrando diferencia si los cursos duran 10 horas

print(f"ver 10 horas de este curso equivale a ver {otros_cursos_promedio * 100 // dalto_curso / 10} horas de otros cursos")
print(f"ver 10 horas de otros cursos equivale a ver {dalto_curso * 100 // otros_cursos_promedio / 10} horas de este curso")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
