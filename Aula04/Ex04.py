#4.  Escreva uma função recursiva que verifique se uma string é um palíndromo. Um 
#palíndromo é uma palavra ou frase que se lê da mesma forma de trás para frente, 
#ignorando espaços, maiúsculas e minúsculas. Por exemplo, "arara" é um palíndromo.

def palindromo(palavra):

    #caso base
    if palavra == palavra[::-1]:
        return palavra
    elif palavra != palavra[::-1]:
        return "não é um palindromo"
    return palavra[-1] + palindromo(palavra[:-1]) 

resultado = palindromo('carro')
print(resultado)