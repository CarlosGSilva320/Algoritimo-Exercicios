#Escreva uma função recursiva que inverta uma string. Por exemplo, se a entrada for "python", a função deve retornar "nohtyp".

def inverter(palavra):

    #caso base
    if len(palavra) <= 1:
        return palavra
    return palavra[-1] + inverter(palavra[:-1])

resultado = inverter('python')
print(resultado)