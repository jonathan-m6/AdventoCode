import valoress
tabla= valoress.getValore()
lavabos,listaNegra=[],[]
lineaX=len(tabla[0])-1
lineaY=len(tabla)-1
contador=0
def existListaNegra(find):
  for lis in listaNegra:
    if "".join(str(lis))=="".join(str(find)):
      return True
  return False
def ruta(i,x):
  global contador
  num=int(tabla[i][x])
  if i==0 and x==0:
    numR=int(tabla[i][x+1])
    numB=int(tabla[i+1][x])
    if existListaNegra([i,x+1])==False and numR!=9:
      if numR-num==1:
        listaNegra.append([i,x+1])
        contador+=1
        ruta(i,x+1)
    if existListaNegra([i+1,x])==False and numB!=9:
      if numB-num==1:
        listaNegra.append([i+1,x])
        contador+=1
        ruta(i+1,x)
  elif i==lineaY and x==lineaX:
    numT=int(tabla[i-1][x])
    numL=int(tabla[i][x-1])
    if existListaNegra([i-1,x])==False and numT!=9:
      if numT-num==1:
        listaNegra.append([i-1,x])
        contador+=1
        ruta(i-1,x)
    if existListaNegra([i,x-1])==False and numL!=9:
      if numL-num==1:
        listaNegra.append([i,x-1])
        contador+=1
        ruta(i,x-1)
  elif i==0 and x==lineaX:
    numB=int(tabla[i+1][x])
    numL=int(tabla[i][x-1])
    if existListaNegra([i+1,x])==False and numB!=9:
      if numB-num==1:
        listaNegra.append([i+1,x])
        contador+=1
        ruta(i+1,x)
    if existListaNegra([i,x-1])==False and numL!=9:
      if numL-num==1:
        listaNegra.append([i,x-1])
        contador+=1
        ruta(i,x-1)
  elif i==lineaY and x==0:
    numT=int(tabla[i-1][x])
    numR=int(tabla[i][x-1])
    if existListaNegra([i-1,x])==False and numT!=9:
      if numT-num==1:
        listaNegra.append([i-1,x])
        contador+=1
        ruta(i-1,x)
    if existListaNegra([i,x-1])==False and numR!=9:
      if numR-num==1:
        listaNegra.append([i,x-1])
        contador+=1
        ruta(i,x-1)
  elif i==0:
    numR=int(tabla[i][x+1])
    numB=int(tabla[i+1][x])
    numL=int(tabla[i][x-1])
    if existListaNegra([i,x+1])==False and numR!=9:
      if numR-num==1:
        listaNegra.append([i,x+1])
        contador+=1
        ruta(i,x+1)
    if existListaNegra([i+1,x])==False and numB!=9:
      if numB-num==1:
        listaNegra.append([i+1,x])
        contador+=1
        ruta(i+1,x)
    if existListaNegra([i,x-1])==False and numL!=9:
      if numL-num==1:
        listaNegra.append([i,x-1])
        contador+=1
        ruta(i,x-1)
  elif x==0:
    numR=int(tabla[i][x+1])
    numB=int(tabla[i+1][x])
    numT=int(tabla[i-1][x])
    if existListaNegra([i,x+1])==False and numR!=9:
      if numR-num==1:
        listaNegra.append([i,x+1])
        contador+=1
        ruta(i,x+1)
    if existListaNegra([i+1,x])==False and numB!=9:
      if numB-num==1:
        listaNegra.append([i+1,x])
        contador+=1
        ruta(i+1,x)
    if existListaNegra([i-1,x])==False and numT!=9:
      if numT-num==1:
        listaNegra.append([i-1,x])
        contador+=1
        ruta(i-1,x)
  elif i==lineaY:
    numT=int(tabla[i-1][x])
    numL=int(tabla[i][x-1])
    numR=int(tabla[i][x+1])
    if existListaNegra([i-1,x])==False and numT!=9:
      if numT-num==1:
        listaNegra.append([i-1,x])
        contador+=1
        ruta(i-1,x)
    if existListaNegra([i,x-1])==False and numL!=9:
      if numL-num==1:
        listaNegra.append([i,x-1])
        contador+=1
        ruta(i,x-1)
    if existListaNegra([i,x+1])==False and numR!=9:
      if numR-num==1:
        listaNegra.append([i,x+1])
        contador+=1
        ruta(i,x+1)
  elif x==lineaX:
    numL=int(tabla[i][x-1])
    numB=int(tabla[i+1][x])
    numT=int(tabla[i-1][x])
    if existListaNegra([i,x-1])==False and numL!=9:
      if numL-num==1:
        listaNegra.append([i,x-1])
        contador+=1
        ruta(i,x-1)
    if existListaNegra([i+1,x])==False and numB!=9:
      if numB-num==1:
        listaNegra.append([i+1,x])
        contador+=1
        ruta(i+1,x)
    if existListaNegra([i-1,x])==False and numT!=9:
      if numT-num==1:
        listaNegra.append([i,x])
        contador+=1
        ruta(i-1,x)
  else:
    numT=int(tabla[i-1][x])
    numL=int(tabla[i][x-1])
    numR=int(tabla[i][x+1])
    numB=int(tabla[i+1][x])
    if existListaNegra([i-1,x])==False and numT!=9:
      if numT-num==1:
        listaNegra.append([i-1,x])
        contador+=1
        ruta(i-1,x)
    if existListaNegra([i,x-1])==False and numL!=9:
      if numL-num==1:
        listaNegra.append([i,x-1])
        contador+=1
        ruta(i,x-1)
    if existListaNegra([i,x+1])==False and numR!=9:
      if numR-num==1:
        listaNegra.append([i,x+1])
        contador+=1
        ruta(i,x+1)
    if existListaNegra([i+1,x])==False and numB!=9:
      if numB-num==1:
        listaNegra.append([i+1,x])
        contador+=1
        ruta(i+1,x)

