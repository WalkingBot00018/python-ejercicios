def suma_matriz(matriz):
    suma = 0
    for fila in matriz:
        for elemento in fila:
            suma += elemento
    return suma
mi_matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
resultado = suma_matriz(mi_matriz)
print(resultado)









