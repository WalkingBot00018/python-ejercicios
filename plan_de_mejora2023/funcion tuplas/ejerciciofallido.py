def funcion (t1,t2):
    if(len(t1)>len(t2)):
        return 't1 es mayor'
    elif(len(t1)<len(t2)):
        return 't2 es mayor'
    else:
        return 'son iguales'
tupla1 = 1000,2000,3000,
tupla2 = ('a', 2,'c', 4, 'd')
print(funcion(tupla1,tupla2))
