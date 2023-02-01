# Crear una función para obtener los elementos de una tupla desde un índice inicial hasta el final
def obtener_elementos(tupla, inicio):
    return tupla[inicio:]

# Crear una tupla
mi_tupla = (1, 2, 3, 4, 5, 6, 7)

# Usar la función para obtener los elementos de la tupla desde el índice 2
resultado = obtener_elementos(mi_tupla, 2)

# Imprimir el resultado
print(resultado)
