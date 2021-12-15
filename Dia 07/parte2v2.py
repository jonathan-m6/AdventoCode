import valores
def parte2(cangrejos):
  better=1e9
  gasolina=0
  for x in range(0,max(cangrejos)):
    gasolina=sum(sum(range(abs(cangrejo-x)+1)) for cangrejo in cangrejos)
    print("Orden "+str(x)+": "+str(gasolina))
    better= gasolina if gasolina<better else better
  print("Mejor ruta 1: "+str(better))

def parte1(cangrejos):
  better=1e9
  gasolina=0
  for x in range(0,max(cangrejos)):
    gasolina=sum(abs(cangrejo-x) for cangrejo in cangrejos)
    print("Orden "+str(x)+": "+str(gasolina))
    better= gasolina if gasolina<better else better
  print("Mejor ruta 2: "+str(better))
parte1(valores.valores.getPrueba())
parte2(valores.valores.getPrueba())