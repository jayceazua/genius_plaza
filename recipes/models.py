from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
# python3 manage.py makemigrations recipes


class Recipe(models.Model):
    # one recipe to one user
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=False)
    # one to many recipe
    # one to many recipe

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Recipes"


class Step(models.Model):
    step_text = models.CharField(max_length=200, null=False)
    # many steps to one recipe

    def __str__(self):
        return self.step_text

    class Meta:
        verbose_name_plural = "Steps"


class Ingredient(models.Model):
    text = models.CharField(max_length=200, null=False)
    # many ingredients to one recipe

    def __str__(self):
        return self.text

    class Meta:
        verbose_name_plural = "Ingredients"
