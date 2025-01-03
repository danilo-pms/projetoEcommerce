from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Cart
from app.models import Produto

# Create your views here.
from django.shortcuts import get_object_or_404

@login_required
def add_to_cart(request, product_id):
    produto = get_object_or_404(Produto, id=product_id)
    cart_item = Cart.objects.filter(user=request.user, product=produto).first()

    if cart_item:
        cart_item.quantity += 1
        cart_item.save()
        messages.success(request, 'Item adicionado ao carrinho')
        
    else:
        Cart.objects.create(user=request.user, product=produto)
        messages.success(request, 'Item adicionado ao carrinho')
        
    return redirect("cart:cart_detail")


@login_required
def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(Cart, id=cart_item_id)
    
    if cart_item.user == request.user:
        cart_item.delete()
        messages.success(request, 'Item removido do carrinho')
        
    return redirect('cart:cart_detail')

@login_required
def cart_detail(request):
    cart_items = Cart.objects.filter(user=request.user)
    total_price = sum(item.quantity * item.product.preco for item in cart_items)
    for item in cart_items: item.total_price = item.quantity * item.product.preco

    context = {
        "cart_items": cart_items,
        "total_price": total_price,
    }

    return render(request, "cart/cart_detail.html", context)