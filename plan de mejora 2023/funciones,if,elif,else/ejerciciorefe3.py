# Crear una función para determinar si un número es positivo o negativo
def es_positivo_o_negativo(numero):
    # Usar un bucle if, elif y else para verificar si el número es positivo o negativo
    if numero > 0:
        print("El número es positivo")
    elif numero < 0:
        print("El número es negativo")
    else:
        print("El número es 0")

# Usar la función para comprobar si el número -5 es positivo o negativo
es_positivo_o_negativo(-5)