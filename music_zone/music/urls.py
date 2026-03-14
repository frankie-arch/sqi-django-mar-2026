from django.urls import path

from . import views

app_name = 'music'

urlpatterns = [
    path('music-listing/',views.music_listing, name='music')
]