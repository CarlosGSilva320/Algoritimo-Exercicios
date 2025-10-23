# 2.  Crie  um  programa  em  Python  que  contenha  uma  função  chamada  calcula_bonificacao.
#  A função deve receber dois parâmetros: 
'''taxa_bonus  →  a  porcentagem  de  bonificação  concedida  ao 
funcionário. 
salario_base → o salário do funcionário antes da bonificação. 
A  função  deve  calcular  e  retornar  o  novo  salário,  já  incluindo  a 
bonificação.
•  No programa principal: 
Solicite  ao  usuário  que  informe  o  salário  base  e  a  taxa  de 
bonificação. 
Chame a função calcula_bonificacao. 
Exiba na tela: 
salário base informado, 
valor da bonificação concedida, 
salário final após a bonificação.'''

salario = float(input("Salario base: R$"))
bonus = float(input("Bônus em porcentagem (0/100)%: "))

def calcula_bonificacao(salario, bonus):
    bonificação = salario * (bonus/100)
    novo_salario = salario + bonificação

    return bonificação, novo_salario

bonificação, novo_salario = calcula_bonificacao(salario, bonus)
print(f"Salário base: R${salario}, Bonus: R$ {bonificação:.2f} , Salário com Bonificação: {novo_salario:.2f}")

