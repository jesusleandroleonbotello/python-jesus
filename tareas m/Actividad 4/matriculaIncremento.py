# Supongamos que la matrícula de una universidad es de 10.000 dólares este año
# y aumenta un 7% cada año. ¿En cuántos años se habrá duplicado la matrícula?



# DEFINIENDO LAS VARIABLES PRINCIPALES.
matricula = 10000
matriculaDoble = matricula * 2
aumentoMatricula = 7
cantidadAumentoMatricula = (matricula * aumentoMatricula) / 100 # Error aquí: El porcentaje no es constante.
year = 0


# DETERMINAR LOS AÑOS 
for i in range(1, 500):
    if matricula >= matriculaDoble:
        print(f"Han tenido que pasar {i:.0f} años para que la matricula pase a valer el doble de {matricula:,.0f}.")
        #Faltó formatear la salida :(
        break

    matricula += (matricula * aumentoMatricula) / 100 
    year += 1