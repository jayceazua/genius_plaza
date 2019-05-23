from django.shortcuts import render
from django.http import HttpResponse
from .models import Recipe
# Create your views here.


def index_recipe(request):
    return render(request, 'recipes/index.html')


def create_recipe(request):
    pass


def read_recipe(request, username):
    pass


def update_receipe(request, id):
    pass


def delete_recipe(request, id):
    pass
