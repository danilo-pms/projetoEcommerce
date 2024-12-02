
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from app.forms import ProdutoForm
from .models import *
# Create your views here.

# Paginação
from django.core.paginator import Paginator


# CRUD - produtos
def index(request): 
    produtos = Produto.objects.all()
    
    # Paginação
    paginator = Paginator(produtos,3)
    page = request.GET.get('page')
    produtos_pag = paginator.get_page(page) 
    context = {
        'produtos_pag': produtos_pag
    }
    return render(request, 'app/index.html', context)
    
 
# Adicionar produtos   
def add_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("index")
        else:
           print(form.errors)
    else:
        form = ProdutoForm()
    context = {'form': form}
    return render(request, 'app/add_produto.html', context)


# Editar produtos
def atualizar(request, id):
    produto = get_object_or_404(Produto, id=id)

    if request.method == "POST":
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = ProdutoForm(instance=produto)
    
    context = {'form': form, 
               'produto': produto}
    return render(request, "app/add_produto.html", context)


# Remover produtos
def deletar_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    produto.delete()

    return redirect("index")


def detalhes(request, id):
    produto = Produto.objects.get(id=id)
    context = {'produto': produto}

    return render(request, "app/details.html", context)
