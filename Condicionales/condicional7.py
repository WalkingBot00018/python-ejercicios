    #7. Un obrero necesita calcular su salario semanal, el cual se obtiene de la sig. manera:
    #Si trabaja 40 horas o menos se le paga $2600 por hora
    #Si trabaja más de 40 horas se le paga $2600 por cada una de las primeras 40 horas
    #y $5000 por cada hora extra.

salario = 2600
horas = int(input("¿Cuántas horas trabajo?\n"))
if horas < 1:
    print ("No digito una hora correcta")
elif horas >= 1 and horas <= 40:
    print ("Su salario semanal por las ",horas," trabajadas es: $",salario * horas)
else:
    salario = 40*2600
    print ("Su salario semanal por las ",horas," trabajadas es: $",salario+((horas-40)*5000))