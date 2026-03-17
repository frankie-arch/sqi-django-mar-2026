from django.shortcuts import render, get_object_or_404
from .models import Album
# Create your views here.

def music_listing(request):
    context = {
        'albums': Album.objects.order_by("release_date")
    }
    return render(request, 'music/music.html', context)

def album_details(request, album_id):
    return render(request, "music/album-details.html", {"album": get_object_or_404(Album, pk=album_id)})