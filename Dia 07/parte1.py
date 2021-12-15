import valores
cangrejos=valores.valores.getValores()
better=1e9
for x in range(0,max(cangrejos)):
  gasolina=0
  for i in range(len(cangrejos)):
    gasolina+=abs(cangrejos[i]-x)
  print(gasolina)
  better= gasolina if gasolina<better else better
print("Mejor ruta: "+str(better))