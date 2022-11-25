def numeros_positivos(num =int(input("Ingrese un número      "))):
    cont=0
    while num>-1:
        num = num=int(input("Ingrese un número      "))
        cont +=1
    print("El total de los numeros positivos: ", cont)
numeros_positivos()
