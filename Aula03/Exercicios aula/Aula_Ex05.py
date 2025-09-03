'''5. Crie um dicionário chamado turma que contenha dois alunos, cada um com nome
e nota.
Depois, exiba o nome do primeiro aluno e a nota do segundo aluno'''

turma = {
    "aluno1" : {"nome" : "Carlos", "nota" : 8},
    "aluno2" : {"nome" : "Daniel", "nota" : 9}
}

print(f"O nome do primeiro aluno é {turma["aluno1"]["nome"]}")
print(f"A nota do segundo aluno é {turma["aluno2"]["nota"]}")
