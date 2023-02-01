#ejemplo de definir una funcion que convierte radianes a grados en python

import math 
def radianes_a_grados(radianes):
    grados = radianes * (180 / math.pi)

    return grados


print(radianes_a_grados(math.pi)) #180
print(radianes_a_grados(math.pi/2)) #90
print(radianes_a_grados(math.pi/3)) #60


 