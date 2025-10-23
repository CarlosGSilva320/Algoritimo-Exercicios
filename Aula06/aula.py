
'''l = int(input(" E n t r e com o número de l in h a s : "))
c = int(input(" E n t r e com o número de col una s : "))
matriz = []
for i in range(l):
    linha = []
    for j in range(c) :
        linha.append(int(input("Entre com um valor"))) # recebendo os dados
    matriz.append(linha)
print(matriz)'''


# 1. Controle de Temperatura de Salas
'''Contexto: Uma empresa monitora a temperatura de 5 salas, 3 vezes ao dia.
Tarefa: Armazene as temperaturas em uma matriz 5x3. Calcule a temperatura média de cada
sala.'''

'''l = 5
c = 3
sala = []
for i in range(l):
    linha = []
    for j in range(c):
        linha.append(float(input(f"Entre com um valor para sala N°{i + 1}: "))) # recebendo os dados
    sala.append(linha)
s = 1
for i in sala:

    media = sum(i) / len(i)    
    print(f"A média da sala {s} é {media}° ")
    s += 1
print(sala)'''

# 2. Grade de Notas de Alunos 
'''Contexto: Uma turma de 4 alunos realizou 3 provas. 
Tarefa: Armazene as notas em uma matriz 4x3 e calcule a média de cada aluno e a média de 
cada prova.'''

a = 4
p = 3

lista = []

for i in range(a):
    linha = []
    for j in range(p):
        linha.append(float(input(f"Digite {j+1}° nota do {i+1}° aluno: ")))
    lista.append(linha)

aluno = 1
for i in lista:
    m = sum(i) / len(i)
    print(f"A média do {aluno}° aluno é igual a {m}")
    aluno +=1

for prova in range(a):
    soma_prova = 0
    for aluno in range(p):
        soma_prova += lista[prova][aluno]
    media_prova = soma_prova / 4
    print(f"Prova {prova+1}: {media_prova:.2f}")


