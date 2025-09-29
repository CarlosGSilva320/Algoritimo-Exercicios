clientes = [ {"nome": "Ana", "renda": 18000},
            {"nome": "Bruno", "renda": 30000},
            {"nome": "Carla", "renda": 60000},
            {"nome": "Diego", "renda": 345000} 
             ]

''' • Até R$ 20.000,00                                                                                                                       
isento. 
    • De R$ 20.001,00 até R$ 50.000,00                                                                                           
15% sobre o valor que exceder R$ 20.000,00. 
    • Acima de R$ 50.000,00                                                                                                                
15% sobre o valor entre R$ 20.001 e R$ 50.000,00, + 25% sobre o valor acima de R$ 
50.000,00.'''


def calcular_imposto(renda):
   
    if renda <= 20000:
        imposto = 0
    elif renda <= 50000:
        imposto = (renda - 20000) * ( 15 / 100 )
    else:
        imposto = (30000 * (15/100)) + ((renda - 50000) * (25/100))
    return imposto

'''•  Crie uma função relatorio(clientes) que percorra a lista de clientes e monte uma 
nova lista com dicionários no formato: 
{"nome": ..., "renda": ..., "imposto": ...} 
•  Exiba o relatório final mostrando todos os clientes com seus respectivos impostos.'''

def relatorio(clientes):
    cliente_impostos = []
    for cliente in clientes:
        imposto = calcular_imposto(cliente['renda'])

        cliente_impostos.append({"nome" : cliente['nome'],
                              "renda" : cliente['renda'],
                              "imposto" : imposto})
    return cliente_impostos
resultado = relatorio(clientes)
for r in resultado:
    print(r)