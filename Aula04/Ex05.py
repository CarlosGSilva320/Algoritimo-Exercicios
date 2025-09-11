#5.  Escreva uma função recursiva que calcule a soma dos dígitos de um número inteiro positivo.

def soma_digitos(n):

    #caso base
    if n < 10:
        return n
    
    return n % 10 + soma_digitos(n  // 10)

resultado = soma_digitos(51)
print(resultado)