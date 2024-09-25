from django.http import HttpResponse # type: ignore
from django.shortcuts import render, get_object_or_404 # type: ignore
from .models import Cartao

def detalhes_cartao(request, id):
    cartao = get_object_or_404(Cartao, id=id)
    return render(request, 'detalhes_cartao.html', {'cartao': cartao})


def pagina1(request):
    return HttpResponse("Olá Mundo")

def pagina2(request):
    return HttpResponse("Bem-vindo à Batcaverna")

def Batcaverna(request):
    if request.method == 'POST':
        contexto = {
            "nome": request.POST.get("nome"),
            "cliente": request.POST.get("cliente"),
            "valor": request.POST.get("valor"),
            "mensagem": request.POST.get("mensagem"),
        }
        return render(request, 'Batcaverna.html', contexto)
    else:
        return HttpResponse("Método não permitido", status=405)

def formulario(request):
    return render(request, 'formulario.html')


def criacao_produto(request):
    return render(request, 'criacao_produto.html')

def tela_venda(request):
    return render(request, 'tela_venda.html')