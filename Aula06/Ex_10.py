# Contexto: Uma estação meteorológica registra chuva em 7 dias, para 3 cidades. 
'''Tarefa: Crie uma matriz 3x7 com os valores de chuva (mm) e determine qual cidade teve mais 
chuva na semana.'''

cidade = 2
dias = 3

lista =[]

for i in range(cidade):
    dia = []
    for j in range(dias):
        dia.append(float(input(f"Digite a quantidade do {j + 1}° dia da {i + 1}° Cidade: ")))
    lista.append(dia)

soma_maior = 0
indice = 0
for i, j in enumerate(lista):
    soma = sum(j)
    if soma > soma_maior:
        soma_maior = soma
        indice = i + 1

print(lista)        
print(f"A Cidade: {indice} teve {soma_maior}mm de chuva na semana.")