for i in range(len(tabla)):
  for x in range(len(tabla[i])):
    num=int(tabla[i][x])
    if i==0 and x==0:
      numR=int(tabla[i][x+1])
      numB=int(tabla[i+1][x])
      if(num<min(numR,numB)):
        listaNegra.append([i,x])
        contador=1
        ruta(i,x)
        lavabos.append(contador)
    elif i==lineaY and x==lineaX:
      numT=int(tabla[i-1][x])
      numL=int(tabla[i][x-1])
      if(num<min(numT,numL)):
        listaNegra.append([i,x])
        contador=1
        ruta(i,x)
        lavabos.append(contador)
    elif i==0 and x==lineaX:
      numB=int(tabla[i+1][x])
      numL=int(tabla[i][x-1])
      if(num<min(numB,numL)):
        listaNegra.append([i,x])
        contador=1
        ruta(i,x)
        lavabos.append(contador)
    elif i==lineaY and x==0:
      numT=int(tabla[i-1][x])
      numR=int(tabla[i][x-1])
      if(num<min(numT,numR)):
        listaNegra.append([i,x])
        contador=1
        ruta(i,x)
        lavabos.append(contador)
    elif i==0:
      numR=int(tabla[i][x+1])
      numB=int(tabla[i+1][x])
      numL=int(tabla[i][x-1])
      if(num<min(numR ,numB ,numL)):
        contador=1
        listaNegra.append([i,x])
        ruta(i,x)
        lavabos.append(contador)
    elif x==0:
      numR=int(tabla[i][x+1])
      numB=int(tabla[i+1][x])
      numT=int(tabla[i-1][x])
      if(num<min(numR ,numB ,numT)):
        listaNegra.append([i,x])
        contador=1
        ruta(i,x)
        lavabos.append(contador)
    elif i==lineaY:
      numT=int(tabla[i-1][x])
      numL=int(tabla[i][x-1])
      numR=int(tabla[i][x+1])
      if(num<min(numR,numT,numL)):
        listaNegra.append([i,x])
        contador=1
        ruta(i,x)
        lavabos.append(contador)
    elif x==lineaX:
      numL=int(tabla[i][x-1])
      numB=int(tabla[i+1][x])
      numT=int(tabla[i-1][x])
      if(num<min(numL,numB,numT)):
        listaNegra.append([i,x])
        contador=1
        ruta(i,x)
        lavabos.append(contador)
    else:
      numT=int(tabla[i-1][x])
      numL=int(tabla[i][x-1])
      numR=int(tabla[i][x+1])
      numB=int(tabla[i+1][x])
      if(num<min(numB,numT,numL,numR)):
        listaNegra.append([i,x])
        contador=1
        ruta(i,x)
        lavabos.append(contador)
lavabos.sort(reverse=True)
print(lavabos)
print(lavabos[0]*lavabos[1]*lavabos[2])
