import valores
peces=valores.valores.getValores()
dia=0
print(peces)
while dia<256:
  pez,i=0,0
  while i<len(peces):
    if peces[i]==0:
      peces[i]=6
      pez+=1
    else:
      peces[i]=peces[i]-1
    i+=1
  for x in range(pez):
    peces.append(8)
  dia+=1
print(len(peces))
