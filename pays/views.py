from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from.models import Pagar, Comentario
from .forms import PagarForm, ComentarioForm

def index(request):
    return render(request, 'pays/index.html')

@login_required
def pay(request):
    pay = Pagar.objects.filter(user=request.user)
    if request.method == 'POST':

        form = PagarForm(request.POST)
        messages.info(request, 'Mensalidade pagada com sucesso. Verifique o seu recibo na sua conta gmail')

        if form.is_valid():
            pay = form.save(commit=False)
            pay.user = request.user
            pay.save()
        return redirect('/pagamentos/')

    else:
        form = PagarForm()
        return render(request, 'pays/pay.html', {'form': form, 'pay':pay})

def confirmar(request, id):
    pagar = get_object_or_404(Pagar, pk=id)
    return render(request, 'pays/confirmar.html', {'pagar':pagar})


def info(request):
    comentario = Comentario.objects.all().order_by('-data')
    return render(request, 'pays/info.html', {'comentario': comentario})

def comentario(request):
    if request.method == 'POST':

        form = ComentarioForm(request.POST)

        if form.is_valid():
            form.save()
        return redirect('/info/')

    else:
        form = ComentarioForm()
        return render(request, 'pays/comentario.html', {'form': form})


