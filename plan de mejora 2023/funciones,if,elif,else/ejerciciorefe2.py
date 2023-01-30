# Crear una función para determinar si un número es par o impar
def es_par_o_impar(numero):
    # Usar un bucle if, elif y else para verificar si el número es par o impar
    if numero % 2 == 0:
        print("El número es par")
    elif numero % 2 != 0:
        print("El número es impar")
    else:
        print("El número no es un entero")

# Usar la función para comprobar si el número 7 es par o impar
es_par_o_impar(7)


