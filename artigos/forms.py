from django import forms
from .models import Comentario, Rating, Post, Autor

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['nome_comentador', 'conteudo']
        
        labels = {
            'nome_comentador': 'Name',
            'conteudo': 'Content',
        }

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['pontuacao']
        
        labels = {
            'pontuacao': 'Rating',
        }
        
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        
        labels = {
            'autor': 'Author',
            'titulo': 'Title',
            'conteudo': 'Content',
            'imagem_capa': 'Cover Image',
            'data': 'Post Date',
            'url_post': 'Original Link',
        }
        
class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = '__all__'
        
        labels = {
            'nome': 'Name',
            'foto_perfil': 'Profile Picture',
            'url_perfil': 'Original Profile Link',
        }