
def leernombre(msg):
    while True:
        try:
            Nombre = input(msg)
            Nombre.strip()
            if(Nombre==""):
                print("Nombre del archivo no puede ser vacio")
                continue
            return Nombre
        except Exception as e:
            print("\nError al ingresar el nombre\n", e)

def main():
    NombreArchivo = leernombre("Digite nombre Archivo: ")
    ContenidoSpam = []
    try:
        Fd = open("Tests/"+NombreArchivo,"r")
    except Exception as e:
        print("no se puede leer el archivo",e)
        return
    
    for linea in Fd:
        if(linea.startswith("X-DSPAM-Confidence:")):
            ContenidoSpam.append(float(linea.split()[1]))

    if(ContenidoSpam==""):
        print("No hay contenido en archivo")
        Fd.close()
        return
    else:
        Fd.close()
        Suma = 0
        for i in ContenidoSpam:
            Suma += i
            try:
                Promedio = Suma/ len(ContenidoSpam)
            except Exception as e:
                print("Division por cero",e)
                return
        print(f"Average spam confidence: {Promedio:,.3f}")
        return
main()