from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def intro_page(request):
    return HttpResponse("This is my first django page and i'm so excited to start my django journey 🎉😄")
