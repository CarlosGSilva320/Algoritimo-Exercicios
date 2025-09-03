'''Escreva um programa que: 
1. Receba 10 números inteiros digitados pelo usuário. 
2. Separe-os em duas listas: pares e ímpares. 
3. Exiba quantos números pares e ímpares foram digitados.'''

num_pares = []
num_impar = []

def receber_num():
    
    for i in range(10):

        num = int(input(f"Digite 10  números para saber se é par ou impar: N°{i + 1}: "))
        if num % 2 == 0:
            num_pares.append(num)
        else:
            num_impar.append(num)

receber_num()

print(f"São {len(num_pares)} números pares e {len(num_impar)} números ímpares")
