from django.contrib import admin
from django.urls import path, include
from pizzas import views

app_name = 'pizzas'
urlpatterns = [
    path("", views.index, name="index")
]