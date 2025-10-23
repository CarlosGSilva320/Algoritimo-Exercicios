# 5.  Você deve criar um programa em Python que utilize um dicionário para armazenar as informações de funcionários de uma empresa. 
# O programa deve ser capaz de fazer o seguinte: 
'''(A) Perguntar o nome, cpf, o salário, o setor e o cargo de cada 
funcionário. 
(B) Armazenar essas informações em um dicionário, onde a chave 
será o nome do funcionário e o valor será outro dicionário com 
as informações de  cpf, salario, o setor e o cargo. 
(C) O programa deve permitir ao usuário consultar o salário e o 
cargo de um funcionário informando seu nome. 
(D) O programa também deve permitir que o usuário liste todos os 
funcionários  cadastrados,  mostrando  seu  nome,  cargo  e 
salário.'''

funcionarios = {}

def cadastrar_funcionarios(nome, cpf, salario, setor, cargo):

    funcionarios[nome] = {'cpf' : cpf, 'salario' : salario, 'setor' : setor, 'cargo' : cargo }
    return funcionarios

def consultar_funcionario(nome):
    print("---Consultar Funcionário---")
    if nome in funcionarios:
        dicionario = funcionarios[nome]
        print(f"Funcionário: {nome}, Salário: {dicionario['salario']}, Cargo: {dicionario['cargo']}")
    else:
        print("Funcionário não cadastrado.")
 
def relatorio_funcionarios(funcionarios):
    print("---Relatório Funcionários---")
    for nome, dados in funcionarios.items():
        print(f"Funcionario: {nome}, Cargo: {dados['cargo']}, Salário: {dados['salario']}  ")


cadastrar_funcionarios('carlos', 5374732706, 1500, 'TI', 'CEO'  )
cadastrar_funcionarios('Arthur', 4374731705, 2500, 'TI', 'Gerente'  )

consultar_funcionario('carlos')

relatorio_funcionarios(funcionarios)
