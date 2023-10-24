Sueldo = 1_100_000
SueldoMin = 1_160_000

if Sueldo<=SueldoMin:
    auxTrans = 140_000
else:
    auxTrans = 0

print("Auxilio de transporte: ${:,.0f}".format(auxTrans))
