'''Llene una lista con la serie de Fibonacci. La cantidad de elementos de la lista la debe ingresar el
usuario. Mínimo debe tener 5 elementos y máximo 20.'''

while True:
    n=int(input("¿Cuantos valores deseas? (min5)(max20): "))
    if n>4 and n<21:
        break
vec=[0,1]
for i in range (n-2):
    vec.append(vec[-1]+vec[-2])
print("Serie Fibonacci: ",vec)




