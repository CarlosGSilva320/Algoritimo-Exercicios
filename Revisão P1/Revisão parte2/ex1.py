alunos = []

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
relatorio_alunos(alunos)