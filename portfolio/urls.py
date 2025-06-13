from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('interesses/', views.interesses_view, name='interesses'),
    path('projetos/', views.projetos_view, name='projetos'),
    path('projetos/<int:projeto_id>/', views.projeto_view, name='projeto_path'),
    path('projetos/novo', views.novo_projeto_view, name="novo_projeto"),
    path('projetos/<int:projeto_id>/edita', views.edita_projeto_view, name="edita_projeto"),
    path('projetos/<int:projeto_id>/apaga', views.apaga_projeto_view, name="apaga_projeto"),
    path('disciplina/nova', views.nova_disciplina_view, name="nova_disciplina"),
    path('docente/novo', views.novo_docente_view, name="novo_docente"),
    path('tecnologias/', views.tecnologias_view, name='tecnologias'),
    path('tecnologias/<int:tecnologia_id>', views.tecnologia_view, name='tecnologia_path'),
    path('tecnologias/nova', views.nova_tecnologia_view, name="nova_tecnologia"),
    path('tecnologias/<int:tecnologia_id>/edita', views.edita_tecnologia_view, name="edita_tecnologia"),
    path('tecnologias/<int:tecnologia_id>/apaga', views.apaga_tecnologia_view, name="apaga_tecnologia"),
    path('cv/', views.cv_view, name='cv'),
]