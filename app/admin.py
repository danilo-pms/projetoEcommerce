from django.contrib import admin
from .models import Categoria, Produto, Order, OrderItem

# Registro de Categoria 
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'created_at', 'updated_at')
    search_fields = ('nome',)


# Registro de Produto
@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'marca', 'categoria', 'preco', 'qtd_estoque', 'created_at', 'updated_at')
    search_fields = ('nome', 'marca')
    list_filter = ('categoria',)


"""# Registro de Cart 
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'finalizado', 'created_at', 'updated_at')
    list_filter = ('finalizado', 'created_at')
    search_fields = ('user__username',)


# Registro de CartItem 
@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('carrinho', 'produto', 'qtd', 'preco')
    search_fields = ('produto__nome', 'carrinho__user__username')
    list_filter = ('carrinho__finalizado',)
"""

# Registro de Order 
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'status', 'pagamento', 'frete', 'created_at', 'updated_at')
    list_filter = ('status', 'created_at', 'updated_at')
    search_fields = ('user__username',)


# Registro de OrderItem 
@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'produto', 'qtd', 'preco')
    search_fields = ('produto__nome', 'order__user__username')
