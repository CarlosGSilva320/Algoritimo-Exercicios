'''4.  A empresa TPVFR (Todo Programador Vai Ficar Rico) deseja conceder 
aumento  salarial  aos  seus  programadores.  O  aumento  será  calculado 
conforme o salário atual do programador, de acordo com as seguintes 
regras: 
(A).  Salários até R$ 2800,00: aumento de 20%. 
(B).  Salários entre R$ 2800,01 e R$ 7000,00: aumento de 15%. 
(C).  Salários entre R$ 7000,01 e R$ 15000,00: aumento de 10%. 
(D).  Salários acima de R$ 15000,00: aumento de 5%. 
Escreva um programa que recebe o salário de um programador e calcula 
o salário atualizado com o aumento.'''

salario = float(input("Digite seu salario: "))

if salario <= 2800:
    aumento = salario * (1 +  20 / 100)
elif salario <= 7000:
    aumento = salario * (1 + 15/100)
elif salario <= 15000:
    aumento = salario * (1 + 10 / 100)
else:
    aumento = salario * (1 + 5 / 100) 
print(f"O salário após o aumento é de R${aumento:.2f}")
