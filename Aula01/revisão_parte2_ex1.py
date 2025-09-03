n = int(input("Digite um número para contagem: "))

soma = 0
contador = 0

for i  in range(1, n + 1 ):
    soma += i
    contador += 1

formula = n * (n + 1) // 2

print(f"A soma  é igual a {soma}")
print(f"São feitas {contador} contagens")
print(f"A contagem pela formula é igual a {formula}")