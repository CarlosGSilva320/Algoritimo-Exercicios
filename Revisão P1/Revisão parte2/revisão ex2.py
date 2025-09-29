clientes = [ {"nome": "Ana", "renda": 18000},
            {"nome": "Bruno", "renda": 30000},
            {"nome": "Carla", "renda": 60000},
            {"nome": "Diego", "renda": 345000} 
             ]

def calcular_imposto(renda):

    if renda <= 20000:
        imposto = 0
    elif renda <= 50000:
        imposto = (renda - 20000) * (15/100)
    else:
        imposto = (renda - 50000) * (25/100) + (30000 * 15/100)      
    return imposto
  
def relatorio(clientes):
    lista_final = []
    for c in clientes:
        imposto = calcular_imposto(c["renda"])
        lista_final.append({
                            "nome" : c["nome"],
                            "renda" : c["renda"],
                            "imposto" : imposto
        })
    return lista_final

resultado = relatorio(clientes)
print("\n--- Relatório ---")
for r in resultado:
    print(f"Nome: {r["nome"]}, Renda: R${r["renda"]:.2f}, Imposto devido: R${r["imposto"]:.2f}")




