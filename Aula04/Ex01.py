#1. Escreva uma função recursiva que calcule o máximo divisor comum (MDC) de dois números inteiros a e b. 

def mdc(a,b):
    #caso base
    if b == 0:
        return a
    return mdc(b, a % b)

resultado = mdc(8,4)
print(resultado)