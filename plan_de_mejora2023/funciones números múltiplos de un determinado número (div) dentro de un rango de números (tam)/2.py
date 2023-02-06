def sumar_divisibles(tam, div):
    suma = 0
    for i in range(1, tam):
        if i % div == 0:
            suma += i
    print("La suma de los números divisibles por", div, "es", suma)

sumar_divisibles(10, 2)
