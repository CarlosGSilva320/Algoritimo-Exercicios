#4.  A empresa TPVFR (Todo Programador Vai Ficar Rico) deseja conceder aumento  salarial  aos  seus  programadores.  
# O  aumento  será  calculado conforme o salário atual do programador, de acordo com as seguintes regras: 
'''(A).  Salários até R$ 3800,00: aumento de 20%. 
(B).  Salários entre R$ 3800,01 e R$ 10.000,00: aumento de 15%. 
(C).  Salários  entre  R$  10.000,01  e  R$  15000,00:  aumento  de 
10%. 
(D).  Salários acima de R$ 15000,00: aumento de 5%. 
Escreva um programa que recebe o salário de um programador e calcula 
o salário atualizado com o aumento.'''


salario = float(input("Informe o salário atual: R$"))

def calculo_aumento(salario):
    if salario <= 3800:
        aumento = salario * (1 + 20/100)
    elif salario <= 10000:
        aumento = salario * (1 + 15/100)
    elif salario <= 15000:
        aumento = salario * (1 + 10/100)
    else:
        aumento = salario * (1 + 5/100)
    return aumento

aumento = calculo_aumento(salario)
print(f"Salário com aumento: R${aumento:.2f}")
        