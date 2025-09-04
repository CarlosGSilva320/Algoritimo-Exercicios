#6 -
#b) Crie um dicionário de notas de 3 alunos (nome como chave, nota como valor). 
#c) Acesse a nota de um dos alunos e exiba. 
#d) Remova um aluno do dicionário de notas.


turma = {
    "aluno1" : {"carlos" : 10},
    "aluno2" : {"allan": 9},
    "aluno3" : {"daniel": 8}

}

print(turma["aluno1"]["carlos"])
turma.pop("aluno2")


print(turma)