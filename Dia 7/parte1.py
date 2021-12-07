import valores
cangrejos=valores.valores.getValores()
better=9999999999999
for x in range(0,max(cangrejos)):
  gasolina=0
  for i in range(len(cangrejos)):
    if cangrejos[i]>x:
      gasolina+=cangrejos[i]-x
    if cangrejos[i]<x:
      gasolina+=x-cangrejos[i]
  print(gasolina)
  better= gasolina if gasolina<better else better
print("Mejor ruta: "+str(better))