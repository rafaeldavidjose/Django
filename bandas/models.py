from django.db import models

# Create your models here.

class Banda(models.Model):
    nome = models.CharField(
        max_length = 100
    )
    foto_banda = models.ImageField(
        upload_to = 'bandas/fotos',
        null = True,
        blank = True,
        verbose_name = 'Foto da banda'
    )
    ano_criacao = models.IntegerField(
        verbose_name = 'Ano de criação'
    )
    nacionalidade = models.CharField(
        max_length = 50,
    )
    descricao = models.TextField(
        null = True,
        blank = True,
        verbose_name = 'Descrição'
    )

    def __str__(self):
        return self.nome

class Album(models.Model):
    nome = models.CharField(
        max_length = 100
    )
    banda = models.ForeignKey(
        Banda,
        on_delete = models.CASCADE,
        related_name = 'albuns'
    )
    capa = models.ImageField(
        upload_to='bandas/capas',
        null = True,
        blank = True,
    )
    ano_lancamento = models.IntegerField(
        verbose_name = "Ano de lançamento",
    )

    def __str__(self):
        return self.nome

class Musica(models.Model):
    nome = models.CharField(
        max_length = 100
    )
    banda = models.ForeignKey(
        Banda,
        on_delete = models.CASCADE,
        related_name = 'musicas'
    )
    album = models.ForeignKey(
        Album,
        on_delete = models.CASCADE,
        related_name = 'musicas'
    )
    duracao = models.DurationField(
        verbose_name = 'Duração',
    )
    link = models.URLField(
        ("URL da música"),
        null = True,
        max_length = 128,
        db_index = True,
        unique = True,
        blank = True
    )
    letra = models.TextField(
        null = True,
        blank = True,
    )

    def __str__(self):
        return self.nome