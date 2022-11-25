

def hola(radio = int(input("cual es su radio"))):
    respuesta_a= 3.14 * radio**2
    respuesta_1 = 2*3.14*radio
    respuesta_d = 2*radio
    respuesta_c = respuesta_d*3.14
    return ("su area es", respuesta_a )
    return ("su longitud es", respuesta_1)
    return("su diametro es ", respuesta_d)
    return ("su circunferencia es ", respuesta_c,"o tambien", respuesta_d,"por PI unidades")
print(hola(radio = int(input("cual es su radio"))))