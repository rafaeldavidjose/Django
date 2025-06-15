from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from datetime import date
from .models import *
from .forms import *
from django.core.mail import send_mail
from django.contrib import messages

# Create your views here.
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
    context = {
        'data' : date.today().year,
        'projetos' : Projeto.objects.all(),
    }
    return render(request, 'portfolio/projetos.html', context)

def projeto_view(request, projeto_id):
    context = {
        'data' : date.today().year,
        'projeto' : Projeto.objects.get(id=projeto_id),
    }
    return render(request, 'portfolio/projeto.html', context)

def tecnologias_view(request):
    # Ordena tecnologias por número de projetos (descendente) e depois por nome
    tecnologias_ordenadas = Tecnologia.objects.annotate(
        num_projetos=Count('projetos')
    ).order_by('-num_projetos', 'nome')
    
    context = {
        'data' : date.today().year,
        'tecnologias' : tecnologias_ordenadas,
    }
    return render(request, 'portfolio/tecnologias.html', context)

def tecnologia_view(request, tecnologia_id):
    context = {
        'data' : date.today().year,
        'tecnologia' : Tecnologia.objects.get(id=tecnologia_id),
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
def edita_projeto_view(request, projeto_id):
    projeto = Projeto.objects.get(id=projeto_id)
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

            return redirect('portfolio:projeto_path', projeto_id=projeto.id)

    context = {
        'form': projeto_form,
        'ficha_form': ficha_form,
        'imagens': imagem_formset,
        'projeto': projeto,
        'data': date.today().year,
    }
    return render(request, 'portfolio/edita_projeto.html', context)

@login_required
def edita_tecnologia_view(request, tecnologia_id):
    tecnologia = Tecnologia.objects.get(id=tecnologia_id)

    form = TecnologiaForm(request.POST or None, request.FILES or None, instance=tecnologia)

    if form.is_valid():
        form.save()

        return redirect('portfolio:tecnologia_path', tecnologia_id=tecnologia.id)

    context = {
        'form': form,
        'tecnologia': tecnologia,
        'data': date.today().year,
    }

    return render(request, 'portfolio/edita_tecnologia.html', context)

@login_required
def apaga_projeto_view(request, projeto_id):
    projeto = Projeto.objects.get(id=projeto_id)
    projeto.delete()
    return redirect('portfolio:projetos')

@login_required
def apaga_tecnologia_view(request, tecnologia_id):
    tecnologia = Tecnologia.objects.get(id=tecnologia_id)
    tecnologia.delete()
    return redirect('portfolio:tecnologias')

def contacto_view(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            # Guardar na base de dados
            contacto = form.save()
            
            # Preparar email
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            assunto = form.cleaned_data['assunto']
            mensagem = form.cleaned_data['mensagem']
            
            # Enviar email para ti
            email_subject = f"[PORTFOLIO CONTACT] {assunto}"
            email_message = f"""
Nova mensagem de contacto recebida:

Nome: {nome}
Email: {email}
Assunto: {assunto}

Mensagem:
{mensagem}

---
Enviado através do portfolio: https://rafaeljose.pythonanywhere.com/
Data: {contacto.data_envio.strftime('%d/%m/%Y às %H:%M')}
"""
            
            try:
                send_mail(
                    subject=email_subject,
                    message=email_message,
                    from_email='noreply@rafaeljose.pythonanywhere.com',
                    recipient_list=['rafaeldavidjose.dev@gmail.com'],
                    fail_silently=False,
                )
                messages.success(request, 'Message sent successfully! I\'ll get back to you soon.')
                return redirect('portfolio:contacto')
            except Exception as e:
                messages.error(request, 'Sorry, there was an error sending your message. Please try again.')
    else:
        form = ContactoForm()
    
    context = {
        'form': form,
        'data': date.today().year,
    }
    return render(request, 'portfolio/contacto.html', context)