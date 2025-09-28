'''1.   Escreva  um  programa  em  Python  que  tenha  uma  função  chamada 
calcular_media_notas. Esta função deve receber uma lista de notas de um aluno 
e calcular a média dessas notas. O programa principal deve:  
(A).  Solicitar ao usuário que informe o nome do aluno. 
(B).  Solicitar ao usuário que informe as notas do aluno (o número de 
notas  pode  ser  variável,  mas  o  programa  deve  permitir  que  o  usuário 
adicione pelo menos 5 notas). 
(C).  Chamar a função calcular_media_notas passando a lista de notas 
e exibir a média das notas. 
(D).  Caso a média seja superior ou igual a 7, exibir que o aluno foi 
aprovado. Caso contrário, exibir que o aluno foi reprovado.'''


nome = input("Digite o nome do aluno: ")
notas = []
for i in range(0, 5):
    nota = float(input(f"Digite a {i +1}° nota: "))
    notas.append(nota)

def calcular_media_notas():
    
    situação = ""

    media = sum(notas) / len(notas)
    if media >= 7:
        situação = "Aprovado"
    else:
        situação = "Reprovado"
    return situação

situação = calcular_media_notas()
print(f"O aluno {nome} tem as notas {notas} e está {situação}")