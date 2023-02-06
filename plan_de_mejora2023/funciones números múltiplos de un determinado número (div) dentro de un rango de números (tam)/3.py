def contar_divisibles(tam, div):
    contador = 0
    for i in range(1, tam):
        if i % div == 0:
            contador += 1
    print("Hay", contador, "números divisibles por", div, "en el rango [1,", tam, ")")

contar_divisibles(10, 3)
