# 1. Busca Linear Simples 
'''o Dado um vetor de números inteiros e um número alvo, use busca sequencial para 
verificar se o número está presente. 
o Extra: informe o índice se encontrar.'''

lista = [10, 5, 89, 76, 58, 101, 33, 66, 86, 66]

def busca_sequencial(lista, x):
    for i in range(len(lista)):
        if lista[i] == x:
            return True, i
    return False, -1

resultado = busca_sequencial(lista, 100)
print(resultado)

# 2. Contar Ocorrências (Busca Linear) 
'''o Conte quantas vezes um número aparece na lista usando busca sequencial.'''


def contagem_busca(lista, x):
    cont = 0

    for i in range(len(lista)):
        if lista[i] == x:
            cont += 1
    return cont

resultado = contagem_busca(lista, 66)
print(resultado) 


# 3. Maior Número (Busca Linear) 
'''o Use busca sequencial para encontrar o maior número em uma lista.'''

def maior_numero(lista):
    maior = lista[0]
   
    
    for i in range(len(lista)):
        if lista[i] >= maior:
            maior = lista[i]
            
    return maior

resultado = maior_numero(lista)
print(resultado)


# 4. Menor Número (Busca Linear) 
'''o Similar ao anterior, mas encontre o menor valor.'''

def menor_numero(lista):

    menor = lista[0]

    for i in range(len(lista)):
        if lista[i] <= menor:
            menor = lista[i]
    return menor

resultado = menor_numero(lista)
print(resultado)


# 5. Verificar Elemento (Busca Binária) 
'''o Dada uma lista ordenada, implemente a busca binária para verificar se o 
elemento existe.'''

lista_ordenada = sorted(lista)



def busca_binaria(lista_ordenada, x):
    l = 0
    r = len(lista_ordenada) - 1

    while (l <= r):
        m = (l + r) // 2
        if lista[m] == x:
            return True
        elif lista[m] > x:
            r = m - 1
        else:
            l = m + 1
    return False
      
resultado = busca_binaria(lista_ordenada, 4)
print(resultado)