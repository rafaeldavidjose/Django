from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index_view(request):
    return HttpResponse("Olá n00b, esta é a página web mais básica do mundo!")

def helloworld_view(request):
    return HttpResponse('Hello World!')

def teste_view(request):
    return HttpResponse('Isto é um teste!')

def djkhaled_view(request):
    return HttpResponse('Another One!')