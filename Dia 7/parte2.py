import valores
cangrejos=valores.valores.getValores()
better=9999999999999
for x in range(0,max(cangrejos)):
  gasolina=0
  for i in range(len(cangrejos)):
    if cangrejos[i]>x:
      gasolina+=sum(range((cangrejos[i]-x)+1))
    if cangrejos[i]<x:
      gasolina+=sum(range((x-cangrejos[i])+1))
  print("Orden "+str(x)+": "+str(gasolina))
  better= gasolina if gasolina<better else better
print("Mejor ruta: "+str(better))