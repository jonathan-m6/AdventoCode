from numpy.core.fromnumeric import size
import valores
import numpy as np
entrada=valores.getValores()
doblaje=valores.getDoblaje()
xLong,yLong=-1,-1

for val in entrada:
  xLong= val[0] if val[0]>xLong else xLong
  yLong= val[1] if val[1]>yLong else yLong
papel=[["." for x in range(1311)] for y in range(895)] 

for val in entrada:
  papel[val[1]][val[0]]="#"
for do in doblaje:
  t=[clave for clave in do.keys()]
  if(t[0]=="y"):
    top,bottom=[],[]
    for ind in range(do["y"]):
      top.append(papel[ind])
      bottom.append(papel[do["y"]+(ind+1)])
    bottom=bottom[::-1]
    arra=np.array(bottom)
    ls=np.where(arra == "#")
    for val in range(len(ls[0])):
      top[ls[0][val]][ls[1][val]]="#"
    top=np.array(top)
    con=np.where(top == "#")
    print(con[0].size)
    papel=top
  elif(t[0]=="x"):
    right,left=np.array([["." for x in range(do["x"])] for y in range(len(papel))]),np.array([["." for x in range(do["x"])] for y in range(len(papel))])
    for y in range(len(papel)):
      for x in range(do["x"]):
        left[y][x]=papel[y][x]
        right[y][x]=papel[y][do["x"]+(x+1)]
    right=np.flip(right, axis=1)
    ls=np.where(right == "#")
    for val in range(len(ls[0])):
      left[ls[0][val]][ls[1][val]]="#"
    conteo=0
    left=np.array(left)
    ls=np.where(left == "#")
    print(ls[0].size)
    papel=left
for linea in papel:
  print("".join(linea))
