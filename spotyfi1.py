musica={}

def artista(lista):
    artista=input('Ingrese el nombre del artista: ')
    genero=input('Ingrese el genero: ')
    cancion=input('Ingrese una cancion del artista: ')
    duracion=input('ingrese duracion de la cancion: ')
    lista.update({artista:{'Genero':genero,'Cancion':[cancion, duracion]}})
    return lista

def anexar_cancion(lista):
    artista=input('Ingrese el nombre del artista: ')
    cancion=input('Ingrese otra cancion del artista: ')
    duracion=input('ingrese duracion de la cancion: ')
    if artista in lista:
        lista[artista.append(cancion)]
        lista[artista.append(duracion)]
    return lista

def eliminar(nombre):
    del musica[nombre]
    return musica


def buscar_artista(lista):
    buscar=input('¿Que artista desea buscar?: ')
    for i in sorted(lista.keys()):
        if buscar==i:
            print('El artista',buscar,'se encuentra en spotify y su genero es:',lista.get(artista))
        else:
            print('El artista',buscar,'no se encuentra en spotify')

while True:
    artista(musica)
    print (musica)
    anexa=int(input('Si desea agregar mas canciones a este artista, marque 1, de lo contrario, marque 0'))
    if anexa==1:
        anexar_cancion(musica)
        anexa1=int(input('si desea agregar otra cancion, marque 1, de lo contrario para finalizar el programa, marque 0'))
        if anexa==0:
            break
            
        
print(musica)