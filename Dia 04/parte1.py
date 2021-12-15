import valores
import numpy as np
tablas=valores.valores.getMatrices(False)
fichas=valores.valores.getValores(False)
#ganadores=[{"x":{"0":0,"1":0,"2":0,"3":0,"4":0,"5":0},"y":{"0":0,"1":0,"2":0,"3":0,"4":0,"5":0}} for n in range(len(tablas))]
winX,winY=-1,-1
theLast,tablaWin=0,-1
ganadores=[{"x":[0 for i in range(5)],"y":[0 for i in range(5)]} for n in range(len(tablas))]
finded=[[] for n in range(len(tablas))]
def existe(y,x):
  for find in finded[tablaWin]:
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
        y,x=ganadores[j]["y"],ganadores[j]["x"]
        for eje in range(5):
          theLast=f
          tablaWin=i
          if y[eje]==5:
            winY=eje
            return
          elif x[eje]==5:
            winX=eje
            return
bingo()
suma,ganadora=0,tablas[tablaWin]
for filas in range(len(ganadora)):
  for col in range(len(ganadora[filas])):
    if existe(filas,col)==False:
      suma+=ganadora[filas][col]
print(suma*theLast)
