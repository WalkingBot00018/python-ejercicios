'''Llenar una lista de tamaño aleatorio entre 10 y 25 elementos. Llene la lista con números
aleatorios. Encuentre la moda de los números de la lista'''

import random
tam=round(random.randint(10,25))
vec=[]
vecCant=[]
for i in range(tam):
    vec.append(round(random.random()*100))
print(vec)
cont=0
for i in range(len(vec)): 
    cont=0
    for j in vec:    
        if vec[i] == j:
            cont+=1 
    if cont!=0:
        vecCant.append(cont)
    else:
        vecCant.append(0)
print(vec)
print(vecCant)
mayor=0
pos=0
moda=0
for i in range(len(vec)):
    if mayor<vecCant[i]:
       mayor=vecCant[i]
print('El mayor es ',mayor)
for j in range(len(vecCant)):
    if mayor==vecCant[j]:
        moda=vecCant[j]
        print('la moda es ',vec[j])
    
