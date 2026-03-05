from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, "profile_app/index.html")

def hobbies(request):
    return render(request, "profile_app/hobbies.html")

def goals(request):
    return render(request, "profile_app/goals.html")