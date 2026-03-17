from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from artist.models import Artist
# Create your models here.

def release_date_validator(value):
    year = value.year
    current_year = timezone.now().year
    if not 1800 <= year <= current_year:
        raise ValidationError(f'Year must be between 1800 and {current_year}')

class Album(models.Model):
    title = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name="album")
    release_date = models.DateField(validators=[release_date_validator])
    cover_image = models.ImageField(upload_to="album_pic/", blank=True, null=True)