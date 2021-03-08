from django.urls import path
from . import views

app_name = 'pays'

urlpatterns = [
    path('', views.index, name='index'),
    path('pagamentos/', views.pay, name='pay'),
    path('confirmar/<int:id>', views.confirmar, name='confirmar'),
    path('info/', views.info, name='info'),
    path('comentario/', views.comentario, name='comentario'),
    path('listas/', views.listas, name='listas'),
    path('res/', views.res, name='res'),
    path('oitava/', views.oita, name='oita'),
    path('nona/', views.nona, name='nona'),
    path('decima/', views.dec, name='dec'),
    path('onze/', views.onze, name='onze'),
]
