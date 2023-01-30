
def calcular_total(productos):
    precios={
        "naranja" : 0.5,
        "fresa" : 0.6,
        "limon" : 0.7,

    }

    total= 0
    for producto in productos:
        total += precios[producto]
    return total

mi_canasta = ["naranja","fresa","limon"]
total = calcular_total(mi_canasta)
print("El precio total es: " + str(total) + "€")
