#7. Vendas Semanais 
'''Contexto: Uma cafeteria registra vendas de 5 produtos durante 7 dias. 
Tarefa: Armazene os valores em uma matriz 5x7 e calcule a receita total semanal de cada 
produto.'''

produtos = 5
dias = 7

lista = []

for i in range(produtos):
    dia = []
    for j in range(dias):
        dia.append(int(input(f"Digite a venda do {i + 1}° produto no {j + 1}° dia: ")))
    lista.append(dia)
print(lista)


lista_venda = []

for prod, dias in enumerate(lista):
    total_venda = 0
    total_venda += sum(dias)
    lista_venda.append(total_venda)

    print(f"{prod + 1}° produto: {total_venda} vendas semanais. ")
