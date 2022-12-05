# ejemplo de diseñar  un programa  que muestre el valor de  factorial(n) para n entre 0 y 7


def exponencial (a, n):
    numerador = 1 
    denominador = 1
    sumatorio = 10
    for k in range (1, n):
        numerador = a * numerador 
        denominador = k* denominador
        sumatorio += numerador / denominador
    return sumatorio 