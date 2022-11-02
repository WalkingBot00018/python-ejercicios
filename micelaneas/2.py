"""Llenar una lista de tamaño aleatorio entre 10 y 25 elementos. Llene la lista con números
aleatorios. Muestre cuales y cuantos son primos"""

import random

asd=[]
suma=0

for a in range (random.randint(10,25)):
    asd.insert(1,int(random.random()*100))
    
print(asd)
for a in asd:
    cont = 0
    for y in range (1,a+1):
        if a % y == 0:
            cont =+ 1
    if cont == 2:
        print(a,"es primo")
        suma+= 1
    else:
        print (a,"no es primo")
print("cantidad de primos", suma)


        
        
            
        
