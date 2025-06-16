from django.db import models
from django.utils.text import slugify

# Create your models here.

class Docente(models.Model):
    nome = models.CharField(
        max_length = 100,
    )

    def __str__(self):
        return self.nome


class Disciplina(models.Model):
    nome = models.CharField(
        max_length = 100,
    )
    ano = models.IntegerField()
    semestre = models.IntegerField()
    docentes = models.ManyToManyField(
        Docente,
        related_name = 'disciplinas',
    )
    link_moodle = models.URLField(
        max_length = 200,
        null = True,
        blank = True,
    )
    link_pagina_ulusofona = models.URLField(
        max_length = 200,
        null = True,
        blank = True,
        verbose_name = "Link página ULusofona",
    )

    def __str__(self):
        return self.nome


class Tecnologia(models.Model):
    nome = models.CharField(
        max_length = 100,
    )
    slug = models.SlugField(
        unique=True,
        help_text="URL amigável gerada automaticamente a partir do nome"
    )
    logotipo = models.ImageField(
        upload_to = 'projetos/logos',
    )
    link = models.URLField(
        max_length = 200,
    )
    descricao = models.TextField(
        verbose_name = "Descrição",
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nome)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome


class Projeto(models.Model):
    titulo = models.CharField(
        max_length = 200,
    )
    slug = models.SlugField(
        unique=True,
        help_text="URL amigável gerada automaticamente a partir do título"
    )
    descricao = models.TextField(
        verbose_name = "Descrição",
    )
    link_itch = models.URLField(
        max_length = 200,
        null = True,
        blank = True,
    )
    link_github = models.URLField(
        max_length = 200,
        null = True,
        blank = True,
    )
    link_video = models.URLField(
        max_length = 200,
        null = True,
        blank = True,
    )
    aspetos_tecnicos = models.TextField(
        verbose_name = "Aspectos técnicos",
    )
    conceitos_aplicados = models.TextField()
    my_role = models.TextField(
        blank=True,
        null=True,
        verbose_name='My Role & Contribution',
        help_text='Describe your specific role and contributions to this project'
    )
    disciplina = models.ForeignKey(
        Disciplina,
        on_delete = models.CASCADE,
        related_name = 'projetos',
        null = True,
        blank = True,
    )
    tecnologias = models.ManyToManyField(
        Tecnologia,
        related_name = 'projetos',
        blank = True,
    )
    ordem = models.IntegerField(
        default=0,
        help_text='Ordem de exibição (menor número aparece primeiro)'
    )

    class Meta:
        ordering = ['ordem', 'titulo']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.titulo


class ImagemProjeto(models.Model):
    imagem = models.ImageField(
        upload_to = 'projetos/imagens',
    )
    legenda = models.CharField(
        max_length = 200,
        null = True,
        blank = True,
    )
    projeto = models.ForeignKey(
        Projeto,
        on_delete = models.CASCADE,
        related_name = 'imagens',
    )

    def __str__(self):
        return f"Imagem de {self.projeto.titulo}"


class FichaTecnica(models.Model):
    projeto = models.OneToOneField(
        Projeto,
        on_delete = models.CASCADE,
        related_name = 'ficha_tecnica',
    )
    plataforma = models.CharField(
        max_length = 100,
        null = True,
        blank = True,
    )
    duracao_desenvolvimento = models.CharField(
        max_length = 100,
        null = True,
        blank = True,
        verbose_name = 'Duração do desenvolvimento',
    )
    equipa = models.IntegerField(
        null = True,
        blank = True,
        verbose_name = 'Número de elementos na equipa',
    )

    def __str__(self):
        return f"Ficha Técnica de {self.projeto.titulo}"
    
class Contacto(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    assunto = models.CharField(max_length=200)
    mensagem = models.TextField()
    data_envio = models.DateTimeField(auto_now_add=True)
    respondido = models.BooleanField(default=False)

    class Meta:
        ordering = ['-data_envio']
        verbose_name = 'Contacto'
        verbose_name_plural = 'Contactos'

    def __str__(self):
        return f"{self.nome} - {self.assunto}"