def calcular_area(dimensiones):
     ancho = dimensiones[0]
     altura = dimensiones[1]
     return ancho * altura

# Crear una tupla con las dimensiones de un rectangulo
rectángulo_dimensiones = (3, 4)

# Pasar la tupla como parametro a la funcion
area_rectángulo = calcular_area(rectángulo_dimensiones)

print("El area del rectangulo es: ", area_rectángulo) # imprime "El area del rectangulo es: 12"
