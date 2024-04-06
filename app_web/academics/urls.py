from django import paht
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name='idex', name='list_person'),
]