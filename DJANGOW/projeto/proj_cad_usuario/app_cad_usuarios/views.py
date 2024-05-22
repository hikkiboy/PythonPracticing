from django.shortcuts import render
from .models import Usuario

# Create your views here.
def home(request):
    return render(request, 'usuarios/home.html')
def usuarios(request):
    #pega os dados da tela
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()

    #gera lista de users

    usuarios = {
        'usuarios': Usuario.objects.all()
    }

    #trazer os dados na tela

    return render (request,'usuarios/usuarios.html',usuarios)

