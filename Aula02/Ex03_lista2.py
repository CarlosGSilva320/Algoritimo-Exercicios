'''Caso3: Supermercado – Controle de Estoque 
Um supermercado mantém uma lista de produtos e seus preços. 
• Cada item será representado como [nome, quantidade, preco_unitario]. 
• O sistema deve: 
1. Calcular o valor total em estoque. 
2. Encontrar o produto de maior valor total (quantidade × preço). 
3. Gerar uma lista apenas com os nomes dos produtos com estoque abaixo de 5 
unidades. 
4. Permitir buscar um produto pelo nome e retornar seus dados.'''
import math

estoque = [['arroz',10,25.30], ['café',4,31.9], ['feijão',3,4.99], ['sabonete',45,1.99]]

def calcular_valor_estoque():

    total = 0
    for prod in estoque:
        total += prod[1] * prod[2]
    return total

def prod_mais_valioso():

    maior_valor = 0
    produto_valioso = None    
    for prod in estoque:
        valor = prod[1] * prod[2]
        if valor > maior_valor:
            maior_valor = valor
            produto_valioso = prod
    return produto_valioso

def prod_estoque_baixo():
    lista_prod_baixo = []
    for prod in estoque:
        if prod[1] < 5:
            lista_prod_baixo.append(prod[0])
    return lista_prod_baixo

def busca_nome():

    busca = input("Digite o nome do item para consultar estoque: ").lower()
    for prod in estoque:
        if prod[0].lower() == busca:
            print(f"O item {prod[0]} se enconta em estoque: Quantidade = {prod[1]}, Preço = {prod[2]}  ")
            return
        
    print("O produto não se encontra em estoque")

print(f"O valor total em estoque é de R${calcular_valor_estoque():.2f}")

prod = prod_mais_valioso()
if prod:
    print(f"Produto mais valioso: {prod[0].capitalize()} (Quantidade: {prod[1]}, Preço unitário: R${prod[2]:.2f})")

print(f"Produtos com estoque abaixo de 5 unidades: {prod_estoque_baixo()}")

busca_nome()