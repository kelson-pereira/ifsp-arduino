from django.http import HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone
from datetime import timedelta
from .models import Registro
import time

# Exibe a página estações
def estacoes(request):
    seven_days = timezone.now() - timedelta(days = 7)
    registros = {'registros': Registro.objects.filter(datahora__gte=seven_days).values('ident', 'datahora', 'nome', 'temperatura', 'umidade', 'pressao').order_by('datahora').reverse()}
    return render(request, 'estacoes.html', registros)

# Salva o novo registro no banco de dados e apaga o antigo.
# http://127.0.0.1:8000/registrar?nome=ESTAÇÃO ARDUINO 1&cep=12242460&temperatura=22.8&umidade=64.2&pressao=1017
# http://127.0.0.1:8000/registrar?nome=ESTAÇÃO ARDUINO 2&cep=12242460&temperatura=24.3&umidade=53.7&pressao=1013
# http://127.0.0.1:8000/registrar?nome=ESTAÇÃO ARDUINO 3&cep=12242460&temperatura=21.1&umidade=55.5&pressao=1018
# https://labclima-cdf9226ee1c5.herokuapp.com/registrar?nome=ESTAÇÃO ARDUINO 1&cep=12242460&temperatura=22.8&umidade=64.2&pressao=1017

def registrar(request):
    if request.method == "GET":
        try:
            registro = Registro()
            nome = request.GET.get('nome')
            registro.nome = nome
            cep = request.GET.get('cep')
            registro.cep = cep
            registro.temperatura = request.GET.get('temperatura')
            registro.umidade = request.GET.get('umidade')
            registro.pressao = request.GET.get('pressao')
            Registro.objects.filter(nome=nome, cep=cep).delete()
            registro.save()
            #time.sleep(10)
            messages.success(request, 'Registro criado com sucesso.', extra_tags='text-bg-success')
        except:
            messages.error(request, 'O registro não pôde ser criado.', extra_tags='text-bg-danger')
        return HttpResponseRedirect(reverse('registros'))

# Apaga o registro no banco de dados.
def apagar(request):
    if request.method == "POST":
        ident = request.POST.get('ident')
        cep = request.POST.get('cep')
        try:
            registro = Registro.objects.get(ident=ident, cep=cep)
            registro.delete()
            messages.success(request, 'Registro apagado com sucesso.', extra_tags='text-bg-success')
        except:
            messages.error(request, 'O registro não pôde ser apagado.', extra_tags='text-bg-danger')
    return HttpResponseRedirect(reverse('registros'))

# Lista os registros do banco de dados
def registros(request):
    seven_days = timezone.now() - timedelta(days = 7)
    registros = {'registros': Registro.objects.filter(datahora__gte=seven_days).values('ident', 'datahora', 'nome', 'temperatura', 'umidade', 'pressao').order_by('datahora').reverse()}
    return render(request, 'registros.html', registros)
