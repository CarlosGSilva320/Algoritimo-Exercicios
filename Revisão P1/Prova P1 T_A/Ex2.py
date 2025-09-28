'''2.  Escreva um programa em Python que contenha uma função chamada 
calcula_bonificacao.  
(A).  Essa função deve receber dois parâmetros:  
i.  taxa_bonus:  A  porcentagem  de  bonificação  de  produção 
concedida ao funcionário.  
ii.  salario_base: O salário do funcionário antes da bonificação. 
A  função  deve  calcular  e  retornar  o  novo  salário  do  funcionário,  já 
incluindo a bonificação. No programa principal, solicite ao usuário que 
informe o salário base e a taxa de bonificação, chame a função e exiba o 
salário final, a bonificação concedida e o salário base informado.'''


salario = float(input("Digite o salário base: "))

bonus = float(input("Digite o valor da bonificação em porcentagem (0 até 100): "))


def calcula_bonificação():


    novo = (salario * ( 1 + bonus / 100))
    return novo


novo = calcula_bonificação()
print(f"O salário base é R${salario:.2f} mais a bonificação de {bonus}% dando um total de R${novo:.2f} ")