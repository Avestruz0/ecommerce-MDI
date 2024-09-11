from django.urls import path
from .views import login_view,logins_sucesso_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logins_sucesso/', logins_sucesso_view, name='logins_sucesso'),
]