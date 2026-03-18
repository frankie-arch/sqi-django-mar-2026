from django.shortcuts import render, redirect, get_object_or_404

from .models import Recipe
from .form import RecipeForm

# Create your views here.

def all_recipe(request):
    return render(request, 'recipe_app/all-recipe.html', {'all_recipe':Recipe.objects.all()})

def recipe_details(request, recipe_id):
    return render(request, "recipe_app/recipe-details.html", {'recipe': get_object_or_404(Recipe, id=recipe_id)})

def add_recipe(request):
    form = RecipeForm()
    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("recipe:all_recipe")
    return render(request, "recipe_app/add-recipe.html",{"recipe": form})