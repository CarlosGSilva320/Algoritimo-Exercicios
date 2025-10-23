#3. Agenda Semanal 
'''Contexto: Um consultório possui 5 dias de atendimento e 3 horários por dia. 
Tarefa: Armazene os nomes dos pacientes em uma matriz 5x3 e exiba a agenda completa.'''


dias = 5
hs = 3

lista = []

for dia in range(dias):
    pacientes = []
    for paciente in range(hs):
        pacientes.append(input(f"Digite o nome do {paciente + 1}° paciente do {dia + 1}° dia: "))
    
    lista.append(pacientes)

print("=============== Agenda Semanal =================")

for dia, pacientes in enumerate(lista):
    print(f"\nDia {dia + 1}:")
    for horario, nome in enumerate(pacientes):
        print(f"Horário {horario + 1}: {nome}")