#6. Horários de Transporte 
'''Contexto: Um ponto de ônibus tem 4 linhas, cada uma com 3 horários. 
Tarefa: Armazene os horários em uma matriz 4x3 e permita que o usuário consulte os horários 
de uma linha específica.'''


linhas = 4
horarios = 3

lista = []

for i in range(linhas):
    linha = []
    for j in range(horarios):
        linha.append(int(input(f"Digite o {j + 1}° horário da {i + 1}° Linha de ônibus: ")))
    lista.append(linha)

while True:
    
    escolha = int(input("Escolha um linha de '1' a '4' ou '0' para parar: "))

    if escolha == 0:       
        break

    elif 1 <= escolha <= 4:
        print(f"Linha {escolha}: Horários: {lista[escolha - 1]}")

        
    