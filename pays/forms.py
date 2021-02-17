from django import forms
from .models import Pagar, Comentario

class PagarForm(forms.ModelForm):

    class Meta:
        model = Pagar
        fields = ['classe', 'nome','valor', 'mes']

class ComentarioForm(forms.ModelForm):

    class Meta:
        model= Comentario
        fields = ['opiniao']