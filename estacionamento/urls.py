from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu_principal, name='menu_principal'),
    path('lista_vagas', views.lista_vagas, name='lista_vagas'),
    path('vaga/<int:pk>/', views.detalhe_vaga, name='detalhe_vaga'),
]