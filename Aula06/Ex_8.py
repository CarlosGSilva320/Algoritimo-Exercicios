# 8. Distribuição de Cadeiras 
'''Contexto: Uma sala de cinema tem 5 filas com 6 cadeiras cada. 
Tarefa: Crie uma matriz 5x6 e marque quais cadeiras estão ocupadas com “X” e quais estão 
livres com “O”.'''

filas = 2
cadeiras = 3
lista = []
for i in range(filas):
    cadeira = []
    for j in range(cadeiras):
        cadeira.append(input(f"Digite letra 'O' para vaiza e letra 'X' para ocupada -> Fila: {i+1} -> cadeira: {j+1} ->  ").upper())
    lista.append(cadeira)
for i, j in enumerate(lista):
    print(f"Fila {i + 1}: {j}")