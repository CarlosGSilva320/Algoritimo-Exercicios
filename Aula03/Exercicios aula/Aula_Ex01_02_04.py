#1. Crie um dicionário chamado aluno com as chaves "nome", "idade" e "curso".Em seguida, exiba apenas o nome do aluno.'''

aluno = {
    "nome" : "Carlos",
    "idade" : 44,
    "curso" : "Engenharia"
}
print(f"O nome do aluno é {aluno["nome"]}")

#2. Adicione uma nova chave "nota" com valor 9.5 ao dicionário aluno. Depois, remova a chave "idade".

aluno["nota"]=9.5

#4. Dado o dicionário aluno, verifique se existe a chave "curso".

if "curso" in aluno.keys():    
    print("A informações de curso constam no dicionário")
else:
    print("A informações de curso não constam no dicionário")
    
