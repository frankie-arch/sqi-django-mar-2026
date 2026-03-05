from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def home_page(request):
    return HttpResponse('This is the home page of the sub app')

def home_views(request):
    return HttpResponse('What do you seek in here?? 🤨🙄')