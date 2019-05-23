from django.contrib import admin

# Register your models here.
from .models import Recipes, Steps, Ingredients

admin.site.register(Recipes)
admin.site.register(Steps)
admin.site.register(Ingredients)
