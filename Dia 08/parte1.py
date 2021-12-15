digitos=[0,0,0,0,0,0,0,0,0]
with open("Dia 8/lodo.txt","r") as archivo:
    for linea in archivo:
      salida=str(linea.strip().split("|")[1]).split(" ")
      for dig in salida:
        digitos[len(dig)]+=1

print (digitos[2]+digitos[4]+digitos[3]+digitos[7])