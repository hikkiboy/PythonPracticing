from django.shortcuts import render
from .models import Produto

# Create your views here.
def home(request):
    return render(request, 'produtos/home.html')

def cadastrar(request):
    return render(request, 'produtos/cadastrar.html')

def listagem(request):
    new_produto = Produto()
    new_produto.descricao = request.POST.get('descricao')
    new_produto.marca = request.POST.get('marca')
    new_produto.valor = request.POST.get('valor')
    new_produto.estoque = request.POST.get('estoque')

    new_produto.save()
    Produtos = {
        'Produtos': Produto.objects.all()
    }
    return render(request, 'produtos/listagem.html',Produtos)
