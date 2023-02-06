def obtener_elemento_mayor(tupla):
    if len(tupla) == 0:
        return None
    mayor = tupla[0]
    for elemento in tupla:
        if elemento > mayor:
            mayor = elemento
    return mayor

mi_tupla = (1, 4, 2, 5, 7, 8)
print(obtener_elemento_mayor(mi_tupla))
