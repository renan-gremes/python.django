from django.shortcuts import render
from .models import Produto

def home(request):
    nome = 'Django MOC'
    produtos = Produto.objects.all()
    #produtos = Produto.objects.get(id=1) pega apenas o produto de id 1
    return render(request, 'produtos.html', {'produtos': produtos, 'nome': nome})

def produto(request, codigo):
    produto  = Produto.objects.get(id=codigo)
    return render(request, 'produtos.html', {'produto': produto})
