'''Llenar una lista de tamaño aleatorio entre 10 y 25 elementos. Llene la lista con números
aleatorios. Encuentre la desviación estandar'''

import random
def n():
    tam=round(random.randint(10,25))
    vec=[]
    dif=[]
    media=0
    print('Tam=',tam)
    for i in range (tam):
        vec.append(round(random.random()*100))
    print(vec)
    for i in vec:
        media+=i
    media=media/len(vec)   
    print('La media es igual a: ',media)
    suma=0
    for i in range(len(vec)):
        x=(vec[i]-media)**2
        dif.append(x)
        suma+=x
    print('El total de la suma es: ',suma)
    print('La desviacion estandar es igual a: ',(suma/len(vec))**0.5)
n()