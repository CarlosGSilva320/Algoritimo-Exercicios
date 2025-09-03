'''Caso1: Controle de Presença em Sala de Aula 
Uma professora precisa registrar a presença dos alunos durante a semana. 
• Cada dia da semana terá uma lista com os nomes dos presentes. 
• No final, ela precisa: 
1. Saber quais alunos estiveram presentes todos os dias. 
2. Saber quais alunos faltaram em pelo menos um dia. 
3. Saber o número total de presenças por aluno.'''


def receber_alunos():
    
    segunda = input("Digite os alunos presentes na segunda separados por virgula: ").split(",")
    terça = input("Digite os alunos presentes na terça separados por virgula: ").split(",")
    quarta = input("Digite os alunos presentes na quarta separados por virgula: ").split(",")  
    quinta = input("Digite os alunos presentes na quinta separados por virgula: ").split(",")
    sexta = input("Digite os alunos presentes na sexta separados por virgula: ").split(",")

    segunda = [aluno.strip().lower() for aluno in segunda]
    terça = [aluno.strip().lower() for aluno in terça]
    quarta = [aluno.strip().lower() for aluno in quarta]
    quinta = [aluno.strip().lower() for aluno in quinta]
    sexta = [aluno.strip().lower() for aluno in sexta]

    return segunda, terça, quarta, quinta, sexta

def analisar_presença(segunda, terça, quarta, quinta, sexta):

    todos_alunos = set(segunda + terça + quarta + quinta + sexta)

    presente_todos = set(segunda) & set(terça) & set(quarta) & set(quinta) & set(sexta)

    faltaram = todos_alunos - presente_todos

    total_presenças = {aluno: 0 for aluno in todos_alunos}
    for lista in [segunda, terça, quarta, quinta, sexta]:
        for aluno in lista:
            total_presenças[aluno] += 1

    print("\n--- RELATÓRIO FINAL ---")
    print(f"Alunos presentes todos os dias: {presente_todos if presente_todos else 'Nenhum'}")
    print(f"Alunos que faltaram em pelo menos um dia: {faltaram if faltaram else 'Nenhum'}")

    print("\nTotal de presenças por aluno:")
    for aluno, qtd in total_presenças.items():
        print(f"{aluno.capitalize()}: {qtd}")

segunda, terca, quarta, quinta, sexta = receber_alunos()
analisar_presença(segunda, terca, quarta, quinta, sexta)
