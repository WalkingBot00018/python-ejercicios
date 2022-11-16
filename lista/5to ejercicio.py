'''Llenar una lista de tamaño aleatorio entre 10 y 25 elementos. Llene la lista con números
aleatorios. Solicite al usuario un número para buscar en la lista. Diga cuantas veces está y en que
posiciones esta. Si no está agréguelo al final de la lista.'''

import random

cont=0
cont1=0
suma1=0
tam=random.randint(10, 25)
vec=[]
n=int(input('ingrese el valor del numero que desea buscar: '))
for i in range(tam):
    vec.insert(i,round(random.randint(0, 100)))
print(vec)

for i in range(len(vec)):
    if vec[i]==n:
        cont=cont+1
        suma1=suma1+vec[i]

if cont>0:
    print('El numero ',n,'esta ',cont,"vez")
else :
    print('El numero ',n,' no se encuentra en la lista')
if n != vec[i]:
    vec.append(n)
print(vec)