from django.shortcuts import render

from .models import Artist
# Create your views here.

def artist_listing(request):
    context = {
        'artists': Artist.objects.all()
    }
    return render(request, 'artist/artist.html', context)