from django.db import models

# Create your models here.

class Artist(models.Model):
    name = models.CharField(max_length=200)
    debut_year = models.IntegerField()
    image = models.ImageField(upload_to="artist_pic/", blank=True, null=True)