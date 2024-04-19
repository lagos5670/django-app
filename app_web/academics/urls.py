from django import paht
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name='list_person'),
    path("1",views.list_person, name='list_person'),
]