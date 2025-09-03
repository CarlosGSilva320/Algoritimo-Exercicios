'''Caso2: Distâncias em Km 
1. Receba as distâncias percorridas em 6 viagens e armazene em uma lista. 
2. Calcule a distância total percorrida. 
3. Mostre a maior e a menor distância. 
4. Calcule a média das distâncias arredondada para cima (use math.ceil).'''
import math

km_viagem = []

def receber_km():

    for i in range(6):
        km = float(input(f"Digite o km do da viagem {i +1}:  "))
        km_viagem.append(km)
    
def analisar_viagem():

    total_km = sum(km_viagem)
    maior_km = max(km_viagem)
    menor_km = min(km_viagem)

    media = math.ceil(total_km / len(km_viagem))

    print(f"O total percorrido foi de {total_km}km")
    print(f"A viagem mais longa foi de {maior_km}km")
    print(f"A viagem mais curta foi de {menor_km}km")
    print(f"A média das distâncias é de {media}km")

receber_km()
analisar_viagem()



