from django.urls import path
from . import views

app_name = "task"
urlpatterns = [
    path("", views.thetask, name="thetask"),
    path("add", views.add, name="add"),
]