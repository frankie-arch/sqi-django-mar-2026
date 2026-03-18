from django.db import models

# Create your models here.

class Recipe(models.Model):
    name = models.CharField(max_length=255)
    ingredients = models.TextField()
    instructions = models.TextField()
    cooking_time = models.IntegerField()
    image = models.ImageField(upload_to="recipe_pic/", blank=True, null=True)
    cover_image = models.ImageField(upload_to="cover_pic/", default="default_cover_image.jpg")