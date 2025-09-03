'''3. Estatísticas de Notas 
Leia as notas de uma turma e: 
• Calcule a média; 
• Mostre a maior e a menor nota; 
• Exiba o percentual de alunos acima da média. '''

notas = []
qtd = int(input("Quantos aulnos tem na turma? "))

for i in range(qtd):
    nota = float(input(f"Digite a nota do {i + 1} aluno: "))
    notas.append(nota)

media = sum(notas) / len(notas)
maior = max(notas)
menor = min(notas)

acima_media = sum(1 for n in notas if n > media)
percentual = (acima_media / len(notas)) * 100

print(f"Média da turma {media}")
print(f"A maior é {maior} e a menor {menor}")
print(f"O percentual de notas acima da média foi de {percentual:.2f}%")