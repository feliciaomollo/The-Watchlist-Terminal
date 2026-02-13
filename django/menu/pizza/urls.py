from django.urls import path
from . import views

urlpatterns = [
    path('', views.toppings, name="toppings"),
    path("dough", views.dough, name="dough"),
    path("sauce", views.sauce, name="sauce"),
    path("<str:name>", views.spice, name="spice"),
]
