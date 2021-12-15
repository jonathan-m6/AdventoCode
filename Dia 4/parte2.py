from typing import Tuple
import valores
import numpy as np
tablas=valores.valores.getMatrices(False)
fichas=valores.valores.getValores(False)
winX,winY=-1,-1
theLast,tablaWin=0,[]
ganadores=[{"x":[0 for i in range(5)],"y":[0 for i in range(5)]} for n in range(len(tablas))]
finded=[[] for n in range(len(tablas))]
def existe(y,x):
  for find in finded[tablaWin[len(tablaWin)-1]]:
    if y==find[0] and x==find[1]:
      return True
  return False

def bingo():
  global theLast,winX,winY,tablaWin,finded
  for f in fichas:
    for i in range(len(tablas)):
      for linea in range(len(tablas[i])):
        for item in range(len(tablas[i][linea])):
          num=tablas[i][linea][item]
          if num==f:
            finded[i].append([linea,item])
            ganadores[i]["y"][linea]+=1
            ganadores[i]["x"][item]+=1
      for j in range(len(ganadores)):
        for eje in range(5):
          y,x=ganadores[j]["y"],ganadores[j]["x"]
          """ if y[eje]==5 or x[eje]==5 and len(tablas)>0:
            tablas.pop(i)
            ganadores.pop(i) """
          if y[eje]==5 or x[eje]==5:
            print("break")
          if y[eje]==5 and (j in tablaWin)!=True:
            """ orientacion="y"
            numOrienta=eje """
            theLast=f
            tablaWin.append(i)
          elif x[eje]==5 and (j in tablaWin)!=True:
            """ orientacion="x"
            numOrienta=eje """
            theLast=f
            tablaWin.append(i)
          if len(tablaWin)==len(tablas):
            return
bingo()
suma,ganadora=0,tablas[tablaWin[len(tablaWin)-1]]
for filas in range(len(ganadora)):
  for col in range(len(ganadora[filas])):
    if existe(filas,col)==False:
      suma+=ganadora[filas][col]
print(suma*theLast)
