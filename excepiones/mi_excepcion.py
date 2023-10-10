# creando mi propia excepcion personalizada

class MiExcepcion(Exception):
    def __init__(self,err):
        print(f"inpresionante cometiste este error :{err}")


# lanzando mi propia excepcion
raise MiExcepcion("esta mal bro")

# manejandola
try:
    raise MiExcepcion("esta mal bro")
except:
    print("como lo vas a hacer")