suma = 0
for i in range (10):
    if i > 7:
        break
    suma = suma + i
    print ('la suma con break ha sido: ', suma)
    suma = 0 
    for  i in range (10):
        suma = suma + i
    print (' la suma  sin break  ha sido: ', suma)
