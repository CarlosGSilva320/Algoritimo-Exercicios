atletas = [
    {
        "nome": "Lucas",
        "idade": 20,
        "modalidades": ["Natação", "Corrida"],
        "treinos": {"Natação": 12, "Corrida": 8}
    },
    {
        "nome": "Mariana",
        "idade": 25,
        "modalidades": ["Musculação", "Yoga", "Pilates"],
        "treinos": {"Musculação": 15, "Yoga": 10, "Pilates": 5}
    },
    {
        "nome": "João",
        "idade": 22,
        "modalidades": ["Corrida", "Ciclismo"],
        "treinos": {"Corrida": 20, "Ciclismo": 18}
    }
]
#1. Crie uma função que calcule a média de idade dos atletas que praticam um esporte específico.


def calc_media(esporte):

    soma_idade = 0
    quantida = 0

    for atleta in atletas:
        if esporte in atleta["modalidades"]:
            soma_idade += atleta["idade"]
            quantida += 1
    if quantida > 0:
        media = soma_idade / quantida
        return media

    else:
        print("Não possui registro")    

resultado = calc_media("Natação")
print(resultado)

#2. Crie uma função que, dado um atleta, informe qual esporte ele mais treinou.

def  mais_treino(nome):

    for atleta in atletas:
        if atleta["nome"] == nome:
            treino = atleta["treinos"]

          
            mais_treinado = ""
            maior_quant = 0

            for esporte, quantidade in treino.items():
                if quantidade > maior_quant:
                    maior_quant = quantidade
                    mais_treinado = esporte
            return mais_treinado, maior_quant
        else:
            "Nome não encontrado"
resultado = mais_treino("João")
print(f"O esporte mais treinado foi {resultado[0]} durante {resultado[1]} horas.")























