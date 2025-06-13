from bandas.models import Banda, Album, Musica
from datetime import timedelta

print('Listar o nome das bandas, ordenadas alfabéticamente')
print(Banda.objects.values_list('nome', flat = True).order_by('nome'))

print('\n' + 'Listar o nome dos álbuns da banda "Queen", ordenados cronológicamente')
print(Banda.objects.get(nome = 'Queen').albuns.all().order_by('nome'))

print('\n' + 'Apresentar todos os álbuns que foram lançados entre 1990 a 2000.')
print(Album.objects.filter(ano_lancamento__gt = 1990, ano_lancamento__lt = 2000))

print('\n' + 'Criar uma playlist do album "A Night at the Opera", i.e., a lista dos links das músicas.')
print(Album.objects.get(nome = 'A Night at the Opera').musicas.values_list('link', flat = True))

print('\n' + 'Listar os albuns com músicas que durem mais de 5 minutos')
print(Album.objects.filter(musicas__duracao__gt = timedelta(minutes=5)))

print('\n' + 'Listar todas as músicas que contenham a palavra "come"')
print(Musica.objects.filter(nome__contains = 'come'))

print('\n' + 'Mostrar as 5 músicas mais longas')
print(Musica.objects.all().order_by('-duracao')[:5])

print('\n' + 'Listar todas as músicas que não têm link')
print(Musica.objects.filter(link__isnull=True).values_list('nome', flat=True))

print('\n' + 'Listar as músicas do álbum "Abbey Road" ordenadas pelo nome')
print(Musica.objects.filter(album__nome='Abbey Road').order_by('nome'))

print('\n' + 'Listar todas as músicas da banda "Pink Floyd" ordenadas por duração decrescente')
print(Musica.objects.filter(banda__nome='Pink Floyd').order_by('-duracao'))