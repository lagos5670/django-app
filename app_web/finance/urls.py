
from django.urls import path
from . import views

urlpatterns = [
    path('listar/', views.list_cliente, name='list_cliente'),
    # Agrega más rutas URL aquí según sea necesario
]
