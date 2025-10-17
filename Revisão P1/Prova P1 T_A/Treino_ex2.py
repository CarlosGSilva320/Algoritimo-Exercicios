'''2.  Escreva um programa em Python que contenha uma função chamada 
calcula_bonificacao.  
(A).  Essa função deve receber dois parâmetros:  
i.  taxa_bonus:  A  porcentagem  de  bonificação  de  produção 
concedida ao funcionário.  
ii.  salario_base: O salário do funcionário antes da bonificação. 
A  função  deve  calcular  e  retornar  o  novo  salário  do  funcionário,  já 
incluindo a bonificação. No programa principal, solicite ao usuário que 
informe o salário base e a taxa de bonificação, chame a função e exiba o 
salário final, a bonificação concedida e o salário base informado'''



salario = float(input("Informe o salário do funcionario => R$ "))
bonus = float(input("Informe a bonificação em porcentagem (0/100)%: "))


def calcula_bonificacao(salario, bonus):

    bonificação = salario * (bonus/100)
    aumento = salario + bonificação

    return bonificação, aumento

bonificação, aumento = calcula_bonificacao(salario, bonus)

print(f"Salário base: R${salario:.2f}, Bonificação: R${bonificação:.2f}, Salário final: R${aumento:.2f}.")