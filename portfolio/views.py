from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from datetime import date
from .models import *
from .forms import *
from django.core.mail import send_mail
from django.contrib import messages


def index_view(request):
    context = {
        'data': date.today().year,
    }
    return render(request, "portfolio/index.html", context)

def interesses_view(request):
    context = {
        'data' : date.today().year,
    }
    return render(request, "portfolio/interesses.html", context)

def projetos_view(request):
    
    projetos_ordenados = Projeto.objects.all().order_by('ordem', 'titulo')
    
    context = {
        'data' : date.today().year,
        'projetos' : projetos_ordenados,
    }
    return render(request, 'portfolio/projetos.html', context)

def projeto_view(request, projeto_slug):
    projeto = get_object_or_404(Projeto, slug=projeto_slug)
    context = {
        'data' : date.today().year,
        'projeto' : projeto,
    }
    return render(request, 'portfolio/projeto.html', context)

def tecnologias_view(request):
    
    tecnologias_ordenadas = Tecnologia.objects.annotate(
        num_projetos=Count('projetos')
    ).order_by('-num_projetos', 'nome')

    context = {
        'data' : date.today().year,
        'tecnologias' : tecnologias_ordenadas,
    }
    return render(request, 'portfolio/tecnologias.html', context)

def tecnologia_view(request, tecnologia_slug):
    tecnologia = get_object_or_404(Tecnologia, slug=tecnologia_slug)
    
    projetos_ordenados = tecnologia.projetos.all().order_by('ordem', 'titulo')
    
    context = {
        'data' : date.today().year,
        'tecnologia' : tecnologia,
        'projetos_da_tecnologia': projetos_ordenados,
    }
    return render(request, 'portfolio/tecnologia.html', context)

def cv_view(request):
    context = {
        'data' : date.today().year,
    }
    return render(request, 'portfolio/cv.html', context)

@login_required
def novo_projeto_view(request):
    if request.method == 'POST':
        projeto_form = ProjetoForm(request.POST, request.FILES)
        ficha_form = FichaTecnicaForm(request.POST)
        imagem_formset = ImagemProjetoFormSet(request.POST, request.FILES, prefix='imagens')

        if projeto_form.is_valid() and ficha_form.is_valid() and imagem_formset.is_valid():
            projeto = projeto_form.save()
            ficha = ficha_form.save(commit=False)
            ficha.projeto = projeto
            ficha.save()
            imagens = imagem_formset.save(commit=False)
            for imagem in imagens:
                imagem.projeto = projeto
                imagem.save()
            return redirect('portfolio:projetos')
    else:
        projeto_form = ProjetoForm()
        ficha_form = FichaTecnicaForm()
        imagem_formset = ImagemProjetoFormSet(prefix='imagens')

    context = {
        'form': projeto_form,
        'ficha_form': ficha_form,
        'imagens': imagem_formset,
        'data': date.today().year,
    }
    return render(request, 'portfolio/novo_projeto.html', context)

@login_required
def nova_tecnologia_view(request):
    if request.method == 'POST':
        form = TecnologiaForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            return redirect('portfolio:tecnologias')
    else:
        form = TecnologiaForm()

    context = {
        'form': form,
        'data': date.today().year,
    }
    return render(request, 'portfolio/nova_tecnologia.html', context)

@login_required
def nova_disciplina_view(request):
    if request.method == 'POST':
        form = DisciplinaForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            return redirect('portfolio:novo_projeto')
    else:
        form = DisciplinaForm()

    context = {
        'form': form,
        'data': date.today().year,
    }
    return render(request, 'portfolio/nova_disciplina.html', context)

@login_required
def novo_docente_view(request):
    if request.method == 'POST':
        form = DocenteForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            return redirect('portfolio:nova_disciplina')
    else:
        form = DocenteForm()

    context = {
        'form': form,
        'data': date.today().year,
    }
    return render(request, 'portfolio/novo_docente.html', context)

@login_required
def edita_projeto_view(request, projeto_slug):
    projeto = get_object_or_404(Projeto, slug=projeto_slug)
    ficha_tecnica = getattr(projeto, 'ficha_tecnica', None)

    projeto_form = ProjetoForm(request.POST or None, request.FILES or None, instance=projeto)
    ficha_form = FichaTecnicaForm(request.POST or None, instance=ficha_tecnica)
    imagem_formset = ImagemProjetoFormSet(request.POST or None, request.FILES or None, instance=projeto, prefix='imagens')

    if request.method == 'POST':
        if projeto_form.is_valid() and ficha_form.is_valid() and imagem_formset.is_valid():
            projeto = projeto_form.save()
            ficha = ficha_form.save(commit=False)
            ficha.projeto = projeto
            ficha.save()

            imagens = imagem_formset.save(commit=False)
            for imagem in imagens:
                imagem.projeto = projeto
                imagem.save()

            for obj in imagem_formset.deleted_objects:
                obj.delete()

            return redirect('portfolio:projeto_path', projeto_slug=projeto.slug)

    context = {
        'form': projeto_form,
        'ficha_form': ficha_form,
        'imagens': imagem_formset,
        'projeto': projeto,
        'data': date.today().year,
    }
    return render(request, 'portfolio/edita_projeto.html', context)

@login_required
def edita_tecnologia_view(request, tecnologia_slug):
    tecnologia = get_object_or_404(Tecnologia, slug=tecnologia_slug)

    form = TecnologiaForm(request.POST or None, request.FILES or None, instance=tecnologia)

    if form.is_valid():
        form.save()

        return redirect('portfolio:tecnologia_path', tecnologia_slug=tecnologia.slug)

    context = {
        'form': form,
        'tecnologia': tecnologia,
        'data': date.today().year,
    }

    return render(request, 'portfolio/edita_tecnologia.html', context)

@login_required
def apaga_projeto_view(request, projeto_slug):
    projeto = get_object_or_404(Projeto, slug=projeto_slug)
    projeto.delete()
    return redirect('portfolio:projetos')

@login_required
def apaga_tecnologia_view(request, tecnologia_slug):
    tecnologia = get_object_or_404(Tecnologia, slug=tecnologia_slug)
    tecnologia.delete()
    return redirect('portfolio:tecnologias')

def envia_email_contacto(nome, email, assunto, mensagem):
    send_mail(
        subject=f'Portfolio: {assunto}',
        message=f'Nome: {nome}\nEmail: {email}\n\nMensagem:\n{mensagem}',
        from_email='rafaeldavidjose.dev@gmail.com',
        recipient_list=['rafaeldavidjose.dev@gmail.com']
    )


def contacto_view(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            
            contacto = form.save()

            
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            assunto = form.cleaned_data['assunto']
            mensagem = form.cleaned_data['mensagem']

            
            
            
            

            try:
                
                from django.core.mail import send_mail
                send_mail(
                    subject=f'[PORTFOLIO] {assunto}',
                    message=f'Nome: {nome}\nEmail: {email}\n\nMensagem:\n{mensagem}',
                    from_email='noreply@portfolio.com',
                    recipient_list=['rafaeldavidjose.dev@gmail.com'],
                    fail_silently=True,  
                )
                email_status = "Email enviado!"
            except:
                email_status = "Email salvo no admin (SMTP indisponível)"

            
            messages.success(request,
                f'✅ Message received successfully! '
                f'I can see it in my admin panel and will respond within 24-48 hours. '
                f'Status: {email_status}')

            return redirect('portfolio:contacto')

    else:
        form = ContactoForm()

    context = {
        'form': form,
        'data': date.today().year,
    }
    return render(request, 'portfolio/contacto.html', context)