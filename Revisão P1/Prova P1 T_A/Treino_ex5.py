
#5  Você deve criar um programa em Python que utilize um dicionário para armazenar as informações de funcionários de uma empresa.
#  O programa deve ser capaz de fazer o seguinte:
#  
'''(A) Perguntar o nome, o salário e o cargo de cada funcionário. 
(B) Armazenar essas informações em um dicionário, onde a chave 
será o nome do funcionário e o valor será outro dicionário com 
as informações de salário e cargo. 
(C) O programa deve permitir ao usuário consultar o salário e o 
cargo de um funcionário informando seu nome. 
(D) O programa também deve permitir que o usuário liste todos os 
funcionários  cadastrados,  mostrando  seu  nome,  cargo  e 
salário.'''


funcionarios = {}

def cadastrar_funcionario(nome, salario, cargo):

    funcionarios[nome] = {'salario' : salario, 'cargo' : cargo }
    return funcionarios

def consultar_funcionario(nome):
    if nome in funcionarios:
        dicionario = funcionarios[nome]
        print(f"{nome},{dicionario['salario']}, {dicionario['cargo']}")
    else:
        print("não encontrado")

def relatorio_funcionarios(funcionarios):
    for nome, dados in funcionarios.items():
        print(f"{nome}, {dados['salario']}, {dados['cargo']}")        

cadastrar_funcionario("carlos", 1500, "ceo")
cadastrar_funcionario("Arthur", 2500, "Gerente")
consultar_funcionario("carlos")
relatorio_funcionarios(funcionarios)