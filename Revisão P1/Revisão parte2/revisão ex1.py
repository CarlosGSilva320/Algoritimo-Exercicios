alunos = []

def cadastrar_alunos(lista, nome, matricula):
    aluno = {
        "nome": nome,
        "matricula": matricula,
        "notas" : []
    }
    lista.append(aluno)

def inserir_notas(lista, matricula, notas):
    for aluno in lista:
        if aluno["matricula"] == matricula:
            aluno["notas"] = notas
            return True
    return False

def calcular_media(notas):
    if len(notas)  == 0:
        return 0
    else:
        return sum(notas) / len(notas)


def relatorio_alunos(lista):
    for aluno in lista:
        media = calcular_media(aluno["notas"])
        if media >= 7:
            situacao = "aprovado"
        else:
            situacao = "reprovado"
        print(f"nome: {aluno['nome']}, matricula: {aluno['matricula']}")
        print(f"notas: {aluno['notas']}, media: {media}, Situação: {situacao}")




cadastrar_alunos(alunos, "giuliano", 121606)

inserir_notas(alunos, 121606, [9.1, 5.0, 0.0])

relatorio_alunos(alunos)