from django.conf import settings
from django.db import models

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=100, unique=True, null=False, blank=False)
    descricao = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=150, null=False, blank=False)
    marca = models.CharField(max_length=150, null=True, blank=True)
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE, null=True)
    descricao = models.TextField(null=True, blank=True)
    preco = models.DecimalField(max_digits=12, decimal_places=2, null=False, blank=False)
    qtd_estoque = models.IntegerField(default=0)
    imagem = models.ImageField(upload_to='img/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    pagamento = models.CharField(max_length=200, null=True, blank=True)
    frete = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ('pending', 'Pending'),
            ('paid', 'Paid'),
            ('shipped', 'Shipped'),
            ('delivered', 'Delivered'),
            ('canceled', 'Canceled')
        ],
        default='pending'
    )
    paidAt = models.DateTimeField(null=True, blank=True)
    envioAt = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Pedido #{self.id} de {self.user.username}"

class OrderItem(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    qtd = models.IntegerField(default=1)
    preco = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"{self.produto.nome} - {self.qtd} unidades"
