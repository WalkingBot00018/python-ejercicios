def numero_primo(n=int(input("Ingrese un numero: "))):
    for i in range(1,n):
        if n % i == 0:
            return "El numero es perfecto"
    else:
        return "El numero no es perfecto"
print(numero_primo())