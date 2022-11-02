"""numeros de 3 digitos donde la suma del cubo de cada digito sea igual al numero."""

for y in range (100,1000):
    md = 0
    suma = 0
    i = y
    while i > 0:
            x = i % 10
            n = i // 10
            md = x**3
            suma += md
            i = n
    if suma == y:
            print(y)
            