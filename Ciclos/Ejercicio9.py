# Calcular la operación x n sin utilizar la función pow 


from ast import main
from pickle import long
from tokenize import Exponent


long potenciaConwhile(long numero,long potencia) 
{
    long resultado = Num;
    while(potencia > 1)
    {
        resultado = resultado * numero;
        potencia--;
    }
    return resultado;
}
int main()
{
    long Exponent = 3, // Al cubo
    long numero = 9;
    long elevadoAlcubo = potenciaRecursiva(numero,potencia);
    printf("probando con recursividad. %ld elevado a %ld es %ld\n", numero, potencia, elevadoAlcubo);
    long elevadoConwhile = (numero, potencia);
    printf("probando con while. %ld elevado a %ld es %ld\n",numero,potencia,elevadoAlcubo);
}