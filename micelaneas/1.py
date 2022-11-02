""" Llenar una lista de tamaño aleatorio entre 10 y 25 elementos. Llene la lista con números
aleatorios. De cada elemento de la lista diga si el elemento está por encima del promedio, debajo
del promedio o es igual al promedio de todos los números de la lista."""

import random

asd=[]
suma=0
cont=0
for a in range (random.randint(10, 25)):
    asd.insert(0,int(random.random()*100))
    suma =+ asd[a]
    cont =+ 1    
prom = suma/cont

for a in asd:
    if a >prom:
        print(a, "es mayor al prom")
    elif a <prom:
        print(a,"es menor al prom")   
    else:
        print(a, "es igual al prom")
        
        
        