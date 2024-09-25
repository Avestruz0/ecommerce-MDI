from django.urls import path 
from . import views

urlpatterns = [
    path('', views.pagina1, name="Pagina1"),
    path('pagina2/', views.pagina2, name="Pagina2"),
    path('Batcaverna/', views.Batcaverna, name="Batcaverna"),
    path('formulario/', views.formulario, name="formulario"),
    path('criacao_produto/', views.criacao_produto, name="criacao_produto"),
    path('tela_venda/', views.tela_venda, name="tela_venda"),
    path('detalhes/<int:id>/', views.detalhes_cartao, name="detalhes_cartao"),
]

