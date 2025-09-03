'''4. Busca Linear 
Dada uma lista de nomes, implemente uma função que busque um nome digitado pelo usuário. 
Informe a posição em que ele aparece ou diga que não foi encontrado. '''



def busca_linear(lista, alvo):
    for i in range(len(lista)):
        if lista[i] == alvo:
            return i
    return -1

nomes = ['carlos', 'feli', 'vinicius', 'caio']
busca = input("Digite o nome para busca: ")

posição = busca_linear(nomes, busca)
if posição != -1:
    print(f"Nome encontrado na posição {posição}")
else:
    print("Nome não encontrado.")