# Estudo de Caso 2: Agenda Telefônica 

'''Uma agenda pode ser representada como um dicionário em que as chaves são os nomes 
das pessoas e os valores são os números de telefone. 
Exemplo: 
agenda = {"Maria": "99999-1234", "João": "98888-5678"} 
print("Telefone da Maria:", agenda["Maria"])'''

agenda = {}

def salvar_agenda():

    while True:

        nome = input("Digite o nome para salvar ou sair para parar: ").lower()

        if nome == "sair":
            break

        num = input("Digite o numero: ")

        agenda[nome] = num
    print(agenda)

salvar_agenda()
