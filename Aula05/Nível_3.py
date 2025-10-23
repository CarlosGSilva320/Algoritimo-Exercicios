#11. Busca em Lista de Dicionários 
'''• Dada uma lista de dicionários representando pessoas ({"nome": "Ana", "idade": 
25}), implemente uma busca linear para encontrar a pessoa com nome "João".''' 

lista = [
    {"nome" : "Ana", "idade" : 25},
    {"nome" : "João", "idade" : 30},
    {"nome" : "Mario", "idade" : 35}
]

nome = input("Digite um nome: ").capitalize()

def busca_linear(lista, nome):
    for i in lista:
        if i["nome"] == nome:
            return f"Nome {i['nome']} pertence a lista" 
        
    return "Não pertence a lista"
        
resultado = busca_linear(lista, nome)
print(resultado)


#12. Jogo: Adivinhe o Número (Busca Binária) 
'''• O computador escolhe um número entre 1 e 100. O jogador tenta adivinhar, e o 
computador responde se é maior ou menor. Use lógica de busca binária para resolver 
com o menor número de tentativas.'''

import random

print("Advinhe o número de 1 até 100: ")

numero_secreto = random.randint(1, 100)
tentativas = 0
baixo = 1
alto = 100

while True:
    tentativas += 1
    palpite = int(input(f"Tentativa {tentativas}: seu palpite ({baixo} a {alto}): "))

    if palpite < numero_secreto:
        print("O número secreto é maior")
        baixo = palpite + 1 
    elif palpite > numero_secreto:
        print("O número secreto é menor")
        alto = palpite - 1
    else:
        print("''Acertou, Parabéns!!!")
        break

#13. Buscar Produtos por Preço 
'''• Dada uma lista de produtos com preços, implemente uma busca para encontrar todos os 
produtos com um determinado preço.'''

produtos = [
    {"nome": "Arroz", "preco": 10},
    {"nome": "Feijão", "preco": 8},
    {"nome": "Macarrão", "preco": 10},
    {"nome": "Açúcar", "preco": 6},
    {"nome": "Café", "preco": 15}
]

preco_busca = float(input("Digite o preço para busca: R$ "))

def buscar_preco(produtos, preco_busca):
    encontrados = []
    for produto in produtos:
        if produto["preco"] == preco_busca:
            encontrados.append(produto["nome"])
    return encontrados
    

resultado = buscar_preco(produtos, preco_busca)
print(resultado)

#14. Implementar sua própria função index() 
'''• Crie uma função meu_index(lista, valor) que funcione como o método 
list.index(), usando busca sequencial.'''

lista = [10, 20, 30, 40, 50]


def meu_index(lista, valor):
    for i in range(len(lista)):
        if lista[i] == valor:
            return i
    return -1

print(meu_index(lista,30))