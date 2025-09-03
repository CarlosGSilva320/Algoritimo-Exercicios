'''5. Verificação de CPF (simplificado) 
Peça ao usuário um número de 11 dígitos e: 
• Verifique se todos os caracteres são dígitos; 
• Verifique se o tamanho é válido (11); 
• Mostre "CPF válido" ou "CPF inválido". 
(Não precisa calcular os dígitos verificadores ainda — é apenas validação estrutural.) '''

cpf = int(input("Digite o CPF para saber se é valido: "))

if cpf.isdigit() and len(cpf) == 11:
    print("CPF válido")
else:
    print("CPF inválido")