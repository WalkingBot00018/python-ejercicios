def obtener_frecuencia_elementos(tupla):
    frecuencia = {}
    for elemento in tupla:
        if elemento in frecuencia:
            frecuencia[elemento] += 1
        else:
            frecuencia[elemento] = 1
    return frecuencia

mi_tupla = (1, 4, 2, 5, 7, 8)
print(obtener_frecuencia_elementos(mi_tupla))