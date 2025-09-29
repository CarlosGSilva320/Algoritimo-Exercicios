#Você foi contratado para criar um sistema simples de gestão acadêmica em Python. 
#O sistema deverá: 
#=>  1. Cadastrar alunos em uma lista de dicionários, onde cada aluno tem: 
'''o Nome 
o Matrícula 
o Notas (lista de 3 avaliações)'''

# => 2. Criar funções para: 
'''o cadastrar_aluno(lista_alunos, nome, matricula)                                                
adiciona um novo aluno ao sistema. 

o inserir_notas(lista_alunos, matricula, notas)                                                      
adiciona as notas a um aluno específico. 

o calcular_media(notas)                                                                                              
retorna a média aritmética das notas. 

o relatorio_alunos(lista_alunos)                                                                                   
exibe todos os alunos com suas notas e médias. 
'''
#3. O sistema deve permitir gerar um relatório final, mostrando: 

'''o Nome do aluno 
o Matrícula 
o Notas 
o Média 
o Situação (Aprovado se média ≥ 7.0, caso contrário Reprovado).'''

lista_alunos = []

def cadastrar_aluno(lista_alunos, nome, matricula):

    aluno = {"nome" : nome,
             "matricula" : matricula,
             "notas" : [] 
    }

    lista_alunos.append(aluno)

def inserir_notas(lista_alunos, matricula, notas):
    
    for aluno in lista_alunos:
        if aluno['matricula'] == matricula:
            aluno['notas'] = notas
            return True
    return False


def calcular_media(notas):
    if len(notas) == 0:
        return 0
    else:
        return sum(notas) / len(notas)

def relatorio_alunos(lista_alunos):
    for aluno in lista_alunos:
        media = calcular_media(aluno["notas"])
        if media > 7:
            situação = 'Aprovado'
        else:
            situação = 'Reprovado'
        print(f"Aluno: {aluno['nome']}, Matrícula: {aluno['matricula']}, Notas: {aluno['notas']} ")
        print(f"Média: {media:.1f}, Situação: {situação} ")    






cadastrar_aluno(lista_alunos, "Carlos", 13060)
cadastrar_aluno(lista_alunos, "Meiry", 13061)

inserir_notas(lista_alunos, 13060, [9.0, 7.0, 6.0])
inserir_notas(lista_alunos, 13061, [10.0, 0.0, 0.0])


relatorio_alunos(lista_alunos)






















'''alunos = []

def cadastrar_aluno(lista_alunos, nome, matricula):
    aluno = {
            "nome": nome,
            "matricula" : matricula,
            "notas" : []
    }
    lista_alunos.append(aluno)

def inserir_notas(lista_alunos, matricula, notas):
    for aluno in lista_alunos:
        if aluno["matricula"] == matricula:
            aluno["notas"] = notas
            return True
    return False

def calcular_media(notas):
    if len(notas) == 0:
        return 0
    else:
        return sum(notas) / len(notas)

def relatorio_alunos(lista_alunos):
    for aluno in lista_alunos:
        media = calcular_media(aluno["notas"])
        if media >= 7:
            situação = "aprovado"
        else:
            situação = "reprovado"
        print(f"Aluno: {aluno["nome"]}, Matrícula: {aluno["matricula"]}, Notas: {aluno["notas"]}")
        print(f"Média: {media:.2f}, situação: {situação}")






cadastrar_aluno(alunos, "carlos", 13060)
inserir_notas(alunos, 13060, [9.0, 7.0, 6.0])
relatorio_alunos(alunos)'''