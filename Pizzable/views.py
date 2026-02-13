from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def toppings_list(request):
    return HttpResponse("Your preferred topping is Pineapples")