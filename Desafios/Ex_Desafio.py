import random

linhas = 5
colunas = 5

tabuleiro = []

for i in range(linhas):
    linha = []
    for j in range(colunas):
        linha.append('~')
    tabuleiro.append(linha)

l = random.randint(0, 4)
c = random.randint(0, 4)


print("<=-=-Caça ao Tesouro-=-=>\n")
for i in tabuleiro:
    print(f"{i}")

def dica_posicao(escolha_linha, escolha_coluna, l, r):
    if escolha_linha > l:
        print("Dica: Está mais para cima.")
    elif escolha_linha < l:
        print("Dica: Está mais para baixo.")
    if escolha_coluna > c:
        print("Diuca: Está mais para esquerda.")
    elif escolha_coluna <c:
        print("Dica: Está mais para direita.")


tentativas = 0
while tentativas <= 6:

    print("Escolha a linha (0 até 4) e a coluna (0 até 4) !")
    print(f"=-{tentativas + 1}° Tentativa-= ")
    while True:
        try:
            escolha_linha = int(input("Qual Linha ? ->"))
            escolha_coluna = int(input("Qual Coluna ? ->"))

            if  0 <= escolha_linha <= 4 and 0 <= escolha_coluna <= 4:
                break
            else:
                print("Valores inválidos, escolha entre(0 e 4) !")
        except ValueError:
                print("Entrada inválida!")


    if escolha_linha == l and escolha_coluna == c:
        tabuleiro[l][c] = "T"
        print("\n<=-=-Caça ao Tesouro-=-=>\n")
        for i in tabuleiro:
            print(f"{i}")
        print("Vitória, você encontrou o Tesouro !!!")
        break
    else:        
        tabuleiro[escolha_linha][escolha_coluna] = "X"
        tentativas += 1
        if tentativas == 6:
            tabuleiro[l][c] = "T"
            print("\n<=-=-Caça ao Tesouro-=-=>\n")
            for i in tabuleiro:
                print(f"{i}")
                print("Você perdeu!!!")
        else:
            print("\n<=-=-Caça ao Tesouro-=-=>\n")
            for i in tabuleiro:
                print(f"{i}")
            dica_posicao(escolha_linha, escolha_coluna, l, c)
            




     
    


