
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from app.forms import ProdutoForm
from .models import *
# Create your views here.

# CRUD - produtos
def index(request): 
    produtos = Produto.objects.all()
    
    return render(request, 'app/index.html', {'produtos':produtos})
    
 
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



# Sistema de autenticação
def cadastro(request):
    if request.method == "POST":
        # Puxa dados do formulario
        nome = request.POST.get("nome")
        senha = request.POST.get("senha")

        # Novo usuario usando modelo User do Django
        user = User.objects.create_user(nome, "", senha)
        user.save()

        return redirect("index")
    return render(request, "app/cadastro.html")


def login(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        senha = request.POST.get("senha")
        
        user = authenticate(request, username=nome, password=senha)

        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            return redirect("login")

    return render(request, "app/login.html")


def logout(request):
    logout(request)
    return redirect("index")