


salario = float(input("Informe o salário: R$"))
'''A).  Salários até R$ 2800,00: aumento de 20%. 
(B).  Salários entre R$ 2800,01 e R$ 7000,00: aumento de 15%. 
(C).  Salários entre R$ 7000,01 e R$ 15000,00: aumento de 10%. 
(D).  Salários acima de R$ 15000,00: aumento de 5%. '''
if salario <= 2800:
    aumento = salario * (1 + 20/100)
elif salario <= 7000:
    aumento = salario * (1+ 15/100)
elif salario <= 15000:
    aumento = salario * (1 + 10/100)
else:
    aumento = salario * (1 + 5/100)

print(f"Salario após o aumento de R${aumento}")