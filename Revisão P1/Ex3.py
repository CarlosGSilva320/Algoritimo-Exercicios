musicas = [
    {
        "titulo": "Back in Black",
        "artista": "AC/DC",
        "downloads": 6800,
        "avaliacoes": [5, 4, 5, 5, 4, 5]
    },
    {
        "titulo": "Stairway in Heaven",
        "artista": "Led Zeppelin",
        "downloads": 8900,
        "avaliacoes": [5, 5,  4, 5, 5, 5]
    },
    {
        "titulo": "Senter Sandman",
        "artista": "Metallica",
        "downloads": 8100,
        "avaliacoes": [5, 5, 5, 5, 4, 4, 5, 5]
    }
]
#1. Crie uma função que calcule a nota média de avaliação de cada música.

def media():

    titulos = {}

    for m in musicas:        
        titulos[m["titulo"]] = round(sum(m["avaliacoes"]) / len(m["avaliacoes"]), 2)     
    return titulos 

resultado = media()
print(resultado)

#2. Crie uma função que mostre qual artista tem o maior número total de downloads somando todas as suas músicas.
def maior_downloads():

    artista = ''
    total = 0

    for m in musicas:
        if m["downloads"] > total:
            total = m["downloads"]
            artista = m["artista"]
            
    return artista, total
resultado = maior_downloads()
print(resultado)

#3. Monte um ranking das músicas mais bem avaliadas (ordem decrescente da média das notas). 
#def mais_avaliações():

ranking = []

for m in musicas:
    titulo = m["titulo"]
    media = round(sum(m["avaliacoes"]) / len(m["avaliacoes"]), 2)
    ranking.append([titulo, media])
ranking_ordenaddo = sorted(ranking, key=lambda x: x[1], reverse=True )

print(ranking_ordenaddo)