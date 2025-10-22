lista = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]


num = int(input("Digiteum número: "))

'''def busca_binaria(lista, num):
    l = 0
    r = len(lista) - 1

    while (l <= r):
        m = (l + r) // 2
        if lista[m] == num:
            return f"Número encontrado na posição -> {m + 1}"
        elif lista[m] > num:
            r = m - 1
        else:
            l = m + 1
    return False
resultado = busca_binaria(lista, num)
print(resultado)'''
'''
def binaria_recursiva(lista, inicio, fim, num):
    if inicio > fim:
        return "Número não encontrado"
    m = (inicio + fim) // 2

    if lista[m] == num:
        return f"Número encontrado na posição {m + 1}"
    elif lista[m] > num:
        return binaria_recursiva(lista, inicio, m - 1, num)
    else:
        return binaria_recursiva(lista, m + 1, fim, num)

resultado = binaria_recursiva(lista, 0, len(lista) - 1, num)
print(resultado)
'''


def busca_linear(lista, num):
    for i in range(len(lista)):
        if lista[i] == num:
            return f"Número encontrado na posição {i + 1}"
    return "Número não encontrado"

resultado = busca_linear(lista, num)
print(resultado)