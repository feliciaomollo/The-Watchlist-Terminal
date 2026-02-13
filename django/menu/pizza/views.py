from django.shortcuts import render
from django.http import HttpResponse

def toppings(request):
    return HttpResponse("Hello, What toppings do you prefer?")

def dough(request):
    return HttpResponse("Do you prefer the vegan dough or john dough?")

def sauce(request):
    return HttpResponse("Saucy or spicy?")

def spice(request, name):
    return render(request, "pizza/spice.html", {
        "name": "Andeezy"
    })
def options(request):
    return render(request, "pizza/options.html")