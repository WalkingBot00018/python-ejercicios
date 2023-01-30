def fisica(n, n1, n2):
    if(n==1):
        return n1 / n2;
    elif(n == 2):
        return n1 * n2
    else:
        return n2 / n1;

puedeser= int(input('\n\tmenu\n\t1. velocidad\n\t2. espacio\n\t3. tiempo\n\t4. salida\tfavor ingresar opcion: '));

while(puedeser != 4):
    if(puedeser == 1):
        espacio = float(input('\nfavor ingrese el espacio: '));
        tiempo = float(input('\nfavor ingrese el tiempo: '));
        print(str(fisica(1, espacio, tiempo)));
    elif(puedeser == 2):
        espacio = float(input('\nfavor ingrese el espacio: '));
        tiempo = float(input('\nfavor ingrese el tiempo: '));
        print(str(fisica(2, espacio, tiempo)));
    elif (puedeser ==3):
        espacio = float(input('\nfavor ingrese el espacio: '));
        tiempo = float(input('\nfavor ingrese el tiempo: '));
        print(str(fisica(3, espacio, tiempo)));
    else:
        break;
    puedeser= int(input('\n\tmenu\n\t1. velocidad\n\t2. espacio\n\t3. tiempo\n\t4. salida\tfavor ingresar opcion: '))