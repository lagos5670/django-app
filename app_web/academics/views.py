from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from .forms import UserForm

# Create your views here.

def index(request):
    return HttpResponse("::: CANTINERO BUENAS NOCHES :::")

def list_users(request):
    #return HttpResponse("::: Listar Usuario :::")
    users = User.objects.all()
    return render(request, 'academics\list_user.html',{'users':users})

def create_users(request):
   # return HttpResponse("::: Usuario Creado :::")
    if request.method == "POST":
        form = UserForm (request.POST)
        if form.is_valid():
           form.save()
           #return redirect('list')
        else:
           form = UserForm()

    return render(request, 'academics\create_user.html',{'form':UserForm})

