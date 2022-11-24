"""11. Escribir un algoritmo que pida un valor entero que equivale a una cantidad de DINERO
    y calcule a cuantos billetes de 50.000, 20.000, 10.000, 5.000, 2.000, y 1.000 equivalen.
    Si el usuario digita 282000 el programa debe responder cinco billetes de 50.000
    un billete de veinte mil, un billete de diez mil, un billete de dos mil."""

from math import trunc


dinero1= int(input("Ingrese la cantidad de dinero  $"))
dinero = dinero1
cincuenta = trunc(dinero/50000)
dinero = dinero - (50000*cincuenta)
veintemil = trunc(dinero/20000)
dinero = dinero - (20000*veintemil)
diezmil = trunc(dinero/10000)
dinero = dinero - (10000*diezmil)
cincomil = trunc(dinero/5000)
dinero = dinero - (5000*cincomil)
dosmil = trunc(dinero/2000)
dinero = dinero - (2000*dosmil)
mil = trunc(dinero/1000)
dinero = dinero - (1000*mil)

if dinero1<1000:
    print("digito un valor menor a mil pesos")
else:
    print ("\nEl valor que ingreso: $",dinero1," en billetes es:\n")
    if cincuenta>=1:
        print(cincuenta," billete de $50.000")
    if veintemil>=1:
        print(veintemil," billete de $20.000")
    if diezmil>=1:
        print(diezmil," billete de $10.000")
    if cincomil>=1:
        print(cincomil," billete de $5.000")
    if dosmil>=1:
        print(dosmil," billete de $2.000")
    if mil>=1:
        print(mil," billete de $1.000")