"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin 
from django.urls import path, include 
from django.conf.urls.static import static
from . import settings 
from app.views import index, add_produto, atualizar, deletar_produto, detalhes

urlpatterns = [
    path('admin/', admin.site.urls),
    # usuario
    path('a/', include('app.urls')),
    # loja
    path('', index, name='index'),
    path('create/', add_produto, name='add_produto'),
    path('excluir/<int:id>/', deletar_produto, name='deletar_produto'),  
    path('att/<int:id>/', atualizar, name='atualizar'),
    path('detalhes/<int:id>/', detalhes, name='detalhes'),
    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
