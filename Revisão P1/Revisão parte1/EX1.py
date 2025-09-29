pedidos = [
{
        "cliente": "Bruno",
        "itens": [
            {"prato": "Lasanha", "preco": 30},
            {"prato": "Suco de Laranja", "preco": 8}
        ]
},
{
        "cliente": "Ana",
        "itens": [
            {"prato": "Pizza", "preco": 40},
            {"prato": "Refrigerante", "preco": 6},
            {"prato": "Sobremesa", "preco": 12}
        ]
},
{
        "cliente": "Carla",
        "itens": [
            {"prato": "Pizza", "preco": 40},
            {"prato": "Suco de Laranja", "preco": 8}
        ]
}
]


#1. Crie uma função que receba o nome de um cliente e retorne o valor total gasto (somando todos os itens pedidos)

def valor_total(nome):
  
    total = 0
    for pedido in pedidos:
        if pedido["cliente"] == nome:
            for i in pedido["itens"]:
                total = total + i["preco"]
    return total
resultado = valor_total("Carla")
print(f"O valor gasto foi de R${resultado:.2f}")
    

#2. Crie uma função que descubra qual prato foi o mais vendido no dia.

def prato_mais_vendido():

    contagem = {}

    for p in pedidos:
        for i in p["itens"]:
            prato = i["prato"]
            if prato in contagem:
                contagem[prato] += 1
            else:
                contagem[prato] = 1
    
    maior_vendas = 0

    for q in contagem.values():
        if q > maior_vendas:
            maior_vendas = q

    mais_vendidos = []
    for p, q in contagem.items():
        if q == maior_vendas:
            mais_vendidos.append(p)

    return contagem, mais_vendidos, maior_vendas
contagem, mais_vendidos, maior_vendas = prato_mais_vendido()
print("Contagem de pratos:", contagem)
print("Prato(s) mais vendido(s):", mais_vendidos, f"({maior_vendas} vendas)")

#3. Mostre um ranking com os 3 clientes que mais gastaram, em ordem decrescente. 

#def ranking():

def ranking(): 

    gastos = {}

    for pedido in pedidos:
        cliente = pedido["cliente"]
        total = 0
        for item in pedido["itens"]:
            total += item["preco"]
        gastos[cliente] = total
    
    return sorted(gastos.items(), key=lambda x: x[1], reverse=True)

top_ranking = ranking()
print(top_ranking)
#print(sorted(gastos.items(), key=lambda x: x[1], reverse=True))