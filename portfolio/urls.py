from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('interests/', views.interesses_view, name='interesses'),
    path('projects/', views.projetos_view, name='projetos'),
    path('projects/<slug:projeto_slug>/', views.projeto_view, name='projeto_path'),
    path('projects/new/', views.novo_projeto_view, name="novo_projeto"),
    path('projects/<slug:projeto_slug>/edit/', views.edita_projeto_view, name="edita_projeto"),
    path('projects/<slug:projeto_slug>/delete/', views.apaga_projeto_view, name="apaga_projeto"),
    path('course/new/', views.nova_disciplina_view, name="nova_disciplina"),
    path('teacher/new/', views.novo_docente_view, name="novo_docente"),
    path('technologies/', views.tecnologias_view, name='tecnologias'),
    path('technologies/<slug:tecnologia_slug>/', views.tecnologia_view, name='tecnologia_path'),
    path('technologies/new/', views.nova_tecnologia_view, name="nova_tecnologia"),
    path('technologies/<slug:tecnologia_slug>/edit/', views.edita_tecnologia_view, name="edita_tecnologia"),
    path('technologies/<slug:tecnologia_slug>/delete/', views.apaga_tecnologia_view, name="apaga_tecnologia"),
    path('cv/', views.cv_view, name='cv'),
    path('contact/', views.contacto_view, name='contacto'),
]