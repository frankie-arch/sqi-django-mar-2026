from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    publication_date = models.DateField()
    cover_image = models.ImageField(upload_to='cover_image/', default='default_cover_image.jpg')
