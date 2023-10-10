# dos listas una con nobres y otra con apellidos
nombres =["juan", "mateo","samuel", "gloria", "jose"]
apellidos =["robert", "gonzales", "leon", "sore", "castro"]

# registrar esta informacion en un txt de forma optima
with open ("/home/Exegol-164/Documents/git jesus/python-jesus/archivos/nombres_yapellidos.txt","w") as nombresyp:
    nombresyp.writelines("los datos son: \n\n")
    [nombresyp.writelines(f"nombre: {n}\napellidos: {a}\n------------------\n") for n,a in zip(nombres,apellidos)]