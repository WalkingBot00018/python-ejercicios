#5.	En un juego de preguntas a las que se responde “Si” o “No”
#gana quien responda correctamente las tres preguntas.
#Si se responde mal a cualquiera de ellas ya no se pregunta la siguiente y termina el juego.
#Las preguntas son:
#    1.	Colon descubrió América?
 #   2.	La independencia de Colombia fue en el año 1810?
  #  3.	The Doors fue un grupo de rock Americano?.

print ("JUEGO DE PREGUNTAS: (Responde 'si' o 'no'")
pregunta = input("¿Colón descubrió a America?")
if pregunta == "si" or pregunta == "Si":
    print("Haz respondido mal, fin del juego")
elif pregunta ==1:
    pregunta = int(input("¿La independencia de Colombia fue en el año 1810? (1. Si 2.No\n"))
    if pregunta != 1:
        print("Haz respondido mal, fin del juego")
    elif pregunta ==1:
        pregunta = int(input("The Doors fue un grupo de Rock Americano (1. Si 2.No\n"))
        if pregunta != 2:
            print("Haz respondido mal, fin del juego")
        else:
            print("Haz ganado el juego")