

def convertir(digito,cero,uno,dos,tres,cuatro,cinco,seis,siete,ocho,nueve):
  num=[cero,uno,dos,tres,cuatro,cinco,seis,siete,ocho,nueve]
  digOrdenado="".join(sorted(digito))
  for i in range(len(num)):
    this="".join(sorted(num[i]))
    if digOrdenado==this:
      return i
suma=0
ceroR,dosR,cincoR,seisR,nueveR="","","","",""
with open("Dia 8/real.txt","r") as archivo:
    for linea in archivo:
      numero=""
      cont9=0
      cero,uno,dos,tres,cuatro,cinco,seis,siete,ocho,nueve="","","","","","","","","",""
      salida=str(linea.strip().split("|")[0]).split(" ")
      salida=sorted(salida, key=len)
      for dig in salida:
        if len(dig)==2:
          uno=dig
        if len(dig)==3:
          siete=dig
        if len(dig)==4:
          cuatro=dig
        if len(dig)==7:
          ocho=dig
        if len(dig)==5:
          ver=0
          for i in siete:
            if i in dig:
              ver+=1
          if ver==3:
            tres=dig
          if ver!=3:
            if uno[0] in dig:
              dos=dig
            elif uno[1] in dig:
              cinco=dig
        if len(dig)==6:
          cont=0
          for i in cinco:
            if i in dig:
              cont+=1
          if cont==5:
            if uno[0] in dig:
              nueve=dig
            else: seis=dig
          if cont!=5:
            cero=dig
        #por si falla
        if len(dig)==5:
          ver=0
          for i in siete:
            if i in dig:
              ver+=1
          if ver!=3:
            if uno[1] in dig:
              dosR=dig
            elif uno[0] in dig:
              cincoR=dig
        if len(dig)==6:
          cont=0
          for i in cincoR:
            if i in dig:
              cont+=1
          if cont==5:
            if uno[1] in dig:
              nueveR=dig
            else: seisR=dig
          if cont!=5:
            ceroR=dig
      salida=str(linea.strip().split("|")[1]).split(" ")
      for dig in salida:
        if nueve=="":
          numero+=str(convertir(dig,ceroR,uno,dosR,tres,cuatro,cincoR,seisR,siete,ocho,nueveR))
        else: numero+=str(convertir(dig,cero,uno,dos,tres,cuatro,cinco,seis,siete,ocho,nueve))
      print(numero)
      suma+=int(numero)
print (suma)

