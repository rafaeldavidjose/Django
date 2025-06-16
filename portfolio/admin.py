from django.contrib import admin
from .models import *

# Register your models here.

class ImagemProjetoInline(admin.TabularInline):
    model = ImagemProjeto
    extra = 3
    max_num = 3
    fields = ('imagem', 'legenda',)
    show_change_link = True

class FichaTecnicaInline(admin.StackedInline):
    model = FichaTecnica
    extra = 1
    max_num = 1
    show_change_link = True

class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'disciplina', 'ordem')
    ordering = ('ordem', 'titulo')
    search_fields = ('titulo', 'disciplina__nome',)
    list_filter = ('disciplina__nome',)
    list_editable = ('ordem',)  # Permite editar ordem diretamente na lista
    inlines = (ImagemProjetoInline, FichaTecnicaInline)
    
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('titulo', 'descricao', 'ordem')
        }),
        ('Links', {
            'fields': ('link_itch', 'link_github', 'link_video')
        }),
        ('Detalhes Técnicos', {
            'fields': ('aspetos_tecnicos', 'conceitos_aplicados')
        }),
        ('Associações', {
            'fields': ('disciplina', 'tecnologias')
        }),
    )

admin.site.register(Projeto, ProjetoAdmin)

class ProjetoInline(admin.TabularInline):
    model = Projeto
    extra = 0
    fields = ('titulo', 'ordem')
    readonly_fields = ('titulo',)
    show_change_link = True

class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ano', 'semestre',)
    ordering = ('nome', 'ano', 'semestre',)
    search_fields = ('nome',)
    list_filter = ('ano', 'semestre',)
    inlines = (ProjetoInline,)

admin.site.register(Disciplina, DisciplinaAdmin)

class DisciplinaInline(admin.TabularInline):
    model = Disciplina.docentes.through
    extra = 0
    show_change_link = True

class DocenteAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    ordering = ('nome',)
    search_fields = ('nome',)
    inlines = (DisciplinaInline,)

admin.site.register(Docente, DocenteAdmin)

class TecnologiaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    ordering = ('nome',)
    search_fields = ('nome',)

admin.site.register(Tecnologia, TecnologiaAdmin)

class ContactoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'assunto', 'data_envio', 'respondido')
    list_filter = ('respondido', 'data_envio')
    search_fields = ('nome', 'email', 'assunto')
    readonly_fields = ('data_envio',)
    ordering = ('-data_envio',)
    
    fieldsets = (
        ('Contact Information', {
            'fields': ('nome', 'email', 'assunto')
        }),
        ('Message', {
            'fields': ('mensagem',)
        }),
        ('Status', {
            'fields': ('respondido', 'data_envio')
        }),
    )

admin.site.register(Contacto, ContactoAdmin)