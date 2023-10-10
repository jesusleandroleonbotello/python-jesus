#import pandas as pd # la sigla de pandas normlamente siempre la ponen como pd

# toca instalar pip y el modulo de pandas
# en la cmd toca intalar pip con un codigo y despues pandas
# sudo apt-get install python3-pip  esta para linux
# py -m pip install pandas  para instalar pandas

# # # import pandas as pd:
# # df = pd.read_csv("/home/Exegol-164/Documents/git jesus/python-jesus/archivos/datos.csv")
# print(df) # df = a data frame

# nombres = (df["nombre"])   # nos muestra todos los datos de la columna nombre

# para usarla con jupyter notebook
# seria (control+shift+p)
# una forma optima de trabajr con ciencia de datos
# nos siver para agendar datos es como un tipo de ia pero bueno
#tambien nos muestra cuanto se tarda en ejecutar un programa

# ordenando el data frame por la edad
# df_ordenado = df.sort_values("edad")

# organizandolo de forma descendente
# df_ordenado-desendente = df.sort_values("edad",ascending=False)

# concatenando dos data frame
# df_concatenado = pd.concat([df,df2])

# accediendo alas primeras # filas con head()
# primer_fila = df.head()   # aqui se coloca parametros para mostrar ya sea el encabezado o unas filas y el encabezado
# accediendo a las ultimas filas con tail()
# ultimas_filas = df.tail()

#accediendo a la cantidad de filas y columnas con shape
# filas_Y_columnas_totales = df.shape

# obteniendo datos estadisticos del data frame
# df_info = df.describe()

# accediendo a un elemento e especifico con loc
# elemento-especifico_loc = df.loc[2,"edad"]

# accediendo a un elemento e especifico con iloc
# elemento-especifico_iloc = df.iloc[2,2

# accediendo a todas las filas de una columna
# apellidos = df.iloc[:,1]

# accediendo a una flia con loc # con iloc seria igual
# flia_3 = df.loc[2,:]

# accediendo alas filas con mayor edad que 30
# mayor_edad = df.loc[df["edad"]>30,:]