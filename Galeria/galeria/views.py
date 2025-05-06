from django.utils import timezone
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def sobre(request):
    return render(request, 'sobre.html')

def descricao(request):
    return render(request, 'descricao.html')

def aula(request):
    
    hora_atual = timezone.now().hour
    if hora_atual <= 9 or hora_atual >= 11:
        status_aula = 'em_aula'
    else:
        status_aula = 'fora_da_aula'
    return render(request, 'aula.html', {'status_aula': status_aula})