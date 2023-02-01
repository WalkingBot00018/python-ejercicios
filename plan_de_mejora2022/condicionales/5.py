# Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.

n = int(input("Introduce un número entero: "))
if n % 2 == 0:
    print("El número " + str(n) + " es par")
else:
    print("El número " + str(n) + " es impar")