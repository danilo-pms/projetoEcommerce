from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, render, redirect
from app.forms import ProdutoForm, ProdutoFilterForm
from .models import *
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# CRUD - produtos
def index(request):
    # Inicializa todos os produtos
    produtos = Produto.objects.all()
    
    # Filtra se "nome" estiver presente nos parâmetros GET
    nome = request.GET.get('nome', '')  # Obtém o valor da barra de pesquisa
    if nome:
        produtos = produtos.filter(nome__icontains=nome)
    
    # Paginação
    paginator = Paginator(produtos, 3)
    page = request.GET.get('page')
    produtos_pag = paginator.get_page(page)

    context = {
        'produtos_pag': produtos_pag,
        'nome': nome,  # Envia o valor pesquisado para o template (opcional)
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


@login_required(login_url='usuarios:login')
def gerencia(request):
    if not request.user.is_staff:
        # Se não for um administrador: code 403
        return HttpResponseForbidden(
            "Acesso negado. Esta página é reservada para administradores."
        )
        
    produtos = Produto.objects.count()
    categorias = Categoria.objects.count()
    
    context = {
        'quantidade_produtos': produtos,
        'quantidade_categorias': categorias
    }
    return render(request, "app/gerencia.html", context)
