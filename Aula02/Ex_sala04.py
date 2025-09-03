'''Imagine que você trabalha em uma loja de eletrônicos que precisa organizar melhor o registro 
diário de vendas. Até então, os vendedores anotavam em papel ou planilhas, mas o dono pediu 
para criar um programa simples em Python para armazenar, analisar e gerar pequenos 
relatórios sobre as vendas do dia. 
O sistema precisa: 
1. Guardar os produtos vendidos (nome e preço). 
2. Mostrar o valor total arrecadado. 
3. Identificar o produto mais caro e o mais barato do dia. 
4. Permitir consultar se um produto específico foi vendido.'''

produto = []
preco = []

def receber_compra():

    while True:
        compra = input("Digite o nome do produto vendido ou 'sair' para parar: ").lower()

        if compra == "sair":
            break
        
        produto.append(compra)
        
        preco1 = float(input("Digite o preço do produto R$ "))

        preco.append(preco1)

receber_compra()

total = sum(preco)

preco_caro = max(preco)
preco_barato = min(preco)

produto_caro = produto[preco.index(preco_caro)]
produto_barato = produto[preco.index(preco_barato)]

print(f"O valor total arrecadado é de R${total:.2f}")
print(f"O produto mais caro custa R${preco_caro}")
print(f"O produto mais barato custa R${preco_barato:.2f}")

def consultar_produto():
    while True:
        consulta = input("Consulte se o produto foi vendido ou escreva 'sair' para parar: ").lower()

        if consulta == 'sair':
            break

        if consulta in produto:
            print(f"O produto {consulta} foi vendido.")
        
        else:
            print(f"O produto {consulta} não foi vendido.")

consultar_produto()