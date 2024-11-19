from django.urls import path
from .views import *

urlpatterns = [
    path('',home, name= "home"),
    path("list/", todo_list, name = "todo_list"),
    path("add/", add, name = "add"),
    path("delete/<id>/", delete, name="delete"),
    path('update/<id>/', update, name="update"),
]
