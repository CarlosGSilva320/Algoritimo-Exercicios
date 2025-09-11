#2. Escreva uma função recursiva que calcule a potência de um número x elevado a um expoente n.

def potencia(base, expoente):
    
    #caso base
    if expoente == 0:
        return 1
    
    elif expoente < 0:
        return base * potencia(base, expoente + 1)
    else:
        return base * potencia(base, expoente - 1)
    
resulatdo = potencia(2,3)
print(resulatdo)