def primos(numero):
    for i in range(2, numero):
        es_primo = True
        for j in range(2, i):
            if i % j == 0:
                es_primo = False
                break
        if es_primo:
            print(i)

primos(20) # 2 3 5 7 11 13 17 19
