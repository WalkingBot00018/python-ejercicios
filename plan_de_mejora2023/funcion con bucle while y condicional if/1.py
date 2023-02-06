def suma_impares(inicio, fin):
    suma = 0
    while inicio <= fin:
        if inicio % 2 != 0:
            suma += inicio
        inicio += 1
    return suma

print(suma_impares(1, 10)) # 25
