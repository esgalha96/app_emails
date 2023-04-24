from django.shortcuts import render
from .models import Emails
from django.contrib import messages

def index(request):

    if request.method == 'POST':
        email = request.POST.get('email')

        try:
            novo_email = Emails.objects.create(email=email)

            if novo_email:
                messages.add_message(request, messages.constants.SUCCESS, "E-mail cadastrado com sucesso!")
            else:
                messages.add_message(request, messages.constants.ERROR, "E-mail inválido ou já cadastrado!")

        except Exception as e:
            messages.add_message(request, messages.constants.ERROR, "E-mail inválido ou já cadastrado!")

    return render(request, 'index.html')
