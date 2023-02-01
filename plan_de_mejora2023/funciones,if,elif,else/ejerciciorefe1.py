# Crear una función para imprimir un mensaje
def imprimir_mensaje(valor):
    # Usar un bucle if, elif y else para imprimir un mensaje diferente en función del valor de la variable
    if valor == 0:
        print("El valor es 0")
    elif valor == 1:
        print("El valor es 1")
    else:
        print("El valor es diferente de 0 y 1")

# Crear una variable
mi_valor = 0

# Usar la función para imprimir un mensaje en función del valor de la variable
imprimir_mensaje(mi_valor)