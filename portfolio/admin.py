from django.contrib import admin
from .models import Docente, Disciplina, Tecnologia, Projeto, ImagemProjeto, FichaTecnica, Visitante, Interesse

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
    list_display = ('titulo', 'disciplina',)
    ordering = ('titulo', 'disciplina',)
    search_fields = ('titulo', 'disciplina__nome',)
    list_filter = ('disciplina__nome',)
    inlines = (ImagemProjetoInline, FichaTecnicaInline)

admin.site.register(Projeto, ProjetoAdmin)

class ProjetoInline(admin.TabularInline):
    model = Projeto
    extra = 0
    fields = ('titulo',)
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

class VisitanteAdmin(admin.ModelAdmin):
    list_display = ('ip', 'session_key',)

admin.site.register(Visitante, VisitanteAdmin)

class InteresseAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao',)

admin.site.register(Interesse, InteresseAdmin)