import valores
peces=valores.valores.getValores()
print(peces)
diasReproducir=[0 for i in range(9)]

for i in range(len(peces)):
  diasReproducir[peces[i]] +=1
for dia in range(256):
  diaFertil=diasReproducir[0]
  for ciclo in range(8):
    diasReproducir[ciclo]=diasReproducir[ciclo+1]
  diasReproducir[6]+=diaFertil
  diasReproducir[8]=diaFertil
total=sum(diasReproducir)
print(total)