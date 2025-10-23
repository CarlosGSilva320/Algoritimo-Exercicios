#2. Grade de Notas de Alunos 
'''Contexto: Uma turma de 4 alunos realizou 3 provas. 
Tarefa: Armazene as notas em uma matriz 4x3 e calcule a média de cada aluno e a média de 
cada prova.'''

alunos = 4
provas = 3

lista = []

for i in range(alunos):
    nota = []
    for j in range(provas):
        nota.append(float(input(f"Digite a {j + 1}° nota do {i + 1}° aluno: ")))

    lista.append(nota)

for aluno, notas in enumerate(lista):
    media = sum(notas) / len(notas)
    print(f"A média do {aluno + 1}° aluno é igual a {media} ")

for prova in range(provas):
    soma_prova = 0
    for aluno in range(alunos):
        soma_prova += lista[aluno][prova]
    media = soma_prova / alunos
    print(f"A média da prova {prova + 1} é {media}")


print(lista)