from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index_view),
    path('helloworld/', views.helloworld_view),
    path('teste/', views.teste_view),
    path('djkhaled/', views.djkhaled_view),
]