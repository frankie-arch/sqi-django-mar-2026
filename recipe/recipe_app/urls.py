from django.urls import path
from . import views

app_name = 'recipe'

urlpatterns = [
    path('',views.add_recipe, name='add_recipe'),
    path('all-recipe/',views.all_recipe, name='all_recipe'),
    path('recipe/<int:recipe_id>',views.recipe_details, name='recipe_details'),
]