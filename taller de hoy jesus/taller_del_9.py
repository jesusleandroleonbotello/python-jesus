# vamos hacer un juego 
# ingresar el nombre 

def nombre_jugadosr():
    while True:
        try:
            nom = input("Ingrese su nombre: ")
            nom = nom.strip()
            if len(nom) == 0 or not nom.isalnum():
                if nom.isdigit(): # esto es para que el nombre no sean solo numeros 
                    print("Nombre inválido")
                continue
            return nom
        except Exception as e:
            print("Error al ingresar el nombre.", e)

rol = {}
name = nombre_jugadosr()

rol["nombre"] = (nombre_jugadosr)

print(rol)