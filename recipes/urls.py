# from django.conf.urls import url
from django.urls import path
from .views import index_recipe, create_recipe, read_recipe, update_receipe, delete_recipe

urlpatterns = [
    # INDEX
    path('', index_recipe, name="index_recipe")
    # CREATE
    # path('new', create_recipe, name="create_recipe")
    # READ
    # path('<username>', read_recipe, name="read_recipe")
    # UPDATE
    # path('update/<int:id>', update_recipe, name="update_recipe")
    # DELETE
    # path('delete/<int:id>', delete_recipe, name="delete_recipe")

]
