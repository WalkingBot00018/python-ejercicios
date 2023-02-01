# ejemplo de ¿ cuales son los datos del problema? los coeficientes  a, b y c. ¿ que deseamos  calcular ? los 
# valores  de x  que hacen  cietra la ecuacion dichos valores son:


from  math  import  sqrt 

print (' programa para  la resolucion  de la ecuacion a x * x + b  x  + c= 0. ')

a= float(input('valor de a: '))
b= float(input('valor de b: '))
c= float(input('valor de c: '))
if a != 0:

    x1= (-b + sqrt (b**2 - 4*a*c)) / (2* a)
    x2= (-b - sqrt (b**2 - 4*a*c)) / (2* a)
    print ('soluciones: x1={0:.3f} y  x2={1:.3f}' .format (x1, x2) )
else:
    if b != 0:
        x = -c / b
        print ('solucion:  x= {0:.3f}'.format(x))
    else:
        if c  != 0:
            print('la ecuacion no tiene solucion. ')
        else:
            print ('la ecuacion tiene infinitas soluciones. ')
