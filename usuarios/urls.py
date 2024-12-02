from django.urls import path
from .views import cadastro, login_view, logout_view

app_name = 'usuarios'
urlpatterns = [
    path('cadastro/', cadastro, name='cadastro'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]