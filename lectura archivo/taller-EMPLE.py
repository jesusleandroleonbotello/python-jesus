fd = open("lectura archivo/datos_empleados.dat",'r')

for linea in fd:
    if not linea.startswith("id"):
        datos = linea.split(",")
        print(f"id:{datos[0]}\nnombre:{datos[1]}\nedad:{datos[2]}\nsexo:{datos[3]}\ntelefono:{datos[4].strip()}")
        print("*" * 30)

fd.close()