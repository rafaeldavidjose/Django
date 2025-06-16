from django import forms
from django.forms import inlineformset_factory
from .models import *

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
            'my_role': 'My Role & Contribution',
            'disciplina': 'Course',
            'tecnologias': 'Technologies Used',
            'ordem': 'Display Order',
        }
        
        help_texts = {
            'ordem': 'Lower numbers appear first (0 = highest priority)',
            'my_role': 'Describe your specific role and what you contributed to this project',
        }
        
        widgets = {
            'ordem': forms.NumberInput(attrs={
                'min': 0,
                'step': 1,
                'placeholder': 'Enter display order (0-999)'
            }),
            'my_role': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Example: Lead programmer responsible for gameplay mechanics, AI systems, and player controller implementation...'
            }),
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
        
class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['nome', 'email', 'assunto', 'mensagem']
        
        labels = {
            'nome': 'Your Name',
            'email': 'Your Email',
            'assunto': 'Subject',
            'mensagem': 'Message',
        }
        
        widgets = {
            'nome': forms.TextInput(attrs={
                'placeholder': 'Enter your full name...',
                'class': 'form-control'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'your.email@example.com',
                'class': 'form-control'
            }),
            'assunto': forms.TextInput(attrs={
                'placeholder': 'What would you like to discuss?',
                'class': 'form-control'
            }),
            'mensagem': forms.Textarea(attrs={
                'placeholder': 'Write your message here...',
                'rows': 6,
                'class': 'form-control'
            }),
        }