from django.db import models

# Create your models here.

class Autor(models.Model):
    nome = models.CharField(
        max_length = 100,
    )
    foto_perfil = models.ImageField(
        upload_to = 'artigos/fotosperfil',
        null = True,
        blank = True,
        verbose_name = 'Foto de Perfil',
    )
    url_perfil = models.URLField(
        ("URL perfil"),
        null = True,
        max_length = 128,
        db_index = True,
        unique = True,
        blank = False
    )

    def __str__(self):
        return self.nome

class Post(models.Model):
    autor = models.ForeignKey(
        Autor,
        on_delete = models.CASCADE,
        related_name = 'posts',
    )
    titulo = models.CharField(
        max_length = 255,
        verbose_name = 'Título',
    )
    conteudo = models.TextField(
        verbose_name = 'Conteúdo',
    )
    imagem_capa = models.ImageField(
        upload_to = 'artigos/capas',
        null = True,
        blank = True,
    )
    data = models.DateField(
        auto_now = False,
        auto_now_add = False,
        verbose_name = 'Data de publicação',
    )
    url_post = models.URLField(
        ("URL post"),
        null = True,
        max_length = 128,
        db_index = True,
        unique = True,
        blank = False
    )

    def __str__(self):
        return f'{self.titulo} ({self.autor})'

class Comentario(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete = models.CASCADE,
        related_name = 'comentarios',
    )
    nome_comentador = models.CharField(
        max_length = 100,
        verbose_name = 'Nome do comentador'
    )
    conteudo = models.TextField(
        verbose_name = 'Conteúdo'
    )
    data = models.DateField(
        auto_now = False,
        auto_now_add = False,
    )
    comentario_pai = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        verbose_name = "Comentário pai",
        related_name='respostas',
    )

    def __str__(self):
        return f'{self.nome_comentador} ({self.post})'

class Rating(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete = models.CASCADE,
        related_name = 'ratings'
    )

    UM = 1
    DOIS = 2
    TRES = 3
    QUATRO = 4
    CINCO = 5

    RATING_CHOICES = [
        (UM, '1'),
        (DOIS, '2'),
        (TRES, '3'),
        (QUATRO, '4'),
        (CINCO, '5'),
    ]

    pontuacao = models.IntegerField(
        choices = RATING_CHOICES,
        default = TRES,
        verbose_name = 'Pontuação',
    )

    def __str__(self):
        return f'{self.post}: Rating({self.pontuacao})'