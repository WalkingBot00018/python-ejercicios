#5.	En un juego de preguntas a las que se responde “Si” o “No”
#gana quien responda correctamente las tres preguntas.
#Si se responde mal a cualquiera de ellas ya no se pregunta la siguiente y termina el juego.
#Las preguntas son:
#    1.	Colon descubrió América?
 #   2.	La independencia de Colombia fue en el año 1810?
  #  3.	The Doors fue un grupo de rock Americano?.

pregunta = input("¿Colón descubrió a America?")
def colon(pregunta):
    print ("JUEGO DE PREGUNTAS: (Responde 'si' o 'no'")
    if pregunta == "si" or pregunta == "Si":
            return("Haz respondido mal, fin del juego")
    elif pregunta ==1:
        pregunta = int(input("¿La independencia de Colombia fue en el año 1810? (1. Si 2.No\n"))
        if pregunta != 1:
            return("Haz respondido mal, fin del juego")
    elif pregunta ==1:
        pregunta = int(input("The Doors fue un grupo de Rock Americano (1. Si 2.No\n"))
        if pregunta != 2:
            return("Haz respondido mal, fin del juego")
        else:
            return("Haz ganado el juego")
colon(pregunta)