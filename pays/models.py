from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Pagar(models.Model):
    nome = models.CharField('Nome do aluno', max_length=20)
    classe = models.CharField('Classe e Turma', max_length=20)
    valor = models.DecimalField(max_digits=10, decimal_places=5)
    mes = models.CharField('mês', choices=[('Janeiro', 'Janeiro'), ('Fevereiro', 'Fevereiro'),
                                           ('Março', 'Março'), ('Abril', 'Abril'), ('Maio', 'Maio'), ('Junho', 'Junho'), ('Julho', 'Julho'), ('Agosto', 'Agosto'), ('Setembro', 'Setembro'), ('Outubro', 'Outubro'), ('Novembro', 'Novembro'), ('Desembro', 'Desembro')], max_length=20)
    email = models.EmailField(max_length=50)
    user = models.ForeignKey(get_user_model(), on_delete = models.DO_NOTHING)
    def __str__(self):
        return self.nome

class Comentario(models.Model):
    opiniao = models.TextField()
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.opiniao