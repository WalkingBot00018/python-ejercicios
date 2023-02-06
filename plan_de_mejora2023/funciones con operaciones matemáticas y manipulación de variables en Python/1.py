
def ecuacion_cuadratica(a, b, c):
    import math
    x1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
    x2 = (-b - math.sqrt(b**2 - 4*a*c)) / (2*a)
    return x1, x2
a=2
b=3
c=4

ecuacion_cuadratica()