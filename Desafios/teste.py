tabuleiro = []

for i in range(5):
    linha = []
    for j in range(5):
        linha.append('~')  # você pode colocar qualquer valor inicial, como 0, "-", ou " "
    tabuleiro.append(linha)

# Exibir o tabuleiro


tabuleiro[2][2] = "x"

for linha in tabuleiro:
    print(linha)