# 6. Busca de Nome em Lista 
'''o Peça ao usuário para digitar nomes e depois procure um nome específico usando 
busca linear.'''

'''lista = ["carlos", "roberto", "andre", "maria", "joão"]

nome = input("digite um nome: ").lower()

def buscar_nome(nome):
    for i in range(len(lista)):
        if lista[i] == nome:
            return "Nome na lista"
    return "Nome não encontrado"

resultado = buscar_nome(nome)
print(resultado)'''

# 7. Busca Binária Recursiva 
'''o Implemente a versão recursiva da busca binária em uma lista ordenada.'''

'''lista = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

num = int(input("Digite um número: "))

def binaria_recursiva(lista, inicio, fim, num):
    if inicio > fim:
        return "Número não encontrado"
    meio = (inicio + fim) // 2
    if lista[meio] == num:
        return f"Número encontrado na posição -> {meio + 1}"
    elif lista[meio] > num:
        return binaria_recursiva(lista, inicio, meio - 1, num)
    else:
        return binaria_recursiva(lista, meio + 1, fim, num)

resultado = binaria_recursiva(lista, 0, len(lista) - 1, num)
print(resultado)'''


# 8. Comparar Tempo de Execução 
'''o Compare o tempo de execução da busca linear e busca binária em uma lista 
com 1 milhão de elementos. Use o módulo time.'''

'''import time
import random

lista = list(range(1_000_000))

num = random.choice(lista)

def busca_linear(lista, num):
    for i in range(len(lista)):
        if lista[i] == num:
            return i
    return -1
inicio = time.time()
busca_linear(lista, num)
fim = time.time()

tempo_linear = fim - inicio
print(f"Tempo de busca linear de {tempo_linear:.6f}s")

def busca_binaria(lista, inicio, fim, num):
    if inicio > fim:
        return -1
    m = (inicio + fim) // 2

    if lista[m] == num:
        return m
    elif lista[m] > num:
        return busca_binaria(lista, inicio, m - 1, num)
    else:
        return busca_binaria(lista, m + 1, fim, num)

inicio = time.time()
busca_binaria(lista, 0, len(lista) - 1, num)
fim = time.time()

tempo_binaria = fim - inicio

print(f"Tempo de busca binária de {tempo_binaria:.6f}s")'''

# 9. Encontrar Primeira Ocorrência (Busca Binária Modificada) 
'''o Dada uma lista ordenada com elementos repetidos, use busca binária modificada 
para encontrar o índice da primeira ocorrência de um número.'''