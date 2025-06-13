from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('sobre/', views.sobre_view, name='sobre'),
    path('interesses/', views.interesses_view, name='interesses'),
    path('projetos/', views.projetos_view, name='projetos'),
    path('projetos/<int:projeto_id>/', views.projeto_view, name='projeto_path'),
    path('projetos/novo', views.novo_projeto_view,name="novo_projeto"),
    path('projetos/<int:projeto_id>/edita', views.edita_projeto_view,name="edita_projeto"),
    path('projetos/<int:projeto_id>/apaga', views.apaga_projeto_view,name="apaga_projeto"),
    path('disciplina/nova', views.nova_disciplina_view,name="nova_disciplina"),
    path('docente/novo', views.novo_docente_view,name="novo_docente"),
    path('tecnologias/', views.tecnologias_view, name='tecnologias'),
    path('tecnologias/<int:tecnologia_id>', views.tecnologia_view, name='tecnologia_path'),
    path('tecnologias/nova', views.nova_tecnologia_view,name="nova_tecnologia"),
    path('tecnologias/<int:tecnologia_id>/edita', views.edita_tecnologia_view,name="edita_tecnologia"),
    path('tecnologias/<int:tecnologia_id>/apaga', views.apaga_tecnologia_view,name="apaga_tecnologia"),
    path('cv/', views.cv_view, name='cv'),
    path('testes/', views.testes_view, name='testes'),

    # Login
    path('registo/', views.registo_view, name="registo"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('login-magic/', views.login_magic_link, name='login_magic_link'),
    path('autentica/', views.autentica_view, name='autentica'),
    path('user/', views.user_view, name='user'),
    # Artigos
    path('posts/', views.posts_view, name='posts'),
    path('posts/<int:post_id>/', views.post_view, name='post_path'),
    path('posts/novo', views.novo_post_view, name='novo_post'),
    path('autor/novo', views.novo_autor_view, name='novo_autor'),
    path('posts/<int:post_id>/edita', views.edita_post_view, name='edita_post'),
    path('posts/<int:post_id>/apaga', views.apaga_post_view, name='apaga_post'),

    # Defesa
    path('interessesdefesa/', views.interessesdefesa_view, name='interessesdefesa'),
    path('interesses/<int:interesse_id>/', views.interesse_view, name='interesse'),
    path('interesses/novo', views.novo_interesse_view,name="novo_interesse"),
    path('interesses/<int:interesse_id>/edita', views.edita_interesse_view,name="edita_interesse"),
    path('interesses/<int:interesse_id>/apaga', views.apaga_interesse_view,name="apaga_interesse"),
    
    # APIs
    path('apis/', views.apis_view, name='apis'),
    path('bandas/', views.bandas_externas, name='bandas_externas'),
    path('albuns/', views.albuns_externos, name='albuns_externos'),
    path('musicas/', views.musicas_externas, name='musicas_externas'),
    path('bandas/<int:banda_id>/', views.bandas_externas_id, name='bandas_externas_id'),
    path('albuns/<int:album_id>/', views.albuns_externos_id, name='albuns_externos_id'),
    path('musicas/<int:musica_id>/', views.musicas_externas_id, name='musicas_externas_id'),
    path('bandas/criar/', views.criar_banda_externa, name='criar_banda_externa'),
    path('bandas/<int:banda_id>/editar/', views.editar_banda_externa, name='editar_banda_externa'),
    path('bandas/<int:banda_id>/apagar/', views.apagar_banda_externa, name='apagar_banda_externa'),
    path('albuns/criar/', views.criar_album_externo, name='criar_album_externo'),
    path('albuns/<int:album_id>/editar/', views.editar_album_externo, name='editar_album_externo'),
    path('albuns/<int:album_id>/apagar/', views.apagar_album_externo, name='apagar_album_externo'),
    path('musicas/criar/', views.criar_musica_externa, name='criar_musica_externa'),
    path('musicas/<int:musica_id>/editar/', views.editar_musica_externa, name='editar_musica_externa'),
    path('musicas/<int:musica_id>/apagar/', views.apagar_musica_externa, name='apagar_musica_externa'),
]