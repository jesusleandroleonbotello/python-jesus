
import json

fd = open("Christian Leonardo Celis Ardila/Persistencia _de_datos/archivos/lista.json","r")


lst = json.load(fd)

print("-"*30)
for e in lst:
    print(f"Nombre: {e['nombre']}")
    print(f"Edad: {e['edad']}")
    print("-"*30)
   
fd.close()
