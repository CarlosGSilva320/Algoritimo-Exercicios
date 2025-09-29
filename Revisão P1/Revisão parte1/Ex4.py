filmes = [
    {
        "titulo": "Inception",
        "diretor": "Chistopher Nolan",
        "bilheteria": 830,
        "avaliacoes": [9, 10, 8, 9, 10]
    },
    {
        "titulo": "Avengers Endgame",
        "diretor": "Anthony Russo",
        "bilheteria": 2797,
        "avaliacoes": [9, 9, 10, 10, 9]
    },
    {
        "titulo": "The Dark Knight",
        "diretor": "Chistopher Nolan",
        "bilheteria": 1005,
        "avaliacoes": [10, 10, 9, 10, 10]
    },
    {
        "titulo": "Jurassic Park",
        "diretor": "Steven Spielberg",
        "bilheteria":1029,
        "avaliacoes": [8, 9, 9, 8, 9]
    }
]
#1. Top 3 maiores bilheterias:  Crie uma função top_bilheteria(filmes) que retorne os 3 filmes com maior bilheteria.

def top_3():

    top = []

    for f in filmes:
        titulo = f["titulo"]
        bilheteria = f["bilheteria"]
        top.append([titulo, bilheteria])
    top = sorted(top, key=lambda x : x[1], reverse=True)
    return top[:3]
resultado = top_3()
print(resultado)
print("-=" * 20)

#2. Top 3 melhores avaliados: Crie uma função top_avaliacao(filmes)
#que calcule a média das avaliações de cada filme e retorne os 3 melhores. 

def top3_avaliacoes():

    top = []
    for f in filmes:
        titulo = f["titulo"]
        media = round(sum(f["avaliacoes"]) / len(f["avaliacoes"]), 2)
        top.append([titulo, media])
    top = sorted(top, key=lambda x: x[1], reverse=True)
    return top[:3]
resultado = top3_avaliacoes()
print(resultado)
print("-=" * 20)

#3. Bilheteria por diretor: Crie uma função bilheteria_por_diretor(filmes)
# que retorne um dicionário onde a chave é o diretor e o valor é o total de bilheteria de todos os seus filmes.

def bilheteria_por_diretor(diretor):

    lista ={}
    bilheteria = 0
    for f in filmes:
        if diretor == f["diretor"]:
            bilheteria += f["bilheteria"]
            lista = {diretor : bilheteria}
    return lista
resultado = bilheteria_por_diretor("Chistopher Nolan")
print(resultado)
print("-=" * 20)

#4. Campeão absoluto: Crie uma função campeao(filmes)
#que mostre qual filme é a melhor combinação de bilheteria alta e avaliação média alta. 

def campeão():

    lista = []

    for f in filmes:
        media = round(sum(f["avaliacoes"]) / len(f["avaliacoes"]), 2)
        score = f["bilheteria"] * media
        lista.append([f["titulo"], score])
    lista = sorted(lista, key=lambda x: x[1], reverse=True)
    return lista[0]
resultado = campeão()
print(resultado)