# contador de palabras ejemplo

cadena = input('escriba una frase: ')
while cadena !="":
    blancas = 0 
    for  caracter  in cadena:
        if  caracter == " ":
            blancas += 1
    palabras = blancas + 1 
    print ('palabras: ', palabras) 

    cadena = input (' escribe una frase: ')
    

