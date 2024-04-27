from django.shortcuts import render

# Create your views here.from django.shortcuts import render
from django.http import HttpResponse
from .models import clientes,Producto,cliente_producto,Tipo_transancciones,Transaccion

# Create your views here.

def index(request):
    return HttpResponse("::: BIENVENIDO A FINANCE :::")

def list_cliente(request):
    #return HttpResponse("::: Listar Usuario :::")
    cliente = clientes.objects.all()
    return render(request, 'finance\listar_cliente.html',{'clientes':cliente})

def list_product(request):
    productos = Producto.objects.all()
    return render(request, 'finance\listar_cliente.html',{'producto':productos})

def list_clienteproduct(request):
    clientes_productos = cliente_producto.objects.all()
    return render(request, 'finance\listar_cliente.html',{'producto':clientes_productos})

def list_ttransaccion(request):
    tipos_transacciones =Tipo_transancciones.objects.all()
    return render(request, 'finance\listar_cliente.html',{'producto':tipos_transacciones})

def list_transaccion(request):
    transacciones = Transaccion.objects.all()
    return render(request, 'finance\listar_cliente.html',{'producto':transacciones})


def create_cliente(request):
    return HttpResponse("::: Usuario Creado :::")
