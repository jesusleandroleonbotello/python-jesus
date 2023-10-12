df = open("lectura archivo/nombres.txt","r")

df2 = open("lectura archivo/nombres_bak.txt","w")

for linea in df:
    df2.write(linea)

df2.close()
df.close()

print("proceso terminado")

