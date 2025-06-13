from bandas.models import *
from datetime import timedelta
import json

def importar_bandas(bandas):
    Banda.objects.all().delete()

    with open(f'bandas/json/{bandas}') as f:
        bandas = json.load(f)

        for item in bandas:
            Banda.objects.create(
                nome = item['nome'],
                foto_banda = item['foto_banda'],
                ano_criacao = item['ano_criacao'],
                nacionalidade = item['nacionalidade'],
                descricao = item['descricao'],
                )

def importar_albuns(albuns):
    Album.objects.all().delete()

    with open(f'bandas/json/{albuns}') as f:
        albuns = json.load(f)

        for item in albuns:
            Album.objects.create(
                nome = item['nome'],
                banda = Banda.objects.get(nome = item['banda']),
                capa = item['capa'],
                ano_lancamento = item['ano_lancamento'],
                )

def importar_musicas(musicas):
    Musica.objects.all().delete()

    with open(f'bandas/json/{musicas}') as f:
        musicas = json.load(f)

        for item in musicas:
            h, m, s = map(int, item['duracao'].split(':'))
            duracao_formatada = timedelta(hours=h, minutes=m, seconds=s)

            Musica.objects.create(
                nome = item['nome'],
                banda = Banda.objects.get(nome = item['banda']),
                album = Album.objects.get(nome = item['album']),
                duracao = duracao_formatada,
                link = item['link'],
                letra = item['letra']
                )