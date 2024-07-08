"""
Configurações de URL para projeto ifsp_arduino.

A lista `urlpatterns` roteia URLs para visualizações. Para mais informações consulte:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Exemplos:
Função views
    1. Adicione a importação:  from my_app import views
    2. Adicione a URL em urlpatterns:  path('', views.home, name='home')
Views baseada em uma classe:
    1. Adicione a importação:  from other_app.views import Home
    2. Adicione a URL em urlpatterns:  path('', Home.as_view(), name='home')
Incluindo outra configuração de URL:
    1. Importe a função include(): from django.urls import include, path
    2. Adicione a URL em urlpatterns:  path('blog/', include('blog.urls'))
"""
#from django.contrib import admin
from django.urls import path
from labclima import views
from django.urls import re_path
from django.views.static import serve
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage
from django.conf import settings

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('imagens/favicon.ico'))),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    path('', views.lab, name='lab'),
    path('estacoes/', views.estacoes, name='estacoes'),
    path('registros/', views.registros, name='registros'),
    path('registrar/', views.registrar, name='registrar'),
    path('apagar/', views.apagar, name='apagar'),
    path('imagem/<str:img>', views.imagem, name="imagem")
]
