music={}
def artist(music):
    artista=input("ingrese el artista: ")
    music.update({artista:{}}) 
    return music
def info_artist(music):
    artista=input("ingrese el artista: ")
    if artista not in music:
        print('El artista no se encuentra, agreguelo primero')
        return music
    cancion=input("Ingrese el nombre del cancion: ")
    genero=input("Ingrese el genero musical: ")
    duracion=input("Ingrese la duracion en formato xx(mm):xx(ss): ")
    if artista in music:
        music.update({artista:{"cancion":cancion,"genero":genero,"duracion":duracion}})
        
def cancion_buscar(music):
    buscar=input("buscar cancion :  ")
    for i in sorted(music.values()):
        if buscar==i['cancion']:
            print("la cancion",buscar, "se encuentra en spotify y su duracion es:",i["duracion"])
            return None
    print("la cancion no se encuentra, ingrese el nombre primero")
    
def buscar_artist(music):
    buscar=input("que artista desea buscar: ")
    for x in (music.keys()):
        if buscar==x:
            print("el artista",buscar, "se encuentra en music y su genero es:", music[x]["genero"])
            return None
    print("el artista no se encuentra, ingrese la cancion con el artista")
    
def eliminar_artist(music):
    buscar=input("Que artista desea eliminar?: ")
    for i in sorted(music.keys()):
        if buscar==i:
            del music[i]
            print("La cancion",buscar,"fue eliminada correctamente")
            return None
    print("la cancion no se encuentra, ingrese primero el nombre")
    
def mayor(music):
    may=int
    mayor_valor=0
    for j in (music.keys()):
        minutos=music[j]["duracion"][0]
        minutos+=music[j]["duracion"][1]
        segundos=music[j]["duracion"][3]
        segundos+=music[j]["duracion"][4]
        segundos=int(segundos)+int(minutos)*60
        if mayor_valor<=segundos:
            mayor_valor=segundos
            may=music[j]['cancion']
            
    print("la cancion mas larga es:", may)
    
def menor(music):
    menor = dict
    menor_valor=9e99999
    for x in (music.keys()):
        minutos=music[x]["duracion"][0]
        minutos+=music[x]["duracion"][1]
        segundos=music[x]["duracion"][3]
        segundos+=music[x]["duracion"][4]
        segundos=int(segundos)+int(minutos)*60
        if menor_valor>=segundos:
            menor_valor=segundos
            menor=music[x]['cancion']
            
    print("la cancion mas corta es", menor)
           
while True:
    print("1-ingresar artista")
    print("2-ingresar infromacion de la cancion")
    print("3-eliminar artista")
    print("4-buscar cancion")
    print("5-buscar artista")
    print("6-Cancion mas larga")
    print("7-cancion mas corta")
    print("8-Todas las canciones")
    ctrl=int(input("anexe la opcion que desee: ")) #tipo strin

    match ctrl:
        case 1:
            print(artist(music))
        case 2:
            print(info_artist(music))
        case 3:
            print(eliminar_artist(music))
        case 4:
            print(cancion_buscar(music))
        case 5:
            print(buscar_artist(music))
        case 6:
            print(mayor(music))
        case 7:
            print(menor(music))
        case 8:
            print("Estan todas las canciones anexadas; ",music)
        case _:
            print("opcion invalida")
            break
    