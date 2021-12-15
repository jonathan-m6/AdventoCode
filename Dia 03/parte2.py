import valores
binarios=valores.valores.getBinarios()
binarios2=valores.valores.getBinarios()
def getDecimal(binario):
  i=0
  decimal=0
  while (binario>0):
    digito  = binario%10
    binario = int(binario//10)
    decimal = decimal+digito*(2**i)
    i = i+1
  return decimal
def procesar():
  for i in range(12):
    contador1=0
    contador0=0
    for index in range(len(binarios)):
      bit=binarios[index][i]
      if bit=="0":
        contador0+=1
      if bit=="1":
        contador1+=1
    if contador1>=contador0:
      ind=0
      while (ind<len(binarios)):
        if binarios[ind][i]=="0":
          binarios.pop(ind)
          ind=0
        else:
          ind+=1
    else:
      ind=0
      while (ind<len(binarios)):
        if binarios[ind][i]=="1":
          binarios.pop(ind)
          ind=0
        else:
          ind+=1
  for i in range(12):
    cont1=0
    cont0=0
    for index in range(len(binarios2)):
      bit=binarios2[index][i]
      if bit=="0":
        cont0+=1
      if bit=="1":
        cont1+=1
    if len(binarios2)==1:
      break
    if cont1<cont0:
      ind=0
      while (ind<len(binarios2)):
        if binarios2[ind][i]=="0":
          binarios2.pop(ind)
          ind=0
        else:
          ind+=1
    else:
      ind=0
      while (ind<len(binarios2)):
        if binarios2[ind][i]=="1":
          binarios2.pop(ind)
          ind=0
        else:
          ind+=1
  print(getDecimal(int(binarios2[0])))
  print(getDecimal(int(binarios[0])))
  print(getDecimal(int(binarios[0]))*getDecimal(int(binarios2[0])))
if __name__ == "__main__":
  procesar()