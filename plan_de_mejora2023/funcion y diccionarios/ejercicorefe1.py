

def obtener_valor(key,diccionario):
    return diccionario[key]

mis_datos={
    "nombre" : "pedro",
    "edad" : 30
}

mi_lista =[1,2,3,4]

valor1 = obtener_valor("nombre", mis_datos)
print("nombre: "+ valor1)

valor2 = obtener_valor(2, mi_lista)
print( "valor de la lista en la posicion 2: "+ str(valor2))
