import valores
binarios=valores.valores.getBinarios()
def procesar():
  gamma=""
  epsilon=""
  for i in range(12):
    contador1=0
    contador0=0
    for index in range(len(binarios)):
      bit=binarios[index][i]
      if bit=="0":
        contador0+=1
      if bit=="1":
        contador1+=1
    if contador1>contador0:
      gamma+="1"
    else:
      gamma+="0"
  for bit in gamma:
    if bit=="0":
      epsilon+="1"
    if bit=="1":
      epsilon+="0"
  deciGama=0
  deciEpsi=0
  intGama=int(gamma)
  intEpsilon=int(epsilon)
  i=0
  while (intGama>0):
    digito  = intGama%10
    intGama = int(intGama//10)
    deciGama = deciGama+digito*(2**i)
    i = i+1
  j=0
  while (intEpsilon>0):
    digito  = intEpsilon%10
    intEpsilon = int(intEpsilon//10)
    deciEpsi = deciEpsi+digito*(2**j)
    j = j+1
  print(deciEpsi)
  print(deciGama*deciEpsi)
if __name__ == "__main__":
  procesar()