azul = "\033[34m"
vermelho = "\033[31m"
reset = "\033[0m"

n = int(input("Digite um número: "))

total = 0

for c in range(1, n + 1 ):
    if n % c == 0:
        print(f"{azul}{c}", end=' ')
        total += 1
    else:
        print(f"{vermelho}{c}", end=' ')
print()
if total == 2:
    print(f"{azul}{n} é um número primo!{reset}")
else:
    print(f"{vermelho}{n} não é número primo!{reset}")
