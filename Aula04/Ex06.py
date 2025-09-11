#6.  Escreva uma função recursiva que encontre todos os anagramas de uma string. 
 
def anagramas(palavra):

    #caso base
    if len(palavra) == 1:
        return palavra
    
    resultado =[]

    for i in range(len(palavra)):
        
        letra = palavra[i]
        resto = palavra[:i] + palavra[i+1:] 
        for perm in anagramas(resto):
            resultado.append(letra + perm)
    return resultado

anagrama = anagramas('casa')
print(anagrama)