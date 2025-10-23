# 1. Controle de Temperatura de Salas 
'''Contexto: Uma empresa monitora a temperatura de 5 salas, 3 vezes ao dia. 
Tarefa: Armazene as temperaturas em uma matriz 5x3. Calcule a temperatura média de cada 
sala.'''

salas = 5
temperaturas = 3

lista = []

for i in range(salas):
    sala = []
    for j in range(temperaturas):
        sala.append(float(input(f"Digite a {j + 1}° temperatura da {i + 1}° sala: ")))
    lista.append(sala)

for indice, temperatura  in enumerate(lista):
    media = sum(temperatura) / len(temperatura)
    print(f"A média da sala {indice + 1} é {media}°")
print(lista)