Bandera = 1
CodeVendedor = 0
TipoV = ""
Comision = 0

PorComision = 0
Ventasmes = 0
ComisionVentas = 0

ComisionTotal = 0
VentasTotales = 0

while True:
  try:
    Cc = int(input("Digite cedula: "))
    if(len(str(Cc))>13 or Cc<-1):
      print("Error cedula invalida / maximo 13 caracteres")
      continue
    break
  except Exception as e:
    print("Error, tipo de dato no valido", e)
    

while(Cc!=-1):

  while True:
    try:
      Nombre = input("Digite su nombre: ")
      Nombre.strip()
      if(Nombre == ""):
        print("Nombre no puede ser vacio")
        continue
      break
    except Exception as e:
      print("Error, tipo de dato no valido", e)

  while True:
    try:
      print("*" * 40 + "\n")
      print("Tipo de Vendedor")
      print("1. Puerta a puerta")
      print("2. Telemercadeo")
      print("3. Ejecutivo de ventas")
      print("*" * 40 + "\n")
    
      CodeVendedor = int(input("Digite el numero correspondiente al tipo de vendedor: "))
      if(CodeVendedor<1 or CodeVendedor>3):
        print("Valor no esta en el rango")
        continue
      break       
    except Exception as e:
      print("Error, tipo de dato no valido", e)




  while True:
    try:
        Ventasmes = float(input("Digite el valor de ventas en el mes: "))
        if(Ventasmes<0):
          print("Error Ventas no puede ser numero negativo")
          continue
        break
    except Exception as e:
      print("Error, tipo de dato no valido", e)

  

  
  if(CodeVendedor == 1 ):
    TipoV = "Puerta a puerta"
    Comision = 0.20
  elif(CodeVendedor == 2 ):
    TipoV = "Telemercadeo"
    Comision = 0.15
  elif(CodeVendedor == 3 ):
    TipoV = "Ejecutivo de Ventas"
    Comision = 0.25

  
  PorComision = Comision * Ventasmes
  ComisionVentas = Ventasmes + PorComision
  VentasTotales += Ventasmes
  ComisionTotal += PorComision
 
  print("*" * 40 + "\n")
  print(f"Cedula de Ciudadania: {Cc}")
  print(f"Nombre: {Nombre}")
  print(f"Tipo de Vendedor {TipoV}")
  print(f"Porcentaje Comision:  {Comision*100} % ")
  print(f" Valor venta mes: {Ventasmes:,.0f}")
  print(f"Valor de la comision: {PorComision}")
  print(f"Valor Total con comision vendedor: {ComisionVentas}" )
  print("\n")
  print("*" * 40 + "\n")


  while True:
    try:
      Cc = int(input("Desea Continuar // si: digite cedula //  no: -1 //"))
      if(Cc<-1 or len(str(Cc))>13):
        print("Error valor invalido")
        continue
      break
    except Exception as e:
      print("Error, tipo de dato no valido", e)

  

  

 
  if(Cc == -1):
    print("Vuelva pronto...")
   
  
print(f"Ventas Totales vendedores: {VentasTotales}")
print(f"Comision Total: {ComisionTotal} ")

