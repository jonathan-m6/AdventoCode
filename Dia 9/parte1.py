import valoress
tabla= valoress.getValore()
suma=0

lineaX=len(tabla[0])-1
lineaY=len(tabla)-1
for i in range(len(tabla)):
  for x in range(len(tabla[i])):
    try:
      numT=int(tabla[i-1][x])
      numL=int(tabla[i][x-1])
      numR=int(tabla[i][x+1])
      numB=int(tabla[i+1][x])
    except:
      print("")
    num=int(tabla[i][x])
    if i==0 and x==0:
      """ numR=int(tabla[i][x+1])
      numB=int(tabla[i+1][x]) """
      if(num<min(numR,numB)):
        suma+=num+1
    elif i==lineaY and x==lineaX:
      """ numT=int(tabla[i-1][x])
      numL=int(tabla[i][x-1]) """
      if(num<min(numT,numL)):
        suma+=num+1
    elif i==0 and x==lineaX:
      """ numB=int(tabla[i+1][x])
      numL=int(tabla[i][x-1]) """
      if(num<min(numB,numL)):
        suma+=num+1
    elif i==lineaY and x==0:
      """ numT=int(tabla[i-1][x])
      numR=int(tabla[i][x-1]) """
      if(num<min(numT,numR)):
        suma+=num+1
    elif i==0:
      """ numR=int(tabla[i][x+1])
      numB=int(tabla[i+1][x])
      numL=int(tabla[i][x-1]) """
      if(num<min(numR ,numB ,numL)):
        suma+=num+1
    elif x==0:
      """ numR=int(tabla[i][x+1])
      numB=int(tabla[i+1][x])
      numT=int(tabla[i-1][x]) """
      if(num<min(numR ,numB ,numT)):
        suma+=num+1
    elif i==lineaY:
      """ numT=int(tabla[i-1][x])
      numL=int(tabla[i][x-1])
      numR=int(tabla[i][x+1]) """
      if(num<min(numR,numT,numL)):
        suma+=num+1
    elif x==lineaX:
      """ numL=int(tabla[i][x-1])
      numB=int(tabla[i+1][x])
      numT=int(tabla[i-1][x]) """
      if(num<min(numR,numB,numT)):
        suma+=num+1
    else:
      """ numT=int(tabla[i-1][x])
      numL=int(tabla[i][x-1])
      numR=int(tabla[i][x+1])
      numB=int(tabla[i+1][x]) """
      if(num<min(numB,numT,numL,numR)):
        suma+=num+1
print(suma)
