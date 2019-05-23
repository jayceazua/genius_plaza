# from django.conf.urls import url
from django.urls import path
from .views import index_recipe, create_recipe, read_recipe, update_receipe, delete_recipe

urlpatterns = [
    # INDEX
    path('', index_recipe, name="index_recipe")
    # CREATE
    # READ
    # UPDATE
    # DELETE
]
