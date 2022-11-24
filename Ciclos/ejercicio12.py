"""12. Escribir un programa que visualice la siguiente figura,
    utilizando ciclos. El usuario decide cuantas líneas quiere imprimir.
    *
    **
    ***
    ****
    ***** """
    
cont=0
asterisco=""
linea = int (input("cuantas lineas desea imprimir:  "))
for i in range (linea):
    asterisco+="*"
    print(asterisco)