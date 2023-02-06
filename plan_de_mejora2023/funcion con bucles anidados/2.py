def imprimir_triangulo(n):
    for i in range(1, n + 1):
        for j in range(i):
            print("*", end="")
        print("")

imprimir_triangulo(5)