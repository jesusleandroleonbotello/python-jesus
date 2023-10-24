# Este programa permite conocer la cantidad de términos según una serie matemática.

# DEFINIENDO LAS VARIABLES PRINCIPALES
suma = 0


# DEFINIENDO LAS FUNCIONES ESCENCIALES
def serieArmonicaAlterna(msj):
    signo = -1
    
    while True:
        try:
            n = int(input(msj))
            
            if n == 0:
                return 0
            elif n < 1:
                print("Error: No puedes introducir números negativos.")
                continue
            break
            
        except ValueError:
            print("Ha ocurrido un error al ingresar el número. Inténtelo de nuevo.")
        except:
            print("Ha ocurrido un error inesperado. Inténtelo de nuevo o comuníquese con un administrador.")
    
    
    # Aquí va el cálculo de la serie armónica alterna.        
    


# CREANDO LA ESTRUCTURA DEL PROGRAMA
resultadoSAA = serieArmonicaAlterna()