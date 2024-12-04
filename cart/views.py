from django.shortcuts import render, get_object_or_404, redirect
from app.models import Produto
from .cart import Cart

def add_to_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Produto, id=product_id)
    cart.add(product=product)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/cart_detail.html', {'cart': cart})

def remove_from_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Produto, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

def clear_cart(request):
    cart = Cart(request)
    cart.clear()
    return redirect('cart:cart_detail')
