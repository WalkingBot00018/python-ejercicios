"""8. Telefónica realiza los cálculos del costo de una llamada de teléfono siguiendo los cálculos así:
    Cuando se descuelga el teléfono los primeros 3 minutos (banderazo)
    cuestan 200 pesos y cada minuto adicional cuesta 50 pesos.
    Escriba un programa que permita calcular el costo de una llamada dados los minutos de duración."""

valor = 200
min = int(input("¿Cuántos minutos duró?\n"))
if min < 1:
    print ("ERROR, no es ningún minuto")
elif min >= 1 and min <= 3:
    print ("El costo de su llamada por sus ",min," minutos es: $",min * valor)
else:
    valor = 600
    print ("El costo de su llamada por sus ",min," minutos es: $",valor+(min-3)*50)
