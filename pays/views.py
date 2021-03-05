from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

from.models import Pagar, Comentario
from .forms import PagarForm, ComentarioForm

def index(request):
    return render(request, 'pays/index.html')

#Cria um formulario do aluno para pagar a mensalidade
@login_required
def pay(request,):
    pay = Pagar.objects.filter(user=request.user)

    # Envia um e-mail automatico a confirmar a transicao


    if request.method == 'POST':

        form = PagarForm(request.POST)
        messages.info(request, 'As informacoes do aluno estao salvas. Agora clique no pay para pagar a mensalidade')

        if form.is_valid():

            pay = form.save(commit=False)
            pay.user = request.user
            pay.save()

            template = render_to_string('pays/email.html',
                                        {'nome': pay.nome, 'classe': pay.classe, 'valor': pay.valor, }, )
            gmail = EmailMessage(
                'Recibo de mensalidade',
                template,
                settings.EMAIL_HOST_USER,
                ['luztecno21@gmail.com', pay.email],
            )

            gmail.fail_silently = False
            gmail.send()

        return redirect('../pagamentos')

    else:
        form = PagarForm()
        return render(request, 'pays/pay.html', {'form': form, 'pay':pay})


def confirmar(request, id):



    pay = get_object_or_404(Pagar, pk=id)
    return render(request, 'pays/confirmar.html', {'pay':pay})

#Da informacoes sobre a escola
def info(request):
    comentario = Comentario.objects.all().order_by('-data')
    return render(request, 'pays/info.html', {'comentario': comentario})

#Cria um formulario para o usuario comentar sobre o site
def comentario(request):
    if request.method == 'POST':

        form = ComentarioForm(request.POST)

        if form.is_valid():
            form.save()
        return redirect('/info/')

    else:
        form = ComentarioForm()
        return render(request, 'pays/comentario.html', {'form': form})

def listas(request):
    return render(request, 'pays/listas.html', )


