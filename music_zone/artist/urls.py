from django.urls import path

from . import views

app_name = 'artist'

urlpatterns = [
    path('artist-listing/',views.artist_listing, name='artist'),
    path('artist-details/<int:id>/',views.artist_details, name='artist_details'),
]