
from django.urls import path
from . import views

urlpatterns = [
    path('clientes/', views.list_cliente, name='listar_cliente '),
    # Agrega más rutas URL aquí según sea necesario
]
