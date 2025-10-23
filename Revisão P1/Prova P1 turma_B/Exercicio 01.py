#1.   Crie  um  programa  em  Python  que  utilize  uma  função  chamada 
#calcular_media  para  calcular  a  média  das  notas  de  um  aluno.  O 
#programa deve: 
'''•  Solicitar ao usuário que informe o nome do aluno. 
•  Pedir  que  o  usuário  digite  as  notas  do  aluno,  sendo  obrigatório 
informar pelo menos 5 notas. 
•  Utilizar a função calcular_media, que recebe como parâmetro a lista 
de notas e retorna a média. 
•  Exibir uma mensagem informando se o aluno foi aprovado (média 
maior ou igual a 7) ou reprovado (média menor que 7). 
•  Mostre  na  tela  o  nome  do  aluno,  as  notas  digitadas  e  a  média 
calculada. Crie uma nova lista apenas com os alunos Aprovados.'''


def calcular_media(notas):
    return sum(notas) / len(notas)

alunos_aprovados = []
todos_alunos = []

while True:
    nome_aluno = input("Digite o nome do aluno ou 'sair' para encerrar: ").lower()
    if nome_aluno == 'sair':
        break

    notas = []

    while len(notas) < 5:
        nota = float(input(f"Digite a {len(notas) + 1}° nota: "))
        notas.append(nota)

    media = calcular_media(notas)
    if media >= 7:
        situacao = "aprovado"
        alunos_aprovados.append(nome_aluno)
    else:
        situacao = "reprovado"

    aluno = {
        'nome' : nome_aluno,
        'notas' : notas,
        'media' : media,
        'situação' : situacao
    }
    todos_alunos.append(aluno)


print(todos_alunos)






'''nome = input("Nome do aluno: ")
notas = []
aprovados = []

for i in range(0, 5):
    nota = float(input(f"Digite a {i + 1}° nota: "))
    notas.append(nota)
while True:

    continuar = input("Continuar lançar nota? (S/N) ").lower()
    if continuar == "s":
        notas.append(float(input(f"Digite a {len(notas) + 1}° nota: ")))
        
    else:
        break

    
def calcular_media(notas):
    media = sum(notas) / len(notas)
    if media >= 7:
        situação = 'aprovado'
        aprovados.append(nome)

    else:
        situação = 'reprovado'
    return media, situação

media, situação = calcular_media(notas)
print(f"Nome: {nome}, Notas: {notas}, Média: {media:.2f}, Situação: {situação}")
print(f"Alunos aprovados: {aprovados}")
'''