

salario = float(input("Informe salario Bruto: R$ " ))

def calcula_imposto(salario):
    if salario <= 2112:
        imposto = 0
    elif salario <= 2826.65:
        imposto = (salario * (7.5/100)) - 158.4
    elif salario <= 3751.05:
        imposto = (salario * (15/100)) - 370.4
    elif salario <= 4664.68:
        imposto = (salario * (22.5/100)) - 651.73
    else:
        imposto = (salario * (27.5/100)) - 884.96
    return imposto




imposto = calcula_imposto(salario)
print(f"Salário Bruto: R${salario:.2f}")
print(f"Imposto Devido: R${imposto:.2f}")