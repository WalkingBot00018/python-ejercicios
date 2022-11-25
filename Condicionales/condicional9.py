#Solicite una fecha al usuario. en formato día, mes y año. Dígale cuanto tiempo
#ha pasado desde esa fecha hasta hoy o cuanto falta para llegar a esa fecha si es
#posterior

import datetime
año = int(input("inserte un año"))
mes = int(input("inserte un mes"))
dia = int(input("inserte un dia"))
fecha = datetime.datetime(año, mes, dia)
fecha_a = datetime.datetime.now()
diferecia = fecha - fecha_a  
dias_p = diferecia.days
if dias_p - 0:
    print("han pasado ",dias_p, "dias")
else:
    print("faltan ", dias_p)