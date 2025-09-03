print("Digite um número por vez: ")
print("Para finalizar escreva 'FIM'")

numeros = []

while True:
    entrada = input("Qual número ?")

    if entrada.lower() == 'fim':
        break
    try:
        numero = float(entrada)
        numeros.append(numero)
    except ValueError:
        print("Entrada inválida, tente novamente: ")

if not numeros:
    print("Nenhum número para calcular!")
else:
    soma_total = sum(numeros)
    quantidade = len(numeros)
    media = soma_total / quantidade

    print(f"(A média dos números é: {media:.2f})")

