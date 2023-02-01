
def funcion(dictionary,key,value):
    if key not in dictionary.keys():
        dictionary[key] = value
        print(dictionary)

    else:
        print('existe')

di={"gato": "cat", "perro": "dog", "caballo" : "horse"}
funcion(di, 'perro', 'rabbit')
