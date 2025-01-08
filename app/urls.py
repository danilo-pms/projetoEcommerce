from django.contrib import admin 
from django.urls import path
from .views import *
from django.conf.urls.static import static
from core import settings 

app_name = "app"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('create/', add_produto, name='add_produto'),
    path('excluir/<int:id>/', deletar_produto, name='deletar_produto'),  
    path('att/<int:id>/', atualizar, name='atualizar'),
    path('detalhes/<int:id>/', detalhes, name='detalhes'),
    path("gerencia/", gerencia, name='gerencia'),
    path('gerencia/produtos/', listar_produto, name='listar_produtos'),
    path('gerencia/categorias/', listar_categoria, name='listar_categoria'),
    path('create/categoria/', add_categoria, name='add_categoria'),
    path('att/categoria/<int:id>/', att_categoria, name='att_categoria'),
    path('delete/categoria/<int:id>/', deletar_categoria, name='deletar_categoria'),
    path('buy/<int:produto_id>/', buy_product, name='buy_product'),
 
    path('admin/manage_orders/', manage_orders, name='manage_orders'),
    path('admin/update_order_status/<int:order_id>/', update_order_status, name='update_order_status'),

       
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)