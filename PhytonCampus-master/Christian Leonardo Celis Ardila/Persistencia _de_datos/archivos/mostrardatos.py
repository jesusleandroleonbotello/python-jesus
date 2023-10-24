
archivo = open("Christian Leonardo Celis Ardila/Persistencia _de_datos/archivos/datosempleados.dat","r")



list = []

for linea in archivo:
    list.append(linea.split(","))
    archivo.close()
    
print()
print("--------EMPLEADOS EMPRESA ACME--------")
for i in range(len(list)):
    if(i!=0):
        print("\n"+"="*35)
        print(f"\n\nEMPLEADO {i}")
        print(f"ID: {list[i][0]}")
        print(f"NOMBRE: {list[i][1]}")
        print(f"EDAD: {list[i][2]}")
        print(f"SEXO: {list[i][3]}")
        print(f"TELEFONO: {list[i][4]}")