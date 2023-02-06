def funcion (tam,div):
    for i in range (1, tam):
        if i %div == 0:
            print(i, 'es multiplo de ', div)
        else:
            print(i, 'no es multiplo de ', div)
funcion(19,3)