from django.shortcuts import render

tasks = ["Cleaning", "Cooking", "Resting"]

def thetask(request):
    return render(request, "task/index.html", {
        "tasks": tasks 
    })
def add(request):
    return render(request, "task/add.html")