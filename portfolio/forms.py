from django import forms
from django.forms import inlineformset_factory
from .models import Projeto, FichaTecnica, ImagemProjeto, Tecnologia, Disciplina, Docente, Interesse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
import requests

class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = '__all__'

        labels = {
            'titulo': 'Title',
            'descricao': 'Description',
            'link_itch': 'Link Itch.io',
            'link_github': 'Link GitHub',
            'link_video': 'Link Video',
            'aspetos_tecnicos': 'Technical Aspects',
            'conceitos_aplicados': 'Core Concepts',
            'disciplina': 'Course',
            'tecnologias': 'Technologies Used',
        }

class ImagemProjetoForm(forms.ModelForm):
    class Meta:
        model = ImagemProjeto
        fields = ('imagem', 'legenda')

        labels = {
            'imagem': 'Image',
            'legenda': 'Caption',
        }

ImagemProjetoFormSet = inlineformset_factory(
    Projeto,
    ImagemProjeto,
    form=ImagemProjetoForm,
    extra=3,
    max_num=3,
    can_delete=False,
)

class FichaTecnicaForm(forms.ModelForm):
    class Meta:
        model = FichaTecnica
        exclude = ['projeto']

        labels = {
            'plataforma': 'Platform',
            'duracao_desenvolvimento': 'Development Time',
            'equipa': 'Team Size',
        }

class TecnologiaForm(forms.ModelForm):
    class Meta:
        model = Tecnologia
        fields = '__all__'

        labels = {
            'nome': 'Name',
            'logotipo': 'Logo',
            'descricao': 'Description',
        }

class DisciplinaForm(forms.ModelForm):
    class Meta:
        model = Disciplina
        fields = '__all__'

        labels = {
            'nome': 'Name',
            'ano': 'Academic Year',
            'semestre': 'Semester',
            'docentes': 'Teachers',
            'link_moodle': 'Moodle Link',
            'link_pagina_ulusofona': 'ULusofona Link Page',
        }

class DocenteForm(forms.ModelForm):
    class Meta:
        model = Docente
        fields = '__all__'

        labels = {
            'nome': 'Name',
        }

class RegistoForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

        widgets = {
            'email': forms.EmailInput(attrs={'required': True}),
            'first_name': forms.TextInput(attrs={'required': True}),
            'last_name': forms.TextInput(attrs={'required': True}),
        }

class InteresseForm(forms.ModelForm):
    class Meta:
        model = Interesse
        fields = '__all__'
        
# APIs
class BandaExternaForm(forms.Form):
    nome = forms.CharField(max_length=100, label='Band Name')
    nr_elementos = forms.IntegerField(label='Number of Members')
    ano_criacao = forms.IntegerField(label='Year Created')
    foto = forms.ImageField(required=False, label='Photo (Optional)')

class AlbumExternoForm(forms.Form):
    nome = forms.CharField(max_length=100, label='Album Name')
    nr_musicas = forms.IntegerField(label='Number of Songs')
    band = forms.ChoiceField(choices=[], label='Band')
    spotify_link = forms.URLField(required=False, label='Spotify Link (Optional)')
    capa = forms.ImageField(required=False, label='Cover Image (Optional)')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        try:
            response = requests.get('https://a22202884.pw.deisi.ulusofona.pt/bandas/api/bandas/', verify=False)
            if response.status_code == 200:
                bandas = response.json()
                choices = [(banda['id'], f"{banda['nome']} (ID: {banda['id']})") for banda in bandas]
                self.fields['band'].choices = [('', 'Select a Band')] + choices
            else:
                self.fields['band'].choices = [('', 'No bands available')]
        except:
            self.fields['band'].choices = [('', 'Error loading bands')]

class MusicaExternaForm(forms.Form):
    nome = forms.CharField(max_length=100, label='Song Name')
    duration = forms.CharField(max_length=10, label='Duration (seconds)')
    album = forms.ChoiceField(choices=[], label='Album')
    spotify_link = forms.URLField(required=False, label='Spotify Link (Optional)')
    lyrics = forms.CharField(widget=forms.Textarea, required=False, label='Lyrics (Optional)')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        try:
            response = requests.get('https://a22202884.pw.deisi.ulusofona.pt/bandas/api/albuns/', verify=False)
            if response.status_code == 200:
                albuns = response.json()
                choices = [(album['id'], f"{album['nome']} (ID: {album['id']})") for album in albuns]
                self.fields['album'].choices = [('', 'Select an Album')] + choices
            else:
                self.fields['album'].choices = [('', 'No albums available')]
        except:
            self.fields['album'].choices = [('', 'Error loading albums')]