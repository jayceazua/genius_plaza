from django.shortcuts import render
from django.http import HttpResponse
from .models import Recipes
# Create your views here.


def index_recipe(request):
    recipes = Recipes
    context = {
        'name': 'recipe name goes here'
    }
    return render(request, 'recipes/index.html', context)


def create_recipe():
    pass


def read_recipe():
    pass


def update_receipe():
    pass


def delete_recipe():
    pass
