from django.shortcuts import render
import datetime

# Create your views here.
def gifts(request):
    now = datetime.datetime.now()
    return render(request, "boxingday/unboxing.html", {
        "boxingday": now.month ==12 and now.day ==26

    })