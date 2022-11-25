#Calcular todos los números de 3 cifras tales que la suma
#de los cubos de las cifras es igual al valor del número.

num=int(input('ingrese numero de 3 cifras'))
if num>=100 and num<=999:
    numero= str(num)
    suma= int(numero[0])+ int(numero[1]) + int(numero[2])
    alcuadrado=suma * suma
    print('la suma es igual a: ', suma)
    print(' el cuadrado es: ', alcuadrado)
else:
    print('el numero ingresado es mayor de 3 cifras: ')
    print('vueva a digitar un numero de 3 cifras: ')