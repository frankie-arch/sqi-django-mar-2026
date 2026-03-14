from django.db import models

from artist.models import Artist
# Create your models here.

class Album(models.Model):
    title = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    release_date = models.DateField()
    cover_image = models.ImageField(upload_to="album_pic/", blank=True, null=True)