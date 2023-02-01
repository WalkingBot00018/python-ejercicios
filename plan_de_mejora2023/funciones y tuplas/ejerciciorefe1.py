# Crear una función para contar la cantidad de veces que aparece un elemento en una tupla
def contar_elementos(tupla, elemento):
    contador = 0
    for item in tupla:
        if item == elemento:
            contador += 1
    return contador

# Crear una tupla
mi_tupla = ("Perro", "Gato", "Perro", "Conejo", "Perro")

# Usar la función para contar la cantidad de veces que aparece el elemento "Perro" en la tupla
num_perros = contar_elementos(mi_tupla, "Perro")

# Imprimir el resultado
print(num_perros)