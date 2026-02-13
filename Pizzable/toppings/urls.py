from django.urls import path
from toppings import views

urlpatterns =[
    path('', views.toppings_list, name="toppings_list")
]