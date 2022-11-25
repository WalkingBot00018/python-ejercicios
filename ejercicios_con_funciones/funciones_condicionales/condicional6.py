#6. Pida un numero al usuario que representa días del año.
#Diga a que mes del año corresponde así:
#Si el número es menor o igual a 31 indica que esta en enero,
#Pero si el número por ejemplo es 32 indica que es el 1 de febrero.
#o tenga en cuenta si el año es bisiesto, es decir siempre febrero tiene 28 días."""

numero = int(input("Ingrese un número del año\n"))
def opps(numero):
    if numero >=1 and numero <=365:
        if numero >0 and numero <=31:
            print ("Es el ",numero," de Enero")
        elif numero >31 and numero <=59:
            print ("Es el ",numero - 31," de Febrero")
        elif numero >59 and numero <=90:
            print ("Es el ",numero - 59," de Marzo")
        elif numero >90 and numero <=120:
            print ("Es el ",numero - 90," de Abril")
        elif numero >120 and numero <=151:
            print ("Es el ",numero - 120," de Mayo")
        elif numero >151 and numero <=181:
            print ("Es el ",numero - 151," de Junio")
        elif numero >181 and numero <=212:
            print ("Es el ",numero - 181," de Julio")
        elif numero >212 and numero <=243:
            print ("Es el ",numero - 212," de Agosto")
        elif numero >243 and numero <=273:
            print ("Es el ",numero - 243," de Septiembre")
        elif numero >273 and numero <=304:
            print ("Es el ",numero - 273," de Octubre")
        elif numero >304 and numero <=334:
            print ("Es el ",numero - 304," de Noviembre")
        elif numero >334 and numero <=365:
            print ("Es el ",numero - 334," de Diciembre")
opps(numero)