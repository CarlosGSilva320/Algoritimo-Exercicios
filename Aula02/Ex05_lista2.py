#Caso 5: Controle de Participação em um Evento 
'''Os organizadores de um evento registraram os nomes dos participantes de cada atividade em 
listas separadas. 
• Exemplo: 
o Palestra: ["Ana", "Carlos", "Marina"] 
o Workshop: ["Carlos", "João", "Ana"] 
o Mesa-redonda: ["Marina", "João", "Paula"] 
Eles precisam: 
1. Saber quem participou de todas as atividades. 
2. Saber quem participou de apenas uma atividade. 
3. Gerar uma lista com todos os nomes únicos dos participantes. 
4. Contar quantos participantes distintos houve no evento.'''

Palestra = ["Ana", "Carlos", "Marina"] 
Workshop = ["Carlos", "João", "Ana"] 
Mesa_redonda = ["Marina", "João", "Paula", "Carlos", "Ana"]

def analisar_presença():

    todos_partcipantes = set(Palestra + Workshop + Mesa_redonda)

    presente_todos = set(Palestra) & set(Workshop) & set(Mesa_redonda)

    apenas_uma = []
    for pessoa in todos_partcipantes:
        contador = 0
        if pessoa in Palestra:
            contador += 1
        if pessoa in Workshop:
            contador += 1
        if pessoa in Mesa_redonda:
            contador += 1
        if contador == 1:
            apenas_uma.append(pessoa)
    if presente_todos:
        print(f"Participou de todas: {presente_todos}")
    else:
        print("Ninguém participou de todos os eventos.")
    print(f"Participou de apenas 1 atividade: {apenas_uma}")
    print(f"Nome dos participantes: {todos_partcipantes}")
    print(f"Forma {len(todos_partcipantes)} participantes no total")

analisar_presença()