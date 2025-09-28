'''3.  Crie  um  programa  em  Python  que  implemente  uma  função  chamada 
calcula_imposto_renda.  A  função  deve  receber  um  único  parâmetro: 
salário: o valor do salário bruto de um indivíduo. '''
#Com  base  na  tabela  de  alíquotas  abaixo,  a  função deve  calcular e retornar o valor do imposto de renda devido: 
'''Faixa Salarial (R$)  Alíquota (%)  Dedução (R$)  Faixa Salarial (R$) 
Até 2.112,00  Isento  0  Até 2.112,01 
De 2.112,01 a 2.826,65  7,50%  158,4  De 2.112,01 a 2.826,66 
De 2.826,66 a 3.751,05  15%  370,4  De 2.826,66 a 3.751,06 
De 3.751,06 a 4.664,68  22,50%  651,73  De 3.751,06 a 4.664,69 
Acima de 4.664,68  27,50%  884,96  Acima de 4.664,69'''

'''Requisitos: 
•  A função deve retornar o valor do imposto de renda a ser pago. 
•  O programa deve solicitar ao usuário o salário bruto, chamar a função e 
exibir o imposto devido.'''

salario = float(input("Digite seu Salário Bruto R$"))

def calcula_imposto_renda():

    if salario <= 2112:
        imposto = 0
    elif salario <= 2826.65:
        imposto = (salario * (7.5 / 100)) - 158.4
    elif salario <= 3751.05:
        imposto = (salario * (15 / 100)) - 370.4
    elif salario <= 4664.68:
        imposto = (salario * (22.5)) - 651.73
    else:
        imposto = (salario * (27.5)) - 884.96
    return imposto
resultado = calcula_imposto_renda()
print(f"O salário Bruto é de R${salario:.2f}")
print(f"O imposto de renda devido é de R${resultado:.2f}")