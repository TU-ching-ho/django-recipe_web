from django.shortcuts import render, redirect
from user.models import Recipe
# Create your views here.


def index(request):
    return render(request, "main/home.html")
