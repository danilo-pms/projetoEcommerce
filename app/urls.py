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
    path("gerencia/", gerencia, name='gerencia')
       
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)