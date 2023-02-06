def verificar_igualdad_elementos(tupla):
    elemento_inicial = tupla[0]
    for elemento in tupla:
        if elemento != elemento_inicial:
            return False
    return True

mi_tupla = (1, 4, 2, 5, 7, 8)
print(verificar_igualdad_elementos(mi_tupla))