'''Crie um programa que: 
1. Receba as temperaturas de 7 dias e armazene em uma lista. 
2. Mostre a média das temperaturas da semana. 
3. Informe o dia mais quente e o dia mais frio. 
4. Mostre quantos dias ficaram acima da média.'''


temperatura_semana = []
dias = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sabado", "Domingo"]

def receber_temperatura():
   

    for i in dias:
        
        temperatura_digitada = float(input(f"Digite a temperartura para {i}: "))
        temperatura_semana.append(temperatura_digitada)
    
    return temperatura_semana, dias

def analisar_temperaturas(temperaturas_semana, dias):

    media = sum(temperatura_semana) / len(temperatura_semana)

    maior = max(temperatura_semana)

    menor = min(temperatura_semana)

    dia_quente = dias[temperatura_semana.index(maior)]
    dia_frio = dias[temperatura_semana.index(menor)]

    dias_acima_media = 0

    for t in temperatura_semana:
        if t > media:
            dias_acima_media += 1


    print(f"A média de temperatura da semana é de {media:.2f} graus")
    print(f"O dia mais quente é {dia_quente} e o mais frio {dia_frio}.")
    print(f"{dias_acima_media} dias ficaram acima da média.")



temperatura_semana, dias = receber_temperatura()
analisar_temperaturas(temperatura_semana, dias)