# Dicionário principal
dicionario = {}

def cadastrar_funcionario(nome, salario, cargo):
    dicionario[nome] = {"salario": salario, "cargo": cargo}

def consultar_funcionario(nome):
    if nome in dicionario:
        funcionario = dicionario[nome]
        print(f"\nConsulta de {nome}:")
        print(f"Cargo: {funcionario['cargo']}, Salário: R$ {funcionario['salario']:.2f}")
    else:
        print(f"Funcionário '{nome}' não encontrado.")

def relatorio_funcionarios(dicionario):
    if not dicionario:
        print("Nenhum funcionário cadastrado.")
        return
    
    print("\n--- Relatório de Funcionários ---")
    for nome, dados in dicionario.items():
        salario = dados["salario"]
        cargo = dados["cargo"]
        print(f"Funcionário: {nome}, Salário: R${salario:.2f}, Cargo: {cargo}")

# -------- Teste --------
cadastrar_funcionario("carlos", 1500, "desenvolvedor")
cadastrar_funcionario("maria", 2000, "gerente")

consultar_funcionario("carlos")
relatorio_funcionarios(dicionario)
