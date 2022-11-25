from math import sqrt

A = int(input("Digite el coeficiente de la variable cuadratica\n"))
B = int(input("Digite el coeficiente de la variable cuadratica\n"))
C = int(input("Digite el  termino independiente\n"))
x1= 0
x2= 0
x3= 0


if ((B**2)-4*A*C) < 0:
    print("La solucion de la ecuacion es  con numeros complejos")
else:
   x1 = (-B+sqrt(B**2-(4*A*C)))/(2*A)
   x2 = (-B-sqrt(B**2-(4*A*C)))/(2*A)
   x3 = (-B-sqrt(B**2-(4*A*C)))/(2*A)
   print("Las soluciones de la ecuacion son:")
   print(x1)
   print(x2)
   print(x3)
   
