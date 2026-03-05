from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def welcome(request):
    return HttpResponse("Welcome to my home page")

def intro(request):
    return HttpResponse("This is my first django page and i'm so excited to start my django journey 🎉😄")
