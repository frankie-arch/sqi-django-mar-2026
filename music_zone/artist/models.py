from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.

class Artist(models.Model):
    name = models.CharField(max_length=200, validators= [MinLengthValidator(2)])
    debut_year = models.IntegerField()
    image = models.ImageField(upload_to="artist_pic/", blank=True, null=True)