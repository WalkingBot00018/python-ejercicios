'''Llenar una lista de tamaño aleatorio entre 10 y 25 elementos. Llene la lista con números
aleatorios. Encuentre la suma y el promedio de los números de la lista'''

import random
suma, prom = 0, 0
vec=[int(random.random()*100) for i in range(10,25)]
print(vec)
for i in range (len(vec)):
    if vec !=0:
        suma+=vec[i]
        prom = suma // len(vec)
print ("la suma de todos da: ",suma,"y el promedio es: ",prom)