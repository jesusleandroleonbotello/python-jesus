# with open("/home/Exegol-164/Documents/git jesus/python-jesus/archivos/datos.csv") as archivo:
    # print(archivo.read())
# para leer sin estar listado


import csv
# nos muestra lo que haya en el archivo csv
with open("/home/Exegol-164/Documents/git jesus/python-jesus/archivos/datos.csv") as archivo:
    reader = csv.reader(archivo)
    for row in reader:
        print(row)
# nos muestras listas con las filas

