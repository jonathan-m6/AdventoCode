import valores1dia
mayor=0
deep=valores1dia.valores.getDeep()
valoresSum=[]
def procesar():
  global mayor
  for index in range(len(deep)):
    a=deep[index]+deep[index+1]+deep[index+2]
    valoresSum.append(a)
    if index+2==len(deep)-1:
      break
  for index in range(len(valoresSum)):
    if index>0:
      if valoresSum[index-1]<valoresSum[index]:
        mayor+=1
  print(mayor)
  print(valoresSum[len(valoresSum)-1])
if __name__ == "__main__":
  procesar()