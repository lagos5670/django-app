from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("::: CANTINERO BUENAS NOCHES :::")

def list_person(request):
    return HttpResponse("::: Rico pablito sabrosito :::")