"""13. Solicite al usuario una cantidad numérica que expresa segundos (medida de tiempo).
Exprésela (conviértala) en horas minutos y segundos. Según el caso."""

from math import trunc


tiempo1 = int(input("Ingrese una cantidad en segundos: "))
tiempo = tiempo1
horas = trunc(tiempo/3600)
tiempo = tiempo-(horas*3600)
minutos = trunc(tiempo/60)
tiempo = tiempo - (minutos*60)

if tiempo1<0:
    print("ERROR, no ingreso un tiempo correcto")
else:
    print("hora","min","seg",sep="  ")
    print(horas,minutos,tiempo,sep="    ")