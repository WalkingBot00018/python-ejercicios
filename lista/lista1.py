
import random
cont=0
cont2=0
sumapar=0
sumaimpar=0

tam=int(input('ingrese cantidad'))
vec=[]
for i in range(tam):
    vec.insert(i,round(random.random()*100))
print(vec)                   # es para calcular numero random con lista


for i in range(len(vec)):    # este es para mirar de lo del numero random si es par o impar
    if vec[i]%2==0:
        print(vec[i],' par')
    else:
        print(vec[i],' impar')

        cont += 1

print("finaliza")
print("cuantos pares hay", cont)
print("cuantos impares hay", cont)
sumapar=+ vec[i]
print('')



