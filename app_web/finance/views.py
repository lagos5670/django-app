from django.shortcuts import render

# Create your views here.from django.shortcuts import render
from django.http import HttpResponse
from .models import clientes
''',Producto,cliente_producto,Tipo_transancciones,Transaccion'''

# Create your views here.

def index(request):
    return HttpResponse("::: BIENVENIDO A FINANCE :::")

def list_cliente(request):
    
    cliente = clientes.objects.all()
    return render(request, 'finance/listar_cliente.html',{'cliente':cliente})

'''def list_product(request):
    productos = productos.objects.all()
    return render(request, 'finance/Templante/finance/listar_cliente.html',{'Producto':productos})

def list_clienteproduct(request):
    clientes_productos = clientes_productos.objects.all()
    return render(request, 'finance/Templante/finance/listar_cliente.html',{'cliente_producto':clientes_productos})

def list_ttransaccion(request):
    tipos_transacciones = tipos_transacciones.objects.all()
    return render(request, 'finance/Templante/finance/listar_cliente.html',{'Tipo_transancciones':tipos_transacciones})

def list_transaccion(request):
    transacciones = t.objects.all()
    return render(request, 'finance/Templante/finance/listar_cliente.html',{'Transaccion':transacciones})


def create_cliente(request):
    return HttpResponse("::: Usuario Creado :::")
    
'''

