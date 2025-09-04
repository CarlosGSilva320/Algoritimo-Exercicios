#Estudo de Caso : Cadastro de Produtos 

'''Um supermercado deseja armazenar informações sobre seus produtos. Cada produto deve 
conter: nome, preço e quantidade em estoque. Utilize um dicionário para representar e 
manipular essas informações. 
Exemplo: 
produto = {"nome": "Arroz", "preco": 25.90, "estoque": 100} 


print(f"O produto {produto["nome"]} custa R${produto["preco"]}")'''


produto = {}

def cadastrar_produto():
    while True:
        nome = input("Digite o nome do produto para cadastrar ou 'sair para parar: ").lower()
        if nome == "sair":
            break
        preço = float(input("Digite o preço R$"))
        quantidade = int(input("Digite a quantidade em estoque: "))

        produto[nome] = {"preço" : preço, "quantidade" : quantidade}


def mostar_produtos():
    for nome, dados in produto.items():
        print(f"{nome.capitalize()} custa R${dados["preço"]:.2f} com {dados["quantidade"]} unidades em estoque.")

def valor_total():
    total = 0
    for valor in produto.values():
        total += valor["preço"] * valor["quantidade"]
    print(f"O valor total em estoque é de R${total:.2f}")

def busca_produto():

    busca = input("Digite o nome do produto para buscar no estoque: ")

    if busca in produto:
        print(f"{busca.capitalize()} - R${produto[busca]["preço"]} - {produto[busca]["quantidade"]} unidades em estoque ").lower()
    else:
        print("O produto está sem estoque!")


cadastrar_produto()
mostar_produtos()
valor_total()  
busca_produto()