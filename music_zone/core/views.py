from django.shortcuts import render
from music.models import Album
# Create your views here.

def home(request):
    context = {
        'albums': Album.objects.all()
    }
    return render(request, 'core/home.html', context)