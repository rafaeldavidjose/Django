from .models import Visitante
from django.core.mail import send_mail

def registar_visitante(request):
    if not request.session.session_key:
        request.session.save()

    session_key = request.session.session_key
    ip = request.META.get('REMOTE_ADDR')

    if session_key and not Visitante.objects.filter(session_key=session_key).exists():
        Visitante.objects.create(ip=ip, session_key=session_key)

    return Visitante.objects.count()

def envia_email(user, email, token):
    send_mail(
        subject='Portfolio ManfelDev: Authentication',
        message=f'Dear {user.first_name}, click on the link '
                f'https://a22202078.pythonanywhere.com/portfolio/autentica/?token={token} '
                'to enter the Portfolio application.',

        from_email='email.app@me.com',

        recipient_list=[email]
    )