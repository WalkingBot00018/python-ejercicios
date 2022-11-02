"""pedir numeros, imprimirlo con el opuesto 
(ejemplo 5 opuesto -5, -10 opuesto 10), 
finaliza con cero y diga cuantos ingreso"""

A = 1
cont = 0

while A != 0:
        A = int(input("Escriba un numero"))
        if A !=0:
            print(A,"opuesto" ,-(A))
            cont += 1
        if A==0:
            print("finalizacion del programa")
print("ingresado",cont, "numero")
