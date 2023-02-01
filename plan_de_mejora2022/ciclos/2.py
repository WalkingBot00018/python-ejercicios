# ejemplo que imprime las tablas de multiplicar del 3 hasta el 7

primero = 3 
while primero <= 7:
    print('tabla del ' + str (primero))
    segundo = 1
    while segundo <= 10:
        print (str ( primero ) + 'x' + str (segundo ) + ' = ' + str (primero * segundo ))
        segundo += 1
    primero += 1
    print('')
