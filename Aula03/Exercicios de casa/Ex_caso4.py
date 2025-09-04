# Considere as atividades da Lista 2(aula anterior)

# Caso4: Análise de Vendas Mensais

# Implemente os códigos usando Dicionários

'''Caso4: Análise de Vendas Mensais 
Uma loja online registra o número de vendas de cada dia do mês em uma lista. 
• Exemplo: [10, 15, 20, 5, 0, 8, ...] 
O gerente precisa: 
1. Calcular o total de vendas no mês. 
2. Descobrir o dia com mais vendas e o dia com menos vendas. 
3. Calcular a média de vendas por dia. 
4. Listar os dias que tiveram vendas acima da média. 
'''

vendas_lista = [10, 15, 20, 5, 0, 8, 12, 18, 7, 14,
          9, 21, 25, 30, 17, 11, 6, 4, 13, 19,
          22, 16, 8, 5, 10, 27, 14, 9, 20, 23]

vendas_dicionario = {}

for i, valor in enumerate(vendas_lista):
    dia = "dia" + str(i+1)
    vendas_dicionario[dia] = valor



def calculo_vendas():
    
    total = 0
 
    for i in vendas_dicionario.values():
        total += i 

    mais_venda = max(vendas_dicionario, key=vendas_dicionario.get)
    menos_venda = min(vendas_dicionario, key=vendas_dicionario.get)
    media = total / len(vendas_dicionario)

    

   

    dias_acima_media = []
    for dia, valor in vendas_dicionario.items():
        if valor > media:
            dias_acima_media.append(dia)

    print(f"Total de vendas no mês {total}")
    print(f"O dia com mais vendas - {mais_venda}")
    print(f"O dia com menos vendas - {menos_venda}")
    print(f"A média de vendas no mês foi de {media}")
    print(f"Dias acima da media -  {dias_acima_media}")

calculo_vendas()