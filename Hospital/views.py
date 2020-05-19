from django.shortcuts import render

# Create your views here.

# Criando a rotas para index
def index(request):
    return render(request, 'index.html')

# Criando a rota para paciente.html
def paciente(request):
    return render(request, 'paciente.html')

# Criando a rota para medico.html
def medico(request):
    return render(request, 'medico.html')