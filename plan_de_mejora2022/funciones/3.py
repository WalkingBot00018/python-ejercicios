# ejemplo de numeros reales para calcular  el valor de e^a para a  real con la siguiente formula.

def elevado (a, k):
    productorio = 1.0
    for i in range (k):
        productorio *= a
    return productorio
def factorial (k):
    productorio = 1.0
    for i in range(2, k+1):
        productorio *= i
    return productorio
def exponencial(a, n):
    sumatoria = 0.0
    for k in range (n):
        sumatoria += elevado (a, k) / factorial (k)
    return sumatoria