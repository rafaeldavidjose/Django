from django.contrib import admin
from .models import Banda, Album, Musica

# Register your models here.

class MusicaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'banda', 'album',)
    ordering = ('nome', 'banda', 'album',)
    search_fields = ('nome', 'banda__nome', 'album__nome',)
    list_filter = ('banda__nome', 'album__nome',)

admin.site.register(Musica, MusicaAdmin)

class MusicaInline(admin.TabularInline):
    model = Musica
    extra = 0
    fields = ('nome', 'album',)
    readonly_fields = ('nome', 'album',)
    show_change_link = True

class AlbumAdmin(admin.ModelAdmin):
    list_display = ('nome', 'banda', 'ano_lancamento')
    ordering = ('nome', 'banda', 'ano_lancamento')
    search_fields = ('nome', 'banda__nome',)
    list_filter = ('banda__nome',)
    inlines = (MusicaInline,)

admin.site.register(Album, AlbumAdmin)

class AlbumInline(admin.TabularInline):
    model = Album
    extra = 0
    fields = ('nome',)
    readonly_fields = ('nome',)
    show_change_link = True

class BandaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ano_criacao',)
    ordering = ('nome', 'ano_criacao',)
    search_fields = ('nome',)
    inlines = (AlbumInline, MusicaInline)

admin.site.register(Banda, BandaAdmin)