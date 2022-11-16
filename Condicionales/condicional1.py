'''Pedir numeros e indicar cual de ellos es el valor del
medio'''

a=int(input("Digita el primer numero: "))
b=int(input("Digita el segundo numero: "))
c=int(input("Digita el tercer numero: "))
if a>b and a<c:
        print("El numero",a,"es el numero del medio")
elif a>c and a<b:
        print("El numero",a,"es el numero del medio")
elif b>a and b<c:
        print("El numero",b,"es el numero del medio")
elif b<a and b>c:
        print("El numero",b,"es el numero del medio")
elif c<a and c>b:
        print("El numero",c,"es el numero del medio")
elif c>a and c<b:
        print("El numero",c,"es el numero del medio")
elif a==b:
        print("No se puede calcular el valor del medio")
elif a==c:
        print("No se puede calcular el valor del medio")
elif c==b:
        print("No se puede calcular el valor del medio")
else:
        print("Todos son iguales")

