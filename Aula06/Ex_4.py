# 4. Controle de Estoque:
'''Contexto: Uma loja possui 4 produtos e verifica o estoque em 3 lojas diferentes. 
Tarefa: Crie uma matriz 4x3 com as quantidades de cada produto em cada loja e calcule o total 
de cada produto.'''

produtos = 4
lojas = 3

lista = []

for i in range(produtos):
    loja = []
    for j in range(lojas):
        loja.append(int(input(f"Digite a quantidade do {i + 1}° produto da {j + 1}° loja: ")))
    lista.append(loja)

for produto in range(produtos):
    soma_produto = 0
    for loja in range(lojas):
        soma_produto += lista[produto][loja]
    print(f"O {produto + 1}° tem {soma_produto} no total")

print(lista)