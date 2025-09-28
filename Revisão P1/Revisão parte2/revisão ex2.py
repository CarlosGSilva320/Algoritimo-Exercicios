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

discionario = []

def cadastar_funcionario(lista, nome, salario, cargo):

    funcionario = {
        "nome" : nome,
        "salario": salario,
        "cargo"  :  cargo
        }
    
    lista.append(funcionario)
    

cadastar_funcionario("carlos", 1500, "desenvolvedor")