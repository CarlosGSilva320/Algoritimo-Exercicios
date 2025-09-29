pedidos = [
{
        "cliente": "Ana",
        "itens": [
            {"prato": "Lasanha", "preco": 30},
            {"prato": "Suco de Laranja", "preco": 8}
        ]
},
{
        "cliente": "Bruno",
        "itens": [
            {"prato": "Pizza", "preco": 40},
            {"prato": "Refrigerante", "preco": 6},
            {"prato": "Sobremesa", "preco": 12}
        ]
},
{
        "cliente": "Carla",
        "itens": [
            {"prato": "Lasanha", "preco": 30},
            {"prato": "Suco de Laranja", "preco": 8}
        ]
}
]

#Crie uma função que receba o nome de um cliente e retorne o valor total gasto (somando
# todos os itens pedidos)
def gastos(nome):
    total = 0
    for pedido in pedidos:
        if pedido["cliente"] == nome:
            for item in pedido["itens"]:
                total = total + item["preco"]
    return total



def mais_vendido():
    contagem_pratos = {}
    for pedido in pedidos:
        for item in pedido["itens"]:
            prato = item["prato"]
            if prato in contagem_pratos:
                contagem_pratos[prato] +=1
            else:
                contagem_pratos = 1
    mais_vendidos = ""
    maior_quantidade = 0

    for prato in contagem_pratos:
        if contagem_pratos[prato] > maior_quantidade:
            mais_vendido = prato
            maior_quantidade = contagem_pratos[prato]
            
    return f'O prato mais vendido foi "{mais_vendido}", com {maior_quantidade} vendas.' 
            
                




resultado = gastos("carlos")

print(resultado)