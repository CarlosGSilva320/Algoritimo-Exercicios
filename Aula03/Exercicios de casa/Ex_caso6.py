# Considere as atividades da Lista 2(aula anterior)


# Caso6: Sistema de Biblioteca
# Implemente os códigos usando Dicionários

'''Uma biblioteca mantém uma lista de livros emprestados, onde cada item é representado por 
[titulo, usuario, dias_emprestado]. 
Exemplo: 
[ 
    ["Dom Casmurro", "Ana", 5], 
    ["1984", "Carlos", 12], 
    ["O Hobbit", "Marina", 3] 
] 
O sistema precisa: 
1. Listar apenas os livros que estão emprestados há mais de 7 dias. 
2. Encontrar o livro emprestado há mais tempo. 
3. Gerar uma lista apenas com os nomes dos usuários que têm livros emprestados. 
4. Calcular a média de dias de empréstimo. '''

lista = [ 
    ["Dom Casmurro", "Ana", 5], 
    ["1984", "Carlos", 12], 
    ["O Hobbit", "Marina", 3] ]

dicionario = {}

for i in lista:
    titulo = i[0]
    nome = i[1]
    dias = i[2]

    dicionario[titulo] = {"nome" : nome, "dias_emprestados" : dias}

print(dicionario)


def analisar_dados():


    for chave, valor in dicionario.items():
        if valor["dias_emprestados"] > 7:
            print(f"Titulo emprestado a mais de 7 dias: {chave}, {valor['dias_emprestados']} dias")



    maior_dia = 0
    mais_tempo = []

    for chave, valor in dicionario.items():
        if valor["dias_emprestados"] > maior_dia:
            maior_dia = valor["dias_emprestados"]
            mais_tempo = chave

    print(f"O dia livro emprestado mais tempo é: {mais_tempo}, {maior_dia} dias")

    
    nome_usuario = []

    for chave, valor in dicionario.items():
        if valor["dias_emprestados"] > 0:
            nome_usuario.append(valor["nome"])
    print(f"Usuarios com livros emprestados: {nome_usuario}")

    soma = 0

    for valor in dicionario.values():
        soma += valor["dias_emprestados"] 
    
    media = soma / len(dicionario)
    print(f"A média de dias emprestados é de {media:.2f} dias" )
analisar_dados()
