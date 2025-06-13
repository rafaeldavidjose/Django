from django.contrib import admin
from .models import Autor, Post, Comentario, Rating

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('autor', 'titulo', 'data',)
    ordering = ('autor', 'titulo', 'data',)
    search_fields = ('autor__nome', 'titulo')
    list_filter = ('autor',)

admin.site.register(Post, PostAdmin)

class PostInline(admin.TabularInline):
    model = Post
    extra = 0
    fields = ('titulo',)
    readonly_fields = ('titulo',)
    show_change_link = True

class AutorAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    ordering = ('nome',)
    search_fields = ('nome',)
    inlines = (PostInline,)

admin.site.register(Autor, AutorAdmin)

class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('post', 'nome_comentador', 'data', 'comentario_pai',)
    ordering = ('post', 'nome_comentador', 'data',)
    search_fields = ('post__titulo', 'nome_comentador',)
    list_filter = ('post','nome_comentador', 'comentario_pai',)

admin.site.register(Comentario, ComentarioAdmin)

class RatingAdmin(admin.ModelAdmin):
    list_display = ('post', 'pontuacao',)
    ordering = ('post', 'pontuacao',)
    search_fields = ('post__titulo',)
    list_filter = ('post__titulo',)

admin.site.register(Rating, RatingAdmin)