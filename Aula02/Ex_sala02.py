'''Faça um programa que: 
1. Permita ao usuário adicionar itens a uma lista de compras. 
2. Caso o usuário digite "sair", o programa encerra. 
3. Mostre a lista final de compras organizada em ordem alfabética.'''

lista_compras = []

def receber_lista():
    while True:

        itens = str(input("Digite o iten da compra para adicionar à lista ou digite 'sair' para parar:  "))
       
        lista_compras.append(itens)
        

        if itens == "sair":
            break
            
    lista_compras.sort()



receber_lista()

print(lista_compras)
