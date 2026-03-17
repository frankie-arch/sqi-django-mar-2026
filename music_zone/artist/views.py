from django.shortcuts import render, get_object_or_404

from .models import Artist
# Create your views here.

def artist_listing(request):
    context = {
        'artists': Artist.objects.order_by('debut_year')
    }
    return render(request, 'artist/artist.html', context)

def artist_details(request, id):
    return render(request, 'artist/artist-details.html', {'artist': get_object_or_404(Artist, pk=id)})