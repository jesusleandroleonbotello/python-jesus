import random


def imprimirtabla(dictposiciones):
  cont = 0
  for k, v in dictposiciones.items():
    cont+=1
    print(v,k)
    if(cont == 10):
      return
  return


def ValidarNombre():
  while True:
    try:
        name =  input("Digite nombre? :")
        name = name.strip()
        if(name == ""):
          print("Nombre no puede ser vacio")
          continue
  
        return name
    except Exception as e:
      print("error nombre no valido",e)
  

def ValidarNumero(msg):
  while True:
    try:
        num =  int(input(msg))
        if(num<0 or num>1000):
          print("Numero fuera de rango")
          continue
  
        return num
    except Exception as e:
      print("error numero no valido",e)
      

def main():
  code = 0
  dictPosiciones = {}
  while True:
    generatenumber = random.randint(1,1000)
    print(generatenumber)
    print("Juego Adivina el numero")
    nombre = ValidarNombre()
    cont = 0
    for i in range(1,11):
      cont = i
      print(f"Intentos {i}/10")
      num = ValidarNumero("¿Dime un Numero?: ")
      if(num==generatenumber):
        print(f"Intentos {i}/10")
        print("Ganaste")
        dictPosiciones[nombre] = i
        break
      elif(num<generatenumber):
        print("No lo lograste, el número es mayor")
      else:
        print(" No lo lograste, el número es menor")
    
    if(cont==10):
      print("Game over")
    op = input("Desea Continuar? (S/N)") 
    op = op.lower()
    if(op=="n"):
      print("Adios")
      return
    code +=1
    dictPosiciones.clear
    dictPosiciones = dict(sorted(dictPosiciones.items(), key=lambda item: item[1]))
    imprimirtabla(dictPosiciones)

main()