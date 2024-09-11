from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


def login_view(request):
    return render(request, 'Formulariologin.html')
def logins_sucesso_view(request):
    contexto = {
        "email": request.GET.get("email"),
        "senha": request.GET.get("senha"),
    }
    return render(request, 'logins_sucesso.html', contexto)
