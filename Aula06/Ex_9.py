# 9. Planejamento de Exercícios 
'''Contexto: Uma academia planeja 3 tipos de exercícios para 4 alunos diferentes. 
Tarefa: Crie uma matriz 4x3 que registre quantas repetições cada aluno deve fazer e calcule o 
total de repetições de cada exercício.'''


alunos = 2
exercicios = 2

lista = []

for i in range(alunos):
    exercicio = []
    for j in range(exercicios):
        exercicio.append(int(input(f"Repetição exercicio {j + 1} do Aluno {i + 1}: ")))
    lista.append(exercicio)

total_repetição = []

for i in range(alunos):
    soma = 0
    for j in range(exercicios):
        soma += lista[i][j]
    total_repetição.append(soma)

for i, j in enumerate(total_repetição):
    print(f"O {i + 1}° Exercicio teve {j} repetições")

