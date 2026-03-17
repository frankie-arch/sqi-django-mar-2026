from django.urls import path

from . import views

app_name = 'music'

urlpatterns = [
    path('music-listing/',views.music_listing, name='music'),
    path('album-details/<int:album_id>/',views.album_details, name='album_details'),
]