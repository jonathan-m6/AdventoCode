from typing import Pattern
import valores
cadena=valores.getLetras(True)
cadena2=valores.getLetras(True)
combinaciones,valor=valores.getAliaciones(True)
for i in range(40):
  for x in range(len(cadena)):
    if x+1==len(cadena):
      break
    par=cadena[x]+cadena[x+1]
    if par in combinaciones:
      indice = combinaciones.index(par)
      parte1,parte2=cadena2[:x+x+1],cadena2[x+1+x:len(cadena2)]
      cadena2=parte1+valor[indice]+parte2
  cadena=cadena2
  print(i)
abc=[chr(i) for i in range(ord('A'),ord('Z')+1)]
conteo=[]
for letra in abc:
  conteo.append(cadena.count(letra))
conteo=[nocero for nocero in conteo if nocero !=0]
print(str(max(conteo))+"-"+str(min(conteo))+"="+str(max(conteo)-min(conteo)))