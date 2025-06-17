from django.contrib import admin
from .models import *

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

class ProjetoTecnologiaInline(admin.TabularInline):
    model = ProjetoTecnologia
    extra = 0
    fields = ('tecnologia', 'ordem_no_cartao', 'mostrar_no_cartao')
    verbose_name = 'Tecnologia'
    verbose_name_plural = 'Tecnologias (controlo individual para cartão)'
    ordering = ['ordem_no_cartao', 'tecnologia__nome']
    
class AwardInline(admin.TabularInline):
    model = Award
    extra = 2
    fields = ('titulo', 'ordem')
    show_change_link = True

class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'slug', 'disciplina', 'ordem')
    ordering = ('ordem', 'titulo')
    search_fields = ('titulo', 'disciplina__nome',)
    list_filter = ('disciplina__nome',)
    list_editable = ('ordem',)  
    prepopulated_fields = {'slug': ('titulo',)}  
    inlines = (ImagemProjetoInline, FichaTecnicaInline, AwardInline)
    
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('titulo', 'slug', 'descricao', 'ordem')
        }),
        ('Links', {
            'fields': ('link_itch', 'link_github', 'link_video')
        }),
        ('Detalhes Técnicos', {
            'fields': ('aspetos_tecnicos', 'conceitos_aplicados', 'my_role')
        }),
        ('Associações', {
            'fields': ('disciplina',)
        }),
    )

admin.site.register(Projeto, ProjetoAdmin)

class ProjetoInline(admin.TabularInline):
    model = Projeto
    extra = 0
    fields = ('titulo', 'slug', 'ordem')
    readonly_fields = ('titulo', 'slug')
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
    list_display = ('nome', 'slug')
    ordering = ('nome',)
    search_fields = ('nome',)
    prepopulated_fields = {'slug': ('nome',)}  

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

class ProjetoTecnologiaAdmin(admin.ModelAdmin):
    list_display = ('projeto', 'tecnologia', 'ordem_no_cartao', 'mostrar_no_cartao')
    list_filter = ('mostrar_no_cartao', 'tecnologia')
    search_fields = ('projeto__titulo', 'tecnologia__nome')
    ordering = ('projeto__titulo', 'ordem_no_cartao')
    list_editable = ('ordem_no_cartao', 'mostrar_no_cartao')

admin.site.register(ProjetoTecnologia, ProjetoTecnologiaAdmin)