'''Caso4: Análise de Vendas Mensais 
Uma loja online registra o número de vendas de cada dia do mês em uma lista. 
• Exemplo: [10, 15, 20, 5, 0, 8, ...] 
O gerente precisa: 
1. Calcular o total de vendas no mês. 
2. Descobrir o dia com mais vendas e o dia com menos vendas. 
3. Calcular a média de vendas por dia. 
4. Listar os dias que tiveram vendas acima da média. 
'''

vendas = [10, 15, 20, 5, 0, 8, 12, 18, 7, 14,
          9, 21, 25, 30, 17, 11, 6, 4, 13, 19,
          22, 16, 8, 5, 10, 27, 14, 9, 20, 23]

def analise_vendas():
    dias_acima_media = []
    total = sum(vendas)    
    maior = max(vendas)
    menor = min(vendas)
    media = total / len(vendas)
    for dia, vendas_dia in enumerate(vendas, start=1):
        if vendas_dia > media:
            dias_acima_media.append(dia)
    

    print(f"O total de vendas no mês é {total}")
    print(f"O dia {vendas.index(maior) + 1} teve {maior} vendas, sendo o maior do mês.")
    print(f"O dia {vendas.index(menor) + 1} teve {menor} vendas, sendo o menor do mês.")
    print(f"A média de vendas no mês foi de {media:.2f} por dia.")
    print(f"Os dias: {dias_acima_media} tiveram vendas acima da média")
analise_vendas()