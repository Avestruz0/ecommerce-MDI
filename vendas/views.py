from django.shortcuts import render
from django.http import HttpResponse

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