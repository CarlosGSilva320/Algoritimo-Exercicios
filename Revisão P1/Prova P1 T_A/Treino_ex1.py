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
        nota = float(input(f"digite a {i + 1}° nota: "))
        notas.append(nota)

while True:
        continuar = input("Desja acrescentar mais uma nota? (S/N):").lower()        
        if continuar == "s":
            nota = float(input(f"Digite a {len(notas)+1}° nota:"))
            notas.append(nota)
        else:
            break
       

def calcular_media_notas(notas):
    media = sum(notas) / len(notas)
    if media >= 7:
        situacao = 'aprovado'
    else:
        situacao = 'reprovado'

    return media, situacao

media, situacao = calcular_media_notas(notas)
print(f"Aluno: {nome}, Média: {media:.1f}, Notas: {notas}, Situação: {situacao}")
