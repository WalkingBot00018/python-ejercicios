# Determinar si un numero es o no es primo
n = int(input("Digite un numero: "))
x = 1
l = 0
while x <= n: 
    if n %  x == 0: 
        l = l + 1
    x = x + 1  
if l == 2:
    print("El numero ",n,"es primo")
else:
    print("el numero",n,"no es primo")
    