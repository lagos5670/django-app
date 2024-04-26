from django.shortcuts import render
from django.http import HttpResponse
from .models import User

# Create your views here.

def index(request):
    return HttpResponse("::: CANTINERO BUENAS NOCHES :::")

def list_users(request):
    #return HttpResponse("::: Listar Usuario :::")
    users = User.objects.all()
    return render(request, 'academics\list_user.html',{'users':users})

def create_users(request):
    return HttpResponse("::: Usuario Creado :::")