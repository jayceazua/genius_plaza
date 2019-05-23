from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
# python3 manage.py makemigrations recipes


class Recipes(models.Model):
    # one recipe to one user
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=False)
    # many steps to one recipe
    # many ingredients to one recipe

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Recipes"


class Steps(models.Model):

    def __str__(self):
        return

    class Meta:
        verbose_name_plural = "Steps"


class Ingredients(models.Model):

    def __str__(self):
        return

    class Meta:
        verbose_name_plural = "Ingredients"
