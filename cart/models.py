from django.conf import settings
from django.db import models
from app.models import Produto
from django.urls import reverse

# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    
    def __str__(self):
        return f"Carrinho de {self.user.username}"

    def get_absolute_url(self):
        return reverse("cart:cart_detail")
