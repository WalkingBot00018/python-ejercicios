# Determinar los divisores de un número introducido por teclado

print("introduzca el numero")
numero = int(input()) #aquí se lee el número entero
contador = 0
print("los divisores de ",numero)
for divisor in range(1,numero+1):
    if (numero % divisor) == 0 :
        print(divisor,"es divisor")
        contador += 1
print("el numero ",numero," tiene ",contador," divisores")