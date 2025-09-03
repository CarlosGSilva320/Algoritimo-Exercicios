'''2. Validação de Login 
Implemente um algoritmo que simule um sistema de login: 
• O usuário tem 3 tentativas para digitar a senha correta (senha123). 
• Caso erre todas, mostre "Acesso bloqueado". 
• Caso acerte, mostre "Bem-vindo!".'''


senha_certa = 'python'
tentativas = 3

while tentativas > 0:
    senha = input("Digite a senha: ")

    if senha == senha_certa:
        print("Bem vindo!")
        break

    else:
        tentativas -= 1
        print(f"Senha incorreta. {tentativas} chances!")

if tentativas == 0:
    print("Acesso bloqueado!")