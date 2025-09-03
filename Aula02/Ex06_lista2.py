#Caso 6: Sistema de Biblioteca 

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


biblioteca = [ 
    ["Dom Casmurro", "Ana", 5], 
    ["1984", "Carlos", 12], 
    ["O Hobbit", "Marina", 3] ]

def analisar_dados():

    mais_7 = []
    for livro in biblioteca:
        if livro[2]> 7:
            mais_7.append(livro[0])

    maior_dia = 0
    livro_mais_tempo = ""
    for livro in biblioteca:        
        if livro[2] > maior_dia:
            maior_dia = livro[2]
            livro_mais_tempo = livro[0]
    
    usuario = []
    for livro in biblioteca:
        usuario.append(livro[1])

    soma_dias = 0
    for livro in biblioteca:
        soma_dias += livro[2]
        media_dias = soma_dias / len(biblioteca)


    print(f"Os livros emprestados a mais de 7 dias: {mais_7}")

    print(f"O livro emprestado a mais tempo: {livro_mais_tempo}")

    print(f"Usuários que tem livros emprestados: {usuario}")

    print(f"A média de dias emprestados : {media_dias:.1f}")


analisar_dados()