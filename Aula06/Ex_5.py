# 5. Registro de Pontos em Jogos 
'''Contexto: Uma liga de esportes registra pontos de 3 times em 4 jogos. 
Tarefa: Crie uma matriz 3x4 com os pontos e determine qual time teve maior pontuação total.'''

times = 3
jogos = 4

lista = []

for i in range(times):
    time = []
    for j in range(jogos):
        time.append(float(input(f"Digite a {j + 1}° pontuação do {i + 1}° time:  ")))
    lista.append(time)

time_vencedor = 0
maior_total = 0 
for time, pontos in  enumerate(lista):
    soma = sum(pontos)

    if soma > maior_total:
        maior_total = soma
        time_vencedor = time + 1

print(f"O time vencedor foi o {time_vencedor}° com pontuação de {maior_total}!")