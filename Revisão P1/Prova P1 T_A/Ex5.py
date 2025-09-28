# Você deve criar um programa em Python que utilize um dicionário para armazenar as informações de funcionários de uma empresa. 
# O programa deve ser capaz de fazer o seguinte: 

''' (A) Perguntar o nome, o salário e o cargo de cada funcionário. 
    (B) Armazenar essas informações em um dicionário, onde a chave 
será o nome do funcionário e o valor será outro dicionário com 
as informações de salário e cargo. 
    (C) O programa deve permitir ao usuário consultar o salário e o 
cargo de um funcionário informando seu nome. 
    (D) O programa também deve permitir que o usuário liste todos os 
funcionários  cadastrados,  mostrando  seu  nome,  cargo  e 
salário'''

dicionario = {}

def cadastrar_funcionario(nome, salario, cargo):
    
        dicionario[nome] = { 
         "salario" : salario,
         "cargo" : cargo} 
    
    
        


def consultar_funcionario(nome):
    print("Consulta de funcionário =>")
    
    if nome in dicionario:
        funcionario = dicionario[nome]
        print(f"O funcionário {nome} tem o salario de R${funcionario['salario']:.2f} e o cargo de {funcionario['cargo']}")
    else:
         print("Funcionario não cadastrado")   
    print("-=" * 15)

def relatorio_funcionarios(dicionario):
    print("Consulta de Banco de dados de funcionários =>")
    
    if not dicionario:
        print("Nenhum funcionario cadastrado.")
        return

    for nome, dados in dicionario.items():
        salario = dados["salario"]
        cargo = dados["cargo"]
        
        
        print(f"Funcionário: {nome}, salario: R${salario:.2f}, cargo: {cargo}")
    print("-=" * 15)



cadastrar_funcionario("carlos", 1500, "desenvolvedor")
cadastrar_funcionario("maria", 2000, "gerente")

consultar_funcionario("carlos")

relatorio_funcionarios(dicionario)