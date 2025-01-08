from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, render, redirect
from app.forms import ProdutoForm, CategoriaForm
from .models import *
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# CRUD - produtos
def listar_produto(request):
    # Inicializa todos os produtos
    produtos = Produto.objects.all()
    
    # Filtra por nome, marca, categoria e quantidade em estoque
    nome = request.GET.get('nome', '')
    marca = request.GET.get('marca', '')
    categoria = request.GET.get('categoria', '')
    quantidade_estoque = request.GET.get('quantidade_estoque', '')

    if nome:
        produtos = produtos.filter(nome__icontains=nome)
    if marca:
        produtos = produtos.filter(marca__icontains=marca)
    if categoria:
        produtos = produtos.filter(categoria__nome__icontains=categoria)
    

    # Paginação
    paginator = Paginator(produtos, 3)
    page = request.GET.get('page')
    produtos_pag = paginator.get_page(page)

    context = {
        'produtos_pag': produtos_pag,
        'nome': nome,
        'marca': marca,
        'categoria': categoria,
        'quantidade_estoque': quantidade_estoque,
    }
    
    return render(request, 'app/lista_produtos.html', context)


def listar_categoria(request):
    categorias = Categoria.objects.all()
    
    paginator = Paginator(categorias, 3)  # Adjust the number of items per page here
    page = request.GET.get('page')
    categorias_pag = paginator.get_page(page)

    context = {
        'categorias_pag': categorias_pag,
    }

    return render(request, 'app/lista_categorias.html', context)


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
            return redirect("app:listar_produtos")
        else:
           print(form.errors)
    else:
        form = ProdutoForm()
    context = {'form': form}
    return render(request, 'app/add_produto.html', context)

def add_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("app:gerencia")
        else:
           print(form.errors)
    else:
        form = CategoriaForm()
    context = {'form': form}
    return render(request, 'app/add_categoria.html', context)


# Editar produtos
def atualizar(request, id):
    produto = get_object_or_404(Produto, id=id)

    if request.method == "POST":
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect("app:gerencia")
    else:
        form = ProdutoForm(instance=produto)
    
    context = {'form': form, 
               'produto': produto}
    return render(request, "app/add_produto.html", context)

def att_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)

    if request.method == "POST":
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect("app:gerencia")
    else:
        form = CategoriaForm(instance=categoria)
    
    context = {'form': form, 
               'produto': categoria}
    return render(request, "app/add_categoria.html", context)

def deletar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    categoria.delete()

    return redirect("app:gerencia")

# Remover produtos
def deletar_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    produto.delete()

    return redirect("app:gerencia")


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

from django.shortcuts import render, get_object_or_404
from django.conf import settings
from .models import Produto, Order, OrderItem
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


from django.shortcuts import render, get_object_or_404
from django.conf import settings
from .models import Produto, Order, OrderItem
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def buy_product(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    usuario = request.user
    quantidade = int(request.GET.get('quantidade', 1))
    preco_total = produto.preco * quantidade

    # Criar um novo pedido
    pedido = Order(user=usuario, frete=0)
    pedido.save()

    # Adicionar item ao pedido
    order_item = OrderItem(produto=produto, order=pedido, qtd=quantidade, preco=produto.preco)
    order_item.save()

    # Calcular o preço total do pedido
    pedido.preco_total = sum(item.qtd * item.preco for item in pedido.orderitem_set.all())
    pedido.save()

    return HttpResponse(f'Pedido realizado: Pedido #{pedido.id} para {usuario.username}')
