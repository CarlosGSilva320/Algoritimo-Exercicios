# Verificação simples de CPF

cpf = input("Digite seu CPF (somente números): ")

if cpf.isdigit() and len(cpf) == 11:
    print("CPF válido")
else:
    print("CPF inválido")
