
from django import path
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name='list_person'),
    path("list",views.list_users, name='list_users'),
    path("list",views.create_users, name='create_user'),
]
 