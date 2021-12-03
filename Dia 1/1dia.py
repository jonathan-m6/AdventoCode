import valores1dia
def procesar():
  mayor=0
  deep=valores1dia.valores.getDeep()
  for index in range(len(deep)):
    if index>0:
      if deep[index-1]<deep[index]:
        mayor+=1
if __name__ == "__main__":
  procesar()